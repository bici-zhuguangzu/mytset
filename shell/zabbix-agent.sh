#!/bin/bash
unset install
serverip=192.168.12.210
##input serverip when you have a server
install(){
    #export yum respoese
    wget resource/package/zabbix-release-2.4-1.el6.noarch.rpm
    rpm -ivh zabbix-release-2.4-1.el6.noarch.rpm
    #install zabbix-agent
    yum -y install zabbix-agent
}

conf(){
    #configure zabbix-agent
    sed -i "s/Server=127.0.0.1/Server=$serverip/g" /etc/zabbix/zabbix_agentd.conf
    sed -i "s/ServerActive=127.0.0.1/ServerActive=$serverip:10051/g" /etc/zabbix/zabbix_agentd.conf
    sed -i "s/Hostname/#Hostname/g" /etc/zabbix/zabbix_agentd.conf
    echo ListenIP=`ifconfig eth0|grep inet|awk -F " " '{print $2}'|awk -F ":" '{print $2}'` >> /etc/zabbix/zabbix_agentd.conf
    echo `hostname` >> /etc/zabbix/zabbix_agentd.conf
    echo HostMetadataItem=system.uname >> /etc/zabbix/zabbix_agentd.conf
}
install
conf
/etc/init.d/zabbix-agent start
chkconfig zabbix-agent on