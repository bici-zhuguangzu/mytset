#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Date    : 2015-09-21 22:42:47
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

sql_createdb="CREATE DATABASE IF NOT EXISTS ${newusername};"
sql_createuser="CREATE USER '${newusername}' IDENTIFIED BY '${newuserpass}';"
sql_grant="GRANT ALL PRIVILEGES ON \`${newusername}\`.* TO '${newusername}'@'%';"
sql_add="${sql_createdb}${sql_createuser}${sql_grant}"
echo $sql_grant; # 测试sql语句是否正常
# mysql $mysqlroot password$mysqlpass execute"$sql_add"