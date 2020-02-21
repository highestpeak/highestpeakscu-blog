import os
import xmlrpc.client

import config


class MetaWeblog:

    def __init__(self, serviceUrl, appKey, usr, passwd):
        self.serviceUrl, self.appKey, self.usr, self.passwd = serviceUrl, appKey, usr, passwd
        self.server = xmlrpc.client.ServerProxy(self.serviceUrl)

    def getUsersBlogs(self):
        return self.server.blogger.getUsersBlogs(self.appKey, self.usr, self.passwd)

    def getCategories(self, blogid=''):
        return self.server.metaWeblog.getCategories(blogid, self.usr, self.passwd)

    def getRecentPosts(self, count=5, blogid=''):
        return self.server.metaWeblog.getRecentPosts(blogid, self.usr, self.passwd, count)

    def getPost(self, id):
        return self.server.metaWeblog.getPost(id, self.usr, self.passwd)

    def newPost(self, title='Title used for test', description='this is a test post.', category='no category',
                publish=True, blogid='', **kw):
        return self.server.metaWeblog.newPost(
            blogid, self.usr, self.passwd,
            # 此处的dict中的key是最终发送时的键，是categories不是category，否则不能识别为markdown
            # 参考https://www.cnblogs.com/robert-9/p/11428982.html
            # 博客园api列表https://rpc.cnblogs.com/metaweblog/fly2wind#WpCategory
            dict(kw, title=title, description=description, categories=[category]),
            publish
        )

    def editPost(self, id, title='Title used for test', description='this is a test post.', category='no category',
                 publish=True, **kw):
        return self.server.metaWeblog.editPost(
            id, self.usr, self.passwd,
            dict(kw, title=title, description=description, category=category),
            publish
        )

    def deletePost(self, id):
        return self.server.blogger.deletePost(self.appKey, id, self.usr, self.passwd, False)


def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = open(file_path,encoding="utf-8").read()
    # print type(all_the_text)
    return all_the_text


if __name__ == '__main__':
    # metaweblog的解释
    # https://www.cnblogs.com/ans42/archive/2011/06/16/2083076.html

    cnblog = MetaWeblog(
        config.cnblog_serviceUrl,
        config.cnblog_appKey,
        config.cnblog_usr,
        config.cnblog_passwd
    )
    cnblog.newPost(
        "testpost23",
        read_file_as_str("E:\\_post\\树莓派远程配置.md"),
        category="[Markdown]"
    )
