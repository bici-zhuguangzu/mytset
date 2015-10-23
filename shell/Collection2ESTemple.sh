#!/bin/bash
#first down conf file
wget resource/conf/log.conf
rm -f /etc/logstash/conf.d/*
PKGName="logstash-1.5.0-1.noarch.rpm"
LogPath=`awk -F ':' 'NR==1{print $2}' log.conf`
RedisHost=`awk -F ':' 'NR==2{print $2}' log.conf`
LogKey1=`cat logcfg.txt |awk -F ':' 'NR==3{print $2}'|awk -F '.' '{print $1}'`
LogKey2=`cat logcfg.txt |awk -F ':' 'NR==4{print $2}'|awk -F '.' '{print $1}'`
ConFileName1=`awk -F ':' 'NR==3{print $2}' log.conf`
ConFileName2=`awk -F ':' 'NR==4{print $2}' log.conf`
##生成安装脚本
cat >LogCollection2ES.sh << SSS
#!/bin/bash

##install logstash
wget resource/package/$PKGName
rpm -ivh $PKGName


##configuration logstash
cd /etc/logstash/conf.d/
wget resource/conf/$ConFileName1
wget resource/conf/$ConFileName2
sed -i   's/ipaddr/$RedisHost/g' $ConFileName1
sed -i   's/key4log/$LogKey1/g' $ConFileName1
sed -i   's/ipaddr/$RedisHost/g' $ConFileName2
sed -i   's/key4log/$LogKey2/g' $ConFileName2
SSS

##chmod of the script
chmod u+x LogCollection2ES.sh


##execute the script
./LogCollection2ES.sh
##add logstash as a service
chkconfig --add logstash
chkconfig logstash on
##del rpm package
cd ~
rm -f $PKGName
