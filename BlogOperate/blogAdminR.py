import argparse

import frontmatter
from tqdm import tqdm

from APIKey import articleKey, tagKey, repoKey
from config import blogPath as blogPath, repoUrlFomart
from dirGit import MdRepo
from localSqlite import getFileNameTitle, writeFileInfo, isTitleIn, closeDB, createDB, rename
from webModel import WebModel, GithubModel, ServerModel, CnBlogModel


def readMdFront(file):
    post = frontmatter.load(file)
    front = post.metadata

    if "tags" not in front.keys():
        front["tags"] = []
    if "title" not in front.keys():
        front["title"] = None
    if "description" not in front.keys():
        front["description"] = None
    if "create_time" not in front.keys():
        front["create_time"] = None

    error = "error:"
    for key in front.keys():
        if key not in {"tags", "title", "description", "create_time", }: error += key + " "
    error = (error + "can not identify") if error != "error:" else ""

    return front, error


def fileTuple(path, relativePath):
    fileType = relativePath[relativePath.rfind("."):]
    nameStartIndex = relativePath.rfind("/")
    if nameStartIndex == -1:
        nameStartIndex = 0
    fileName = relativePath[nameStartIndex:]
    filePath = path + "\\" + relativePath.replace("/", "\\")
    return fileName, filePath, fileType


def getContentMdUrl(filename):
    content = repoUrlFomart.format(name=filename)
    return content


