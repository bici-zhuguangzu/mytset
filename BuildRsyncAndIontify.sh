#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Date    : 2015-09-23 21:49:24
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

PAckageNameInotify=inotify-tools
PAckageNameRsync=rsync
PAckageNameXinetd=xinetd
InstallType=$1
UserName=root
Passwd=bici!@#Sync
ServerIP=10.172.6.233
ClientIp1=10.170.224.93
ClientIp2=10.173.37.171
SyncPath=/home/dev/Service/
moduleName=bicicode

CreateServerConf(){
cat <<EOF >/etc/rsyncd.conf
uid = root
gid = root
use chroot = no
max connections = 100
log file = /var/log/rsyncd.log
pid file = /var/run/rsyncd.pid
lock file = /var/run/rsync.lock
secrets file = /etc/server.pass
[$moduleName]
path = $SyncPath
auth users = UserName
hosts allow = 10.0.0.0/255.0.0.0,$ClientIp1
list = no
read only = no
secrets file = /etc/servers.pass
comment = server directory
EOF
chmod 600 /etc/rsyncd.conf
}

CreateClientConf(){
cat <<SSS >/etc/rsyncd.conf
uid = nobody
gid = nobody
use chroot = no
max connections = 10
strict modes = yes
pid file = /var/run/rsyncd.pid
lock file = /var/run/rsync.lock
log file = /var/log/rsyncd.log
[$moduleName]
path = $SyncPath
comment = client file
ignore errors
read only = no
write only = no
hosts allow = $ServerIP
hosts deny = *
list = false
uid = root
gid = root
auth users = $UserName
secrets file = /etc/client.pass
SSS
chmod 600 /etc/rsyncd.conf
}

CreatePassowdServer(){
    echo $UserName:$Passwd >/etc/servers.pass
}

CreatePassowdClient(){
    echo $UserName:$Passwd >/etc/client.pass
}

InstallInotify(){
    yum -y install $PAckageNameInotify
}

InstallRsync(){
    yum -y install $PAckageNameRsync
    yum -y install $PAckageNameXinetd
}

ConfigureRsyncServer(){
    sed -i "s/yes/no/g" /etc/xinetd.d/rsync
    CreateServerConf
    CreatePassowdServer
}

ConfigureRsyncClient(){
    sed -i "yes/no/g" /etc/xinetd.d/rsync
    CreateClientConf
    CreatePassowdClient
}

case $InstallType in
    Server )
        InstallInotify
        InstallInotify
        ConfigureRsyncServer
        service xinetd start
    ;;
    Client )
        InstallRsync
        ConfigureRsyncClient
        service xinetd start
    ;;
    * )
        echo "usage: Server|Client"
    ;;
esac
