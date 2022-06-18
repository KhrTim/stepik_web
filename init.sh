#!/bin/bash

mkdir public;
mkdir uploads;
mkdir etc;

mkdir ./public/img;
mkdir ./public/css;
mkdir ./public/js;


if [[ -f "nginx.conf" ]]; then
    # sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default;
    # sudo /etc/init.d/nginx restart;
    echo "Existing file linked";
else
    # cp /etc/nginx/nginx.conf .;
    echo "File copied from nginx";
fi
