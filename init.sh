#!/bin/bash

mkdir public;
mkdir uploads;
mkdir etc;

mkdir ./public/img;
mkdir ./public/css;
mkdir ./public/js;



sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf;
sudo /etc/init.d/nginx restart;
echo "Existing file linked";
