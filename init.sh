#!/bin/bash

mkdir public;
mkdir uploads;

mkdir ./public/img;
mkdir ./public/css;
mkdir ./public/js;




sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf;
sudo rm /etc/nginx/sites-enabled/default;

sudo /etc/init.d/nginx restart;

cd ask;
gunicorn --bind='0.0.0.0:8000' ask.wsgi;

# link gunicorn too


