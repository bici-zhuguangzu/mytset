#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Date    : 2015-09-21 22:42:47
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

DBName=$1
DBUser=$2
DBPasswd=$3
notice="脚本名称后按顺序输入 DBName DBUser DBPasswd"


CerateDatabase(){
    sql_createdb="CREATE DATABASE IF NOT EXISTS ${DBName} character set utf8 collate utf8_bin;"
    sql_createuser="CREATE USER '${DBUser}' IDENTIFIED BY '${DBPasswd}';"
    sql_grant="GRANT ALL PRIVILEGES ON \`${DBName}\`.* TO '${DBUser}'@'%';"
    sql_add="${sql_createdb}${sql_createuser}${sql_grant}"
    echo $sql_grant; # 测试sql语句是否正常
    mysql -uroot -e "${sql_add}"
}


CerateDatabase||echo ${notice}