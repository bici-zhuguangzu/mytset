#!/bin/bash
PKGName=elasticsearch-1.6.0.noarch.rpm

#Download package
wget resource/package/$PKGName

#Install package
rpm -ivh $PKGName


#add as a servie
chkconfig --add elasticsearch
chkconfig elasticsearch on

#configuration package

#delete package
rm -f $PKGName
