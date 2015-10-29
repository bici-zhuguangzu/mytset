#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Date    : 2015-10-10 16:15:15
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$
# @Desc        :init system

DelUnavilableAccount(){
    userdel adm
    userdel lp
    userdel sync
    userdel shutdown
    userdel halt
    userdel news
    userdel uucp
    userdel operator
    userdel games
    userdel gopher
}

DelUnavilableGroup(){
    groupdel adm
    groupdel lp
    groupdel news
    groupdel uucp
    groupdel games
    groupdel dip
    groupdel pppusers
    groupdel popusers
    groupdel slipusers
}

DelUnavilableService(){
    
}

DisableIpV6(){
    
}

youhua(){
    
}

Addrepo(){
    yum -y install epel-release
    rpm -ivh http://apt.sw.be/redhat/el6/en/x86_64/rpmforge/RPMS/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
}

