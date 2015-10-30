#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# DESC     : nginx status
# @Date    : 2015-10-29 19:09:12
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

lan=`ifconfig eth0|grep inet|awk -F " " '{print $2}'|awk -F ":" '{print $2}'`

AddConfForNginxStat(){
    cat > status.conf << EOF
server {
    listen       8080;
    server_name  _;

    include /etc/nginx/default.d/*.conf;

    location / {
    stub_status on;
    access_log off;
 }

    error_page  404              /404.html;
    location = /404.html {
        root   /usr/share/nginx/html;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
EOF
}

AddConfForNginxStat
/etc/init.d/nginx  restart
curl 127.0.0.1:8080/