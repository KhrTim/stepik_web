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

gunicorn --bind='0.0.0.0:8080' hello:wsgi_processor_make_file;

# link gunicorn too


