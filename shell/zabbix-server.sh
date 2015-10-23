#!/bin/bash

#数据库名称和数据库密码
newusername=zabbix
newuserpass=********

install(){
    #先安装yum源   方便yum安装zabbix
    rpm -ivh http://repo.zabbix.com/zabbix/2.4/rhel/6/x86_64/zabbix-release-2.4-1.el6.noarch.rpm
    #先配置服务器端  安装lamp环境
    yum -y install curl curl-devel net-snmp net-snmp-devel perl-DBI php-gd php-xml php-bcmath
    yum -y install httpd
    yum -y install php php-mysql php-common php-gd php-mbstring php-mcrypt php-devel php-xml
    #然后开始配置安装zabbix
    yum -y install zabbix-server-mysql zabbix-web-mysql
    /etc/init.d/mysqld start
}
conf(){
    #配置mysql数据库
    #先配置用户和权限
    Mysql=`which mysql`
    sql_createdb="CREATE DATABASE IF NOT EXISTS ${newusername};"
    sql_createuser="CREATE USER '${newusername}' IDENTIFIED BY '${newuserpass}';"
    sql_grant="GRANT ALL PRIVILEGES ON \`${newusername}\`.* TO '${newusername}'@'%';"
    sql_add="${sql_createdb}${sql_createuser}${sql_grant}"
    Mysql -uroot -e "$sql_add"
    #然后导入数据库
    SqlDir=`echo /usr/share/doc/zabbix-server-mysql*`
    cd $SqlDir/create
    mysql -uroot zabbix < schema.sql
    mysql -uroot zabbix < images.sql
    mysql -uroot zabbix < data.sql
    # 修改zabbix_server.conf配置文件
    echo DBPassword= ${newuserpass}>>/etc/zabbix/zabbix_server.conf
}
AddOnBoot(){
    chkconfig zabbix-server on
    chkconfig httpd on
    # 启动zabbix－server
    /etc/init.d/httpd start
    /etc/init.d/zabbix-server start
    chkconfig mysqld on
}
install
conf
AddOnBoot

