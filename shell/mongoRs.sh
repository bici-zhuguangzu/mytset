#!/bin/bash

#提取服务器ip
mongodbip=`awk -F: 'NR==2{print $3}' rscfg.conf`
#echo $ip
yum=`which yum`
#安装python－pymongo模块
$yum -y install python-pymongo 

#生成python脚本
cat << EOF > /root/mongoRs.py
#!/usr/bin/env python
from pymongo import MongoClient

conn = MongoClient($ip',27017)
config = `cat rscfg.conf`
conn.admin.command("replSetInitiate", config)
EOF

##给脚本加执行权限
chmod u+x /root/mongoRs.py
python /root/mongoRs.py
