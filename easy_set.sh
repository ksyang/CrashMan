#!/bin/bash
export LC_ALL=C
apt-get install -y python python-pip python3 python3-pip ufw git mysql-client mysql-server libmysqlclient-dev curl
curl -fsSL https://get.docker.com/ | sudo sh
pip3 install django pymysql mysqlclient
pip install flask flask-mysql
mysql -uroot -p -e "create database crashMan"
