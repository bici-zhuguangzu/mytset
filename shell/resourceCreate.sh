#!/bin/bash
unset install
lan=`ifconfig eth0|grep inet|awk -F " " '{print $2}'|awk -F ":" '{print $2}'`
path_now=`pwd`
path=/usr/share/nginx/html
install(){
    rpm -i http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
    yum -y install nginx
}
download(){
    cd $path
    mkdir package&&cd package
    wget -c `cat /root/ResourceCenter/pkglist`
}
move2nginx(){
    cp -r $path_now/shell $path
    cp -r $path_now/conf $path
    mkdir －p $path/code
}
chginitscript(){
    sed -i "s/192.168.12.209/$lan/g" $path/conf/init.sh
}
install
download
move2nginx
chginitscript

