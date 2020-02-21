[简体中文](https://github.com/highestpeak/highestpeakscu-blog/blob/master/README.zh-CN.md)|English

# Introduction

highestpeakscu-blog is a blog site written by a programmer from Sichuan University. It is based on flask and vue and uses a front-end and back-end design. The UI part of vue refers to [hexo-theme-vexo](https: // github.com/yanm1ng/hexo-theme-vexo) design (or a complete copy style), the flask backend uses flask_restful, so the backend interface is more concise. This repository also provides a python script that can be operated on the local pc, which is completely inspired by hexo, and has the idea of synchronizing multiple blog sites.

The code of this project is very basic in every aspect. I hope this project can inspire some friends or say that the code can be copied.

Hope this project can help you. I'm here for the first time.

# Preview

![](https://raw.githubusercontent.com/highestpeak/highestpeakscu-blog/master/highestpeak-blog.gif)

# Build & Deploy

Simple and detailed deployment process

> note

- The vssue comment component is in the vue front-end source code. If you need to change, you need to regenerate the front-end source code dist folder to execute
- Need to modify the setting.js of blogui, change the baseURL address to the server address or domain name
- Server vendors such as Alibaba Cloud need to configure firewall or security group rules, and enable corresponding port filtering for http, https, and mysql so that they can access the site
- After changing the database, you need to change the value of the mysql corresponding link of the blog flask configuration file config.ini so that you can access the database

> Process

1. blogui generates dist => copy dist to highestpeak-blog directory

2. Install mysql => add remote user / local configuration database

3. Server installation flask dependency => install gunicorn and start => install nginx => modify Nginx configuration file => run Nginx

> Deployment process

- build blog UI

``` bash
# Generate dist folder for blogui
npm run build
# Copy the dist folder to the highestpeak-blog directory
```

- MySQL installation

``` bash
# Install mysql
sudo apt-get install mysql-server

# Confirm the installation was successful
sudo mysql_secure_installation

# Modify the listening IP and change MySQL to listen to the remote host IP or all IPs
vim /etc/mysql/mysql.conf.d/mysqld.cnf

# Find the bind-address. If you listen to a fixed remote IP, change it to the remote host IP. If you listen to all IPs, change it to 0.0.0.0 or comment bind-address. Restart MySQL after modification
service mysql restart

# View mysql listening address
netstat -ano | grep 3306

# In the statement, *. * Represents all library tables. If you want to give all IP permissions, "ip" is written as "%", so the first sentence of sql means to give logins through "user" and "password" from all IP addresses The user has all operation permissions on all library tables.
grant all privileges on *.* to 'user'@'ip' identified by 'password' with grant option;

# Create a database account used by flask and modify the data in the corresponding config.ini
CREATE USER 'xxx'@'localhost' IDENTIFIED BY 'xxx';

# Grant appropriate permissions
GRANT all privileges ON highest_blog.* TO 'xxx'@'localhost' identified by 'xxx';

# Refresh permissions
flush privileges;

# Refresh permissions
flush privileges;

# restart mysql
service mysql restart
```

- Server installs flask dependencies, installs gunicorn and starts

``` bash
pip install -r requirements.txt

pip install gunicorn
# app:app is the app instance in app.py
gunicorn -w 4 -b 0.0.0.0:5000 app:app
# Background startup
nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app &
```

- Install nginx

``` bash
apt-get install nginx
sudo nginx -t
```

Configure Nginx. After installing Nginx, open /etc/nginx/conf.d/default.conf and modify the default.conf.
The following configuration can be written multiple times in a file, that is, multiple server_names can be matched for a server and a port.

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
# One of the following
sudo /etc/init.d/nginx start
service nginx start
```

