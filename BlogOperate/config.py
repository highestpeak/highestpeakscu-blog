# Repository location, where blog posts are saved
# Full address
blogPath = r"xxxxxx"
# Local sqlite temporary file location. 
# This file can back up a blog post data locally, while reducing the number of updates to the server.
# Full address
sqllitePath = r"xxxxx"
# Warehouse article api address, 
# the article content in the database only saves this address, 
# the front end requests the corresponding github api to get the content
# github api format please Check out github v4 api
# replace userName/userRepo to you own name and repo string
repoUrlFomart = r"https://api.github.com/repos/userName/userRepo/contents/{name}?ref=master"
# github access operation
# You must apply for the corresponding token on github to give permission to modify the repository
# replace userName/userRepo to you own name and repo string
github_access_token = "xxxxxx"
repoName = "userName/userRepo"
# cnblog metaweblog Operating parameters
# replace username passward to you own string
cnblog_serviceUrl, cnblog_appKey = 'https://rpc.cnblogs.com/metaweblog/username', 'username'
cnblog_usr, cnblog_passwd = 'username', 'passward'
sleepTime = 30  # cnblog, one blog post can only be published within 30 seconds
# Blog server server address and modify secret_key
server = "http://127.0.0.1:5000"
secret_key = "123456"
