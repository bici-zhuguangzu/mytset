#!/bin/bash
#down conf file
#
PKGName="logstash-1.5.0-1.noarch.rpm"
LogPath=`awk -F ':' 'NR==1{print $2}' log2.conf`
RedisHost=`awk -F ':' 'NR==2{print $2}' log2.conf`

#Create install script
cat >LogCollection2Redis.sh << SSS
#!/bin/bash

#install logstash
wget resource/package/$PKGName
rpm -ivh $PKGName


##configuration logstash
cat >/etc/logstash/conf.d/shipper.conf << EOF
input {
        file {
                path => "$LogPath"
                start_position => "end"
      }
}
output {
        redis {
                host => "$RedisHost"
                data_type => "list"
                key => "logkey"

        }
}
EOF
SSS

##chmod of the script
chmod u+x Collection2Redis.sh


##execute the script
./Collection2Redis.sh
##add logstash as a service
chkconfig --add logstash
chkconfig logstash on
##del rpm package
rm -f $PKGName
