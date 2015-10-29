#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# DESC     : install salt
# @Date    : 2015-10-28 14:32:04
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

InstallMaster(){
    yum -y install salt-master
    sed -i 's/#auto_accept: False/auto_accept: True/' /etc/salt/master
    sed -i "s/#interface: 0.0.0.0/interface: `ifconfig eth0|grep inet|awk -F " " '{print $2}'|awk -F ":" '{print $2}'`/"  /etc/salt/master
    /etc/init.d/salt-master start
    chkconfig salt-master on
}

InstallMinion(){
    yum -y install salt-minion
    sed -i 's/#master: salt/master: 192.168.10.191/' /etc/salt/minion
    /etc/init.d/salt-minion start
    chkconfig salt-minion on
}


case $1 in
    master )
        InstallMaster
    ;;
    minion )
        InstallMinion
    ;;
esac