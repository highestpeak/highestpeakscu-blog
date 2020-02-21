简体中文|[English](https://github.com/highestpeak/highestpeakscu-blog)

# Introduction

highestpeakscu-blog 是一个有四川大学某位程序员编写的博客站点，它基于flask、vue，采用前后端分离的设计.其中vue的ui部分界面参照了[hexo-theme-vexo](https://github.com/yanm1ng/hexo-theme-vexo)的设计（抑或是完全的copy style）,flask后端采用flask_restful，因此后端的接口较为简洁。本仓库同时提供一个可在本地pc操作的python脚本，这完全是受到了hexo的启发，并且有多博客站点同步的想法。

这个项目的代码从哪一方面来说都是很基础的，希望本项目可以给一些朋友启发或者说可以供copy的代码吧。

希望本项目可以帮助到你。初来乍到多多关照。

# Preview

![]()

# Build & Deploy

简单详尽的部署过程

> note

- vssue评论组件在vue前端源码中，需要更改则需要重新生成前端源码dist文件夹执行
- 需要修改blogui的setting.js，更改baseURL地址为服务器地址或域名
- 服务器厂商如阿里云需要配置防火墙或安全组规则等，开启http、https、mysql相应端口过滤，以便可以访问站点
- 更改完数据库后，需要更改blog flask配置文件config.ini的mysql对应链接的值，以使得可以访问数据库

> 流程

1. blogui生成dist => 复制dist到highestpeak-blog目录下

2. 安装mysql => 添加远程用户/本地配置数据库

3. 服务器安装flask依赖 => 安装gunicorn并启动 => 安装nginx => 修改Nginx配置文件 => 运行Nginx

> 部署流程

- blogui构建

``` bash
# 对blogui生成dist文件夹
npm run build
# 复制dist文件夹到highestpeak-blog目录下
```

- mysql安装

``` bash
# 安装mysql
sudo apt-get install mysql-server
# 确认安装成功
sudo mysql_secure_installation
# 修改监听ip，将MySQL改成监听远程主机IP或者所有IP
vim /etc/mysql/mysql.conf.d/mysqld.cnf
# 找到bind-address，如果监听固定远程IP，则改成远程主机IP，若监听所有IP，则改成0.0.0.0或者注释bind-address。修改完成后重启MySQL
service mysql restart
# 查看mysql监听地址
netstat -ano | grep 3306

# 语句中，*.*代表所有库表，若想给予所有IP权限，”ip”写成“%”,所以第一句sql的意思是给予来自所有IP地址的通过“用户”，“密码”登录的用户对所有库表的所有操作权限。
grant all privileges on *.* to '用户'@'ip' identified by '密码' with grant option;
# 创建flask 使用的数据库账户,并修改相应config.ini中的数据
CREATE USER 'xxx'@'localhost' IDENTIFIED BY 'xxx';
# 授予相应权限
GRANT all privileges ON highest_blog.* TO 'xxx'@'localhost' identified by 'xxx';
# 刷新权限
flush privileges;

# 刷新权限
flush privileges;
# 重启mysql
service mysql restart
```

- 服务器安装flask依赖 、安装gunicorn并启动 

``` bash
pip install -r requirements.txt

pip install gunicorn
# app:app 为app.py文件中的 app实例
gunicorn -w 4 -b 0.0.0.0:5000 app:app
# 后台启动
nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app &
```

- 安装nginx

``` bash
apt-get install nginx
sudo nginx -t
```

配置Nginx，安装了Nginx之后，打开/etc/nginx/conf.d/default.conf，修改默认的default.conf
下面这个配置可以在一个文件内重复写多次，即可以为一台服务器一个端口匹配多个server_name

``` txt
server {
    listen 80;
    server_name localhost;
    location /{
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

``` bash
nginx -t
nginx -s reload
# 下面之一
sudo /etc/init.d/nginx start
service nginx start
```

