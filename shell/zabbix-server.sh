#!/bin/bash

#数据库名称和数据库密码
newusername=zabbix
newuserpass=********

install(){
    rpm -ivh http://repo.zabbix.com/zabbix/2.4/rhel/6/x86_64/zabbix-release-2.4-1.el6.noarch.rpm
    yum -y install curl curl-devel net-snmp net-snmp-devel perl-DBI php-gd php-xml php-bcmath
    yum -y install httpd
    yum -y install php php-mysql php-common php-gd php-mbstring php-mcrypt php-devel php-xml
    yum -y install zabbix-server-mysql zabbix-web-mysql
    /etc/init.d/mysqld start
}
conf(){
    Mysql=`which mysql`
    sql_createdb="CREATE DATABASE IF NOT EXISTS ${newusername};"
    sql_createuser="CREATE USER '${newusername}' IDENTIFIED BY '${newuserpass}';"
    sql_grant="GRANT ALL PRIVILEGES ON \`${newusername}\`.* TO '${newusername}'@'%';"
    sql_add="${sql_createdb}${sql_createuser}${sql_grant}"
    Mysql -uroot -e "$sql_add"
    SqlDir=`echo /usr/share/doc/zabbix-server-mysql*`
    cd $SqlDir/create
    mysql -uroot zabbix < schema.sql
    mysql -uroot zabbix < images.sql
    mysql -uroot zabbix < data.sql
    echo DBPassword= ${newuserpass}>>/etc/zabbix/zabbix_server.conf
}
AddOnBoot(){
    /etc/init.d/httpd start
    /etc/init.d/zabbix-server start
    chkconfig zabbix-server on
    chkconfig httpd on
    chkconfig mysqld on
}
install
conf
AddOnBoot

