#!/bin/bash
##声明包名
wan=`ifconfig eth1|grep inet|awk -F " " '{print $2}'|awk -F ":" '{print $2}'`
PKGName=nginx-release-centos-6-0.el6.ngx.noarch.rpm
unset install
install(){
    #下载yum源安装包，导入yum源
    wget resource/package/$PKGName
    rpm -ivh $PKGName
    yum makecache
    #使用yum安装nginx
    yum install nginx
}
conf(){
    #下载配置文件并放入到对应位置
    wget resource/conf/default.conf
    wget resource/conf/nginx.conf
    wget resource/conf/aid.conf
    wget resource/conf/intranet.conf
    mv default.conf /etc/nginx/conf.d
    mv aid.conf /etc/nginx/conf.d
    mv intranet.conf /etc/nginx/conf.d
    mv nginx.conf /etc/nginx
    sed -i "s/serverip/$wan/g"      /etc/nginx/conf.d/default.conf
}


install
conf
#开启nginx服务
/etc/init.d/nginx start
