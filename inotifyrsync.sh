#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Date    : 2015-09-23 15:30:24
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

client1=
client2=
src=/home/dev/Service
dst=bicicode
user=root
log_file=/var/log/inotifywait.log
inotify_exclude='/etc/inotifywait_exclude.lst'
rsync_exclude='/etc/rsyncd.d/rsync_excude.lst'


CreateExcludeFile(){
cat <<EOF > /etc/inotifywait_exclude.lst
@/home/dev/Service/odataSeivece/logs
@/home/dev/Service/odataSeivece/images
@/home/dev/Service/odataSeivece/node_modules
@/home/dev/Service/expressSeivece/node_modules
EOF
    mkdir -p /etc/rsyncd.d
cat <<SSS > /etc/rsynced.d/rsync_excude.lst
odataSeivece/logs/
odataSeivece/images/
odataSeivece/node_modules/
expressSeivece/node_modules/
SSS
}

inotifyAndRsync(){
    /usr/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format '%T %w%f%e'  \
    -fromfile=${inotify_exclude}  -e close_write $src | while read files
    do
        /usr/bin/rsync -auvrtzopgP --progress --exclude-from=${rsync_exclude} --password-file=/etc/client.pass $src $user@$client2::$dst
        /usr/bin/rsync -auvrtzopgP --progress --exclude-from=${rsync_exclude} --password-file=/etc/client.pass $src $user@$client1::$dst
    done
}

if [ ! -f "$log_file" ]; then
    touch "$log_file"
fi

if [[ c! -f "$inotify_exclude" ]]; then
    CreateExcludeFile
fi

inotifyAndRsync >> ${log_file} 2>&1 &
