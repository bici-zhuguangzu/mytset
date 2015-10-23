#!/bin/bash
unset install
install(){
    #下载编译git需要的依赖包
    yum -y install curl-devel expat-devel gettext-devel \
    openssl-devel zlib-devel gcc
    wget https://www.kernel.org/pub/software/scm/git/git-2.4.5.tar.gz
    tar -zxvf git-2.4.5.tar.gz
    cd git-2.4.5
    make prefix=/usr/local all
    make prefix=/usr/local install
}
clone(){
    ＃克隆项目到本地 test
    cd /root
    git clone https://******:******@github.com/BiCiCare/ResourceCenter.git
}
install
clone