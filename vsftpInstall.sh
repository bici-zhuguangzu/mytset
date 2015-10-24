#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Date    : 2015-09-25 13:11:07
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

PKGName=vsftpd
UserName=dev
Passwd=*******
ConfilePath=/etc/vsftpd/vsftpd.conf
LanIP=`ifconfig eth0|grep inet|awk -F " " '{print $2}'|awk -F ":" '{print $2}'`

InstallVsftp(){
    yum install $PKGName
}

ConfigureVsftp(){
    sed -i 's/anonymous_enable=YES/anonymous_enable=NO/g' $ConfilePath
cat <<EOF >/etc/vsftpd/vsftpd.conf
listen_address=$LanIP
listen_port=2231
chroot_local_user=NO
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd/chroot_list
EOF
    echo $UserName >/etc/vsftpd/chroot_list
}

CreateFtpUser(){
    useradd -s /sbin/nologin $UserName
    echo $Passwd|passwd --stdin $UserName
}


InstallVsftp  # ok
CreateFtpUser  # ok
ConfigureVsftp # ok
/etc/init.d/vsftpd start
