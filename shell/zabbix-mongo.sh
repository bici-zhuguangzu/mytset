#!/bin/bash
#escrpition:this script will create zabbix User parameters for mongodb
#get wan of this server
ip=`ifconfig eth0|grep Bcast|awk -F: '{print $2}'|awk -F " " '{print $1}'`
#echo $ip
#create userparameter for mongodb
cat >> /etc/zabbix/zabbix_agentd.d/userparameter_mysql.conf <<EOF
UserParameter=mongo.mem_resident,echo "db.serverStatus().mem"| mongo -host $ip admin|grep resident | cut -d ":" -f 2 |cut -d "," -f 1| cut -d " " -f 2
UserParameter=mongo.mem_virtual,echo "db.serverStatus().mem"| mongo -host $ip admin|grep virtual | cut -d ":" -f 2 |cut -d "," -f 1| cut -d " " -f 2
UserParameter=mongo.mem_mapped,echo "db.serverStatus().mem"| mongo -host $ip admin|grep '\bmapped\b' | cut -d ":" -f 2 |cut -d "," -f 1| cut -d " " -f 2
UserParameter=mongo.network[*],echo "db.serverStatus().network"|mongo -host $ip admin  | grep $1 | cut -d ":" -f 2 |cut -d "," -f1 |cut -d " " -f 2
UserParameter=mongo.index[*],echo "db.serverStatus().indexCounters"|mongo -host $ip admin | grep $1| cut -d ":" -f 2 |cut -d "," -f1 |cut -d " " -f 2
UserParameter=mongo.connection_current,echo "db.serverStatus().connections"| mongo -host $ip admin| grep current|cut -d ":" -f 2|cut -d "," -f 1|cut -d " " -f 2
UserParameter=mongo.connection_available,echo "db.serverStatus().connections"| mongo -host $ip admin| grep current| cut -d ":" -f 3|cut -d "," -f 1 |cut -d " " -f 2
UserParameter=mongo.opcounters[*],echo "db.serverStatus().opcounters" |mongo -host $ip admin | grep $1|cut -d ":" -f 2|cut -d "," -f 1 |cut -d " " -f 2
UserParameter=mongo.rpstatus,echo "rs.status()"| mongo -host $ip admin | grep myState| cut -d ":" -f 2| cut -d "," -f 1 |cut -d " " -f 2
UserParameter=mongo.queue_write,echo "db.serverStatus().globalLock.currentQueue.writers"|mongo -host $ip admin |sed -n 3p
UserParameter=mongo.queue_reader,echo "db.serverStatus().globalLock.currentQueue.readers"|mongo -host $ip admin |sed -n 3p
UserParameter=mongo.backgroundFlush,echo "db.serverStatus().backgroundFlushing.last_ms" |mongo -host $ip admin |sed -n 3p
UserParameter=mongo.curosor_Totalopen,echo "db.serverStatus().cursors.totalOpen" |mongo -host $ip admin |sed -n 3p
UserParameter=mongo.curospr_timedOu,echo "db.serverStatus().cursors.timedOut" |mongo -host $ip admin |sed -n 3p
UserParameter=mongo.pagefaults,echo "db.serverStatus().extra_info.page_faults" |mongo -host $ip admin|sed -n 3p
UserParameter=mongo.oplog_storetime,echo "db.printReplicationInfo()"|mongo -host $ip admin|sed -n 4p|cut -d "(" -f 2|cut -d "h" -f
EOF