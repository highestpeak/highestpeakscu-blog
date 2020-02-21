import time
from collections import namedtuple

import frontmatter
import requests
from github import Github
from tqdm import tqdm

from APIKey import articleKey, repoKey, tagKey
from config import github_access_token, repoName, cnblog_serviceUrl, cnblog_appKey, cnblog_usr, cnblog_passwd, server, \
    sleepTime
from localSqlite import getFileTitleCnID, isFileInfoChanged
from metaweblog import MetaWeblog, read_file_as_str

articleHash = articleKey()
tagHash = tagKey()
repoHash = repoKey()


def readMdContent(file):
    post = frontmatter.load(file)
    content = post.content
    return content


# post fuctions

def githubFuc(itemList, tag):
    mdFiles = [postItem["fileInfo"] + (postItem["type"],) for postItem in itemList]
    errorinfo = []
    g2, repo = None, None
    try:
        g2 = Github(github_access_token)
        repo = g2.get_repo(repoName)
    except Exception:
        errorinfo.append("github: connect error!")
    pbar = tqdm(total=mdFiles.__len__())
    for md in mdFiles:
        pbar.set_description(md[0])
        try:
            if md[2] == "post":
                repo.create_file(md[0], "post article", readMdContent(md[1]), branch="master")
            elif md[2] == "update":
                contents = repo.get_contents(md[0], ref="master")
                repo.update_file(contents.path, "update article", readMdContent(md[1]), contents.sha, branch="master")
            elif md[2] == "delete":
                contents = repo.get_contents(md[0], ref="master")
                repo.delete_file(contents.path, "delete article", contents.sha, branch="master")
        except Exception as e:
            errorinfo.append("github: " + md[0] + " error!")
            pbar.set_description("github: " + md[0] + " error!")
        pbar.update(1)
    pbar.close()
    return errorinfo


def serverFuc(itemList, tag):
    errorinfo = []

    def articleFuc(items, api):
        mdInfo = [(postItem["server"], postItem["type"]) for postItem in items]
        pbar = tqdm(total=mdInfo.__len__())
        for md in mdInfo:
            pbar.set_description(md[0]["title"])
            md[0].update({"hash": articleHash})
            try:
                if md[1] == "post":
                    # todo: error can be here
                    requests.post(api, data=md[0])
                elif md[1] == "update":
                    if isFileInfoChanged(md[0]):
                        requests.put(api, data=md[0])
                elif md[1] == "delete":
                    requests.delete(api, data=md[0])
            except ConnectionError:
                errorinfo.append("serrver: " + md[0]["title"] + " connection error!")
                pbar.set_description(md[0]["title"] + "connection error!")
            pbar.update(1)
        pbar.close()

    def tagFuc(items, api):
        tagInfo = [(postItem["server"], postItem["type"]) for postItem in items]
        pbar = tqdm(total=tagInfo.__len__())
        for tagI in tagInfo:
            pbar.set_description(tagI[0]["name"])
            tagI[0].update({"hash": tagHash})
            try:
                if tagI[1] == "update":
                    requests.put(api, data=tagI[0])
                elif tagI[1] == "delete":
                    requests.delete(api, data=tagI[0])
            except ConnectionError:
                errorinfo.append("serrver: " + tagI[0]["name"] + " connection error!")
                pbar.set_description(tagI[0]["name"] + "connection error!")
            pbar.update(1)
        pbar.close()

    def repoFuc(items, api):
        repoInfo = [(postItem["server"], postItem["type"]) for postItem in items]
        pbar = tqdm(total=repoInfo.__len__())
        pbar.set_description("repo")
        for repo in repoInfo:
            repo[0].update({"hash": repoHash})
            try:
                if repo[1] == "post":
                    requests.post(api, data=repo[0])
                elif repo[1] == "delete":
                    requests.delete(api, data=repo[0])
            except ConnectionError:
                errorinfo.append("serrver: " + repo[0] + " connection error!")
                pbar.set_description("connection error!")
            pbar.update(1)
        pbar.close()

    serverApi = server
    if tag == "article":
        serverApi += "/api/article"
        articleFuc(itemList, serverApi)
    elif tag == "tags":
        serverApi += "/api/tags"
        tagFuc(itemList, serverApi)
    elif tag == "repo":
        serverApi += "/api/repo"
        repoFuc(itemList, serverApi)

    return errorinfo


def cnBlogFuc(itemList, tag):
    mdFiles = [(postItem["server"]["title"], postItem["fileInfo"][1], postItem["type"], postItem["fileInfo"][0]) for
               postItem in itemList]
    cnblog = MetaWeblog(cnblog_serviceUrl, cnblog_appKey, cnblog_usr, cnblog_passwd)

    errorinfo = []
    cnIDDict = {}
    pbar = tqdm(total=mdFiles.__len__())
    i = len(mdFiles) - 1
    while True:
        md = mdFiles[i]
        pbar.set_description(md[0])
        mdID = None
        try:
            if md[2] == "post":
                mdID = cnblog.newPost(
                    md[0],
                    readMdContent(md[1]),
                    category="[Markdown]"
                )
            elif md[2] == "update":
                mdID=getFileTitleCnID(md[0])
                cnblog.editPost(
                    mdID,
                    md[0],
                    readMdContent(md[1]),
                    category="[Markdown]"
                )
            elif md[2] == "delete":
                mdID = getFileTitleCnID(md[0])
                cnblog.deletePost(
                    mdID
                )
        except Exception as e:
            errorinfo.append("cnblog: " + md[0] + "error!")
            pbar.set_description("cnblog: " + md[0] + "error!")
            i -= 1
            if i < 0:
                pbar.update(1)
                break
            pbar.update(1)
            continue
        cnIDDict[md[0]] = mdID
        i -= 1
        if i < 0:
            pbar.update(1)
            break
        pbar.set_description("next 30s.")
        time.sleep(sleepTime)
        pbar.update(1)
    pbar.close()
    return cnIDDict, errorinfo


WebModel = namedtuple("PostModel", ["modelName", "modelFunction"])
GithubModel = WebModel(modelName='GithubPost', modelFunction=githubFuc)
ServerModel = WebModel(modelName='ServerPost', modelFunction=serverFuc)
CnBlogModel = WebModel(modelName='CnBlogPost', modelFunction=cnBlogFuc)
