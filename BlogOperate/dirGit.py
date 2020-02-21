import os
import sys

from git import Repo


class MdRepo(object):
    def __init__(self, path):
        if path is None:
            raise Exception("repo path can not be none")
        elif ".git" not in os.listdir(path):
            raise Exception("path dir must be git repo")
        self.repo = Repo(path)
        self.fileList = {
            "untracked": self.repo.untracked_files,
            "modified": [self.getDncodePath(m.a_path) for m in self.repo.index.diff(None) if m.change_type == "M"],
            "delete": [self.getDncodePath(m.a_path) for m in self.repo.index.diff(None) if m.change_type == "D"],
            "staged": [self.getDncodePath(m.a_path) for m in self.repo.index.diff("HEAD")],
        }

    def isDirty(self):
        return self.repo.is_dirty()

    def getDncodePath(self, path):
        if path[0] == path[-1] == '"':
            path = path[1:-1]
        return path.encode('ascii').decode('unicode_escape').encode('latin1').decode(sys.getfilesystemencoding())

    def files(self):
        return self.fileList

    def renames(self, namelist):
        for name in namelist:
            self.repo.git.execute('git mv '+name[0]+' '+name[1])

    def commit(self):
        for addfile in self.fileList["untracked"] + self.fileList["modified"] + self.fileList["staged"]:
            self.repo.index.add(addfile)
        for delfile in self.fileList["delete"]:
            self.repo.index.remove(delfile, working_tree=True)
        self.repo.index.commit('md file commit')

    def push(self):
        self.repo.remote().push()

    def pull(self):
        self.repo.remote().pull()


if __name__ == '__main__':
    path = r"E:\_data\test\2019"
    mdrepo = MdRepo(path)
    files = mdrepo.files()
    mdrepo.renames([("test.txt", "testrest.txt")])
    mdrepo.commit()
    print("hello world")
