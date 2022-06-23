#!/bin/bash

mkdir public;
mkdir uploads;
mkdir etc;

mkdir ./public/img;
mkdir ./public/css;
mkdir ./public/js;


mv nginx.conf etc/;




sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf;
sudo rm /etc/nginx/sites-enabled/default;

sudo /etc/init.d/nginx restart;

sudo /etc/init.d/mysql start;
mysql -uroot -e "create database web;";
mysql -uploads -e "create user 'tim'@'localhost'"
mysql -uroot -e "grant all privileges on stepic_web.* to 'tim'@'localhost' with grant option;";
~/web/ask/manage.py makemigrations;
~/web/ask/manage.py migrate;

cd ask;
gunicorn --bind='0.0.0.0:8000' ask.wsgi;

# link gunicorn too


