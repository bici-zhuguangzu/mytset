#!/bin/bash
#read hostname from file
#
#init server
unset install
HostnameNew=`cat hostname.txt`
lan=`ifconfig eth0|grep inet|awk -F " " '{print $2}'|awk -F ":" '{print $2}'`
ServerType=`cat hostname.txt|awk -F "[0-9]" '{print$1}'`
ShellPath=resource/shell

AddYumProxy(){
    echo proxy=proxyip:proxyport >>/etc/yum.conf
}

AddYumRepo(){
    yum -y install epel-release
}

BasePkg(){
    yum -y install epel-release
    yum -y install gcc
}

ChgHostname(){
    sed -i "s/`hostname`/$HostnameNew/g" /etc/sysconfig/network
    hostname $HostnameNew
}

AddHosts(){
    echo 192.168.12.209 resource >>/etc/hosts
    echo $lan $HostnameNew >>/etc/hosts
}
chglogkey(){
    sed -i "s/logkey/$ServerType/g /etc/logstash/shipper.conf"
}
BuildApi(){
    wget $ShellPath/nodejs.sh
    sh nodejs.sh
}

BuildCollection(){
    wget $ShellPath/mongodb.sh
    sh mongodb.sh
}

BuildLB(){
    wget $ShellPath/nginx.sh
    sh nginx.sh
}

BuildIMG(){
    wget $ShellPath/nodejs.sh
    sh nodejs.sh
    yum -y install ImageMagick ImageMagick-devel
}

BuildMQ(){
    wget $ShellPath/redis.sh
    sh redis.sh
}

InstallZabbixAgent(){
    wget $ShellPath/zabbix-agent.sh
    sh zabbix-agent.sh
}

BuildZabbixServer(){
    wget $ShellPath/zabbix-server.sh
    sh zabbix-server.sh
}

BuildLogingcenter(){
    wget $ShellPath/Collection2ESTemple.sh
    sh Collection2ESTemple
}

InstallLogstash(){
    wget $ShellPath/Collection2RedisTemple.sh
    sh Collection2RedisTemple.sh
}

AddYumProxy
AddYumRepo
BasePkg
ChgHostname
AddHosts
InstallZabbixAgent
case  $ServerType in
    APINode)
        BuildApi
        cd /home
        wget resource/code/Service.tgz
        tar zxvf Server.tgz
    ;;
    CollectionNode)
        BuildCollection
    ;;
    LBNode)
        BuildLB
    ;;
    ImageProcessNode)
        BuildApi
        yum -y install ImageMagick ImageMagick-devel
        cd /home
        wget resource/code/Tracker.tgz
        tar zxvf Tracker.tgz
    ;;
    MQNode)
        BuildMQ
    ;;
    LoggingCenter)
        BuildLogingcenter
    ;;
    logMQ)
        BuildMQ
    ;;
    MonitoringCenter)
        BuildZabbixServer
    ;;
    ConfigurationCenter)
        BuildMQ
    ;;
esac
