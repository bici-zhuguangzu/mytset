#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Date    : 2015-09-23 21:49:24
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

PAckageNameInotify=
PAckageNameRsync=
InstallType=$1
UserName=
Passwd=
ServerIP=
ClientIp=
SyncPath

CreateServerConf(){
cat <<EOF >/etc/rsyncd.conf
uid = root
gid = root
use chroot = no
max connections = 100
log file = \/var\/log\/rsyncd.log
pid file = \/var\/run\/rsyncd.pid
lock file = \/var\/run\/rsync.lock
secrets file = \/etc\/server.pass
[lixuan]
path = $SyncPath
auth users = UserName
list = no
read only = no
secrets file = \/etc\/servers.pass
comment = server directory
EOF
}

CreateClientConf(){
cat <<SSS >/etc/rsyncd.conf
uid = nobody
gid = nobody
use chroot = no
max connections = 10
strict modes = yes
pid file = \/var\/run\/rsyncd.pid
lock file = \/var\/run\/rsync.lock
log file = \/var\/log\/rsyncd.log
[lixuan]
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
secrets file = \/etc\/client.pass
SSS
}

CreatePassowdServer(){
    echo $UserName:$Passwd >/etc/servers.pass
}

CreatePassowdClient(){
    echo $UserName:$Passwd >/etc/client.pass 
}

InstallInotify(){
    yum install inotify
}

InstallRsync(){
    yum install rsync
}

ConfigureRsyncServer(){
    CreateServerConf
    CreatePassowdServer
}

ConfigureRsyncClient(){
    ConfigureRsyncClient
    CreatePassowdClient
}

case $InstallType in
    Server )
        InstallInotify
        InstallInotify
        ConfigureRsyncServer
    ;;
    $InstallType in
    Client )
        InstallRsync
        ConfigureRsyncClient
    ;;
    $InstallType in
    * )
        echo "usage: Server|Client"
    ;;
esac