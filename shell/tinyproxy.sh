#!/bin/bash
#安装tinyproxy
InstallTinyproxy(){
    yum install tinyproxy
}

#配置tinyproxy
ConfTinyproxy(){
    sed -i "s/Allow=127.0.0.1/#Allow=127.0.0.1/g" /etc/tinyproxy/tinyproxy.conf
}

InstallTinyproxy
ConfTinyproxy