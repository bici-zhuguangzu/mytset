#!/bin/bash
pkgname=mongodb-linux-x86_64-2.6.10.tgz
dirname=mongodb-linux-x86_64-2.6.10
cd /home
rm -f $pkgname
rm -rf $dirname
install(){
    wget resource/package/$pkgname
    tar zxvf $pkgname
    mv /home/$dirname/bin/* /usr/bin
    rm -f $pkgname
    rm -rf $dirname
}
conf(){
cat > /etc/init.d/mongodb <<EOF
#!/bin/bash
#
#chkconfig: 2345 80 90
#description: mongodb
start() {
 /usr/bin/mongod -f /etc/mongodb/bici.conf
}

stop() {
  /usr/bin/mongod -f /etc/mongodb/bici.conf --shutdown
}

case "\$1" in
  start)
 start
 ;;
  stop)
 stop
 ;;
  restart)
 stop
 start
 ;;
  *)
 echo $"Usage: service mongodb {start|stop|restart}"
 exit 1
esac
EOF
}
addOnboot(){
    chmod u+x /etc/init.d/mongodb
    mkdir -p /etc/mongodb
cat > /etc/mongodb/bici.conf <<EOF
#27017.conf
dbpath=/home/mongodb/data
logpath=/home/mongodb/log/mongodb.log
pidfilepath=/home/mongodb/mongodb.pid
directoryperdb=true
logappend=true
replSet=bici
bind_ip=`ifconfig eth0|grep inet|awk -F " " '{print $2}'|awk -F ":" '{print $2}'`
port=27017
oplogSize=1000
fork=true
noprealloc=true
EOF
    mkdir -p /home/mongodb/data
    mkdir -p /home/mongodb/log
    chkconfig --add mongodb
    chkconfig mongodb on
}
install
conf
addOnboot