class BlogAdmin(object):
    def __init__(self, webModels=None):
        for model in webModels:
            if not isinstance(model, WebModel):
                raise Exception("post model function error")
        self.webModels = webModels
        self.errorInfo = []

    def fileOperate(self, path):
        print("process repos...")
        # process repos
        localRepo = MdRepo(path)
        files = localRepo.files()
        # ensure type is md file, read name\path\type for this md file,others will jump
        fileInfoList = {"untracked": [], "modified": [], "delete": [], "staged": []}
        for type, fileL in files.items():
            for fileI in fileL:
                fileInfo = fileTuple(path, fileI)
                if fileInfo[2] != ".md":
                    self.errorInfo.append("warning: new file: " + fileInfo[0] + " is not md file.")
                else:
                    fileInfoList[type].append(fileInfo[0:2])

        print("process diferent file type list...")
        # get files to operate
        fileList = []
        fileList += self.newFile(fileInfoList["untracked"])
        fileList += self.modifyFile(fileInfoList["modified"])
        fileList += self.delFile(fileInfoList["delete"])
        # filelist is empty
        if len(fileList) == 0: return

        for fileS in fileList:
            print(files["type"]+":"+fileS["fileInfo"][0])
        ensure = input("are you sure to operate these files?(y/n)").replace(" ", "")
        if ensure == "n" or ensure == "N":
            exit(-1)
        elif ensure == "y" or ensure == "Y":
            pass
        else:
            exit(-1)

        print("send article info to web...")
        # send article info to web
        cnIDDict = {}
        print([model.modelName for model in self.webModels])
        for model in self.webModels:
            print(model.modelName + " ...")
            if model.modelName == "CnBlogPost":
                cnIDDict, errorinfo = model.modelFunction(fileList, tag="article")
            else:
                errorinfo = model.modelFunction(fileList, tag="article")
            if len(errorinfo) != 0:
                self.errorInfo += errorinfo

        print("write info to sqlite...")
        # write info to csv
        fileInfoList = []
        for file in fileList:
            if file["type"] == "delete":
                fileInfoList.append({
                    "title": file["server"]["title"],
                    "type": file["type"],
                })
            else:
                fileInfoList.append({
                    "filename": file["fileInfo"][0],
                    "title": file["server"]["title"],
                    "description": file["server"]["description"],
                    "tags": file["server"]["tags"],
                    "createtime": file["server"]["create_time"],
                    "cnblogid": cnIDDict[file["server"]["title"]],
                    "type": file["type"],
                })
        writeFileInfo(fileInfoList)

        print("commit...")
        localRepo.commit()

    def mdHeadOperate(self, filePath, type="new"):
        # read front matter of the md file
        md, error = readMdFront(filePath)
        if error != "":
            self.errorInfo.append(error)
            return None
        # ensure the only title-title in md must not in csv(server-database\cnblog\etc)
        if type == "new" and isTitleIn(md["title"]):
            self.errorInfo.append("error: title " + md["title"] + " already in database."
                                                                  "Rename or Duplicate title appears!")
            for info in self.errorInfo:
                print(info)
            exit(-1)
            # return None
        return md

    def newFile(self, fileInfoList):
        postList = []
        for fileInfo in fileInfoList:
            md = self.mdHeadOperate(fileInfo[1], type="new")
            if md is None: continue
            postList.append({
                "server": {
                    "title": md["title"],
                    "description": md["description"],
                    "repourl": getContentMdUrl(fileInfo[0]),
                    "create_time": md["create_time"].strftime("%Y-%m-%d %H:%M:%S"),
                    "tags": md["tags"],
                },
                "fileInfo": fileInfo,
                "type": "post",
            })
        return postList

    def modifyFile(self, fileInfoList):
        modifyFileList = []
        for fileInfo in fileInfoList:
            md = self.mdHeadOperate(fileInfo[1], type="modify")
            if md is None: continue
            modifyFileList.append({
                "server": {
                    "title": md["title"],
                    "description": md["description"],
                    "create_time": md["create_time"].strftime("%Y-%m-%d %H:%M:%S"),
                    "tags": md["tags"],
                },
                "fileInfo": fileInfo,
                "type": "update",
            })
        return modifyFileList

    def delFile(self, fileInfoList):
        delFileList = []
        for fileInfo in fileInfoList:
            delFileList.append({
                "server": {
                    "title": getFileNameTitle(fileInfo[0]),
                },
                "fileInfo": fileInfo,
                "type": "delete",
            })
        return delFileList

    def tagOperate(self, operate):
        tags = []
        print("input -1 to exit;others continue")
        if operate == "modify":
            self.modifyTag(tags)
        elif operate == "del":
            self.delTag(tags)
        for tag in tags:
            print(tag)
        ensure = input("are you sure to operate these tags?(y/n)").replace(" ", "")
        if ensure == "n" or ensure == "N":
            exit(-1)
        elif ensure == "y" or ensure == "Y":
            for model in self.webModels:
                if model.modelName != "ServerPost":
                    continue
                model.modelFunction(tags, tag="tags")

    def modifyTag(self, tags):
        while True:
            label = input("Input label: ").replace(" ", "")
            if label == "-1":
                break
            tagname = input("Input tag name: ").replace(" ", "")
            tagDescription = input("Input tag description: ").replace(" ", "")
            tags.append({
                "server": {
                    "name": tagname,
                    "description": tagDescription,
                },
                "type": "update"
            })

    def delTag(self, tags):
        while True:
            label = input("Input label:").replace(" ", "")
            if label == "-1":
                break
            tagname = input("Input tag name: ").replace(" ", "")
            tags.append({
                "server": {
                    "name": tagname,
                },
                "type": "delete"
            })

    def repoOperate(self, operate):
        repos = []
        print("input -1 to exit;others continue")
        print("repo-api-format: https://api.github.com/repos/{username}/{reponame}")
        if operate == "add":
            self.addRepo(repos)
        elif operate == "del":
            self.delRepo(repos)
        print("repos list:")
        for repo in repos:
            print(repo)
        ensure = input("are you sure to operate these repos?(y/n)").replace(" ", "")
        if ensure == "n" or ensure == "N":
            exit(-1)
        elif ensure == "y" or ensure == "Y":
            for model in self.webModels:
                if model.modelName != "ServerPost":
                    continue
                model.modelFunction(repos, tag="repo")

    def addRepo(self, repos):
        while True:
            label = input("Input label:").replace(" ", "")
            if label == "-1":
                break
            repoUrl = input("Input repo api url: ").replace(" ", "")
            repos.append({
                "server": {
                    "url": repoUrl,
                },
                "type": "post"
            })

    def delRepo(self, repos):
        while True:
            label = input("Input label:").replace(" ", "")
            if label == "-1":
                break
            repoUrl = input("Input repo api url: ").replace(" ", "")
            repos.append({
                "server": {
                    "url": repoUrl,
                },
                "type": "delete"
            })

    def renameOperate(self):
        renameList = []
        print("update old filenames to newnames.")
        print("input -1 to exit;others continue")
        while True:
            label = input("Input label:").replace(" ", "")
            if label == "-1":
                break
            oldname = input("Input old filename: ").replace(" ", "")
            newname = input("Input new filename: ").replace(" ", "")
            renameList.append((oldname, newname))

        for name in renameList:
            print(name[0]+"==>"+name[1])
        ensure = input("are you sure to rename these files?(y/n)").replace(" ", "")
        if ensure == "n" or ensure == "N":
            exit(-1)
        elif ensure == "y" or ensure == "Y":
            pass
        else:
            exit(-1)

        print("change git names to new...")
        localRepo = MdRepo(path)
        localRepo.renames(renameList)
        localRepo.commit()
        print("change db rows to new...")
        rename(renameList)


if __name__ == '__main__':
    # args parser
    parser = argparse.ArgumentParser(description='Process blog admin...')
    parser.add_argument("type", type=str,
                        choices=["article", "modify-tag", "del-tag", "add-repo", "del-repo", "initdb", "rename", ], )
    args = parser.parse_args()
    d = args.__dict__

    # operate function
    path = blogPath
    webModels = [GithubModel, ServerModel, CnBlogModel, ]
    blog = BlogAdmin(webModels=webModels)
    dtype = d["type"]
    if dtype == "article":
        blog.fileOperate(path)
    elif dtype == "modify-tag":
        blog.tagOperate("modify")
    elif dtype == "del-tag":
        blog.tagOperate("del")
    elif dtype == "add-repo":
        blog.repoOperate("add")
    elif dtype == "del-repo":
        blog.repoOperate("del")
    elif dtype == "rename":
        blog.renameOperate()
    elif dtype == "initdb":
        print("create db table...")
        createDB()

    print("close db...")
    closeDB()

    print("Have a nice day!")
