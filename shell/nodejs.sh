#!/bin/bash
path_now=`pwd`
pkgname=node-v0.12.4-linux-x64.tar.gz
dirname=node-v0.12.4-linux-x64
cd /home
wget resource/package/$pkgname
tar zxvf $pkgname
echo 'export PATH="/home/'$dirname'/bin:$PATH"' >> /etc/profile
source /etc/profile
rm -rf $pkgname
cd $path_now
node -v
