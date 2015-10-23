#!/bin/bash
path_now=`pwd`
packagename=kibana-4.0.2-linux-x64.tar.gz
dirname=kibana-4.0.2-linux-x64
download(){
wget resource/package/$packagename
tar zxvf $packagename
}
chgstartype(){
	echo > /$path_now/dirname/bin/kibana <<EOF
#!/bin/sh
SCRIPT=\$0

# SCRIPT may be an arbitrarily deep series of symlinks. Loop until we have the concrete path.
while [ -h "\$SCRIPT" ] ; do
  ls=$(ls -ld "\$SCRIPT")
  # Drop everything prior to ->
  link=\$(expr "\$ls" : '.*-> \(.*\)$')
  if expr "\$link" : '/.*' > /dev/null; then
    SCRIPT="\$link"
  else
    SCRIPT=$(dirname "\$SCRIPT")/"$link"
  fi
done

DIR=/root/kibana
NODE=\${DIR}/node/bin/node
SERVER=\${DIR}/src/bin/kibana.js

CONFIG_PATH="\${DIR}/config/kibana.yml" NODE_ENV="production"
start()
{
CONFIG_PATH="\${DIR}/config/kibana.yml" NODE_ENV="production" \
exec forever start \${SERVER} >>/var/log/kinaba.log
}

stop()
{
CONFIG_PATH="${DIR}/config/kibana.yml" NODE_ENV="production" \
exec forever stop \${SERVER} >>/var/log/kinaba.log
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
esac 
}
EOF
startonreboot(){
	echo  /$path_now/$dirname/bin/kibana start >> /etc/rc.local
}


download
chgstartype
startonreboot
/$path_now/$dirname/bin/kibana start
