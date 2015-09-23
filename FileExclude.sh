#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Date    : 2015-09-23 15:30:24
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

client1=192.168.12.203
client2=192.168.12.204
src=/home/test/
dst=lixuan
user=root
log_file=/var/log/inotifywait.log
inotify_exclude='(home/test/test)'
rsync_exclude='/etc/rsynced.d/rsync_exclude.lst'

inotifyAndRsync(){
    /usr/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format '%T %w%f%e' --exclude ${inotify_exclude} -e close_write $src | while read files
    do
        /usr/bin/rsync -auvrtzopgP --progress --exclude-from=${rsync_exclude} --password-file=/etc/client.pass $src $user@$client2::$dst
        /usr/bin/rsync -auvrtzopgP --progress --exclude-from=${rsync_exclude} --password-file=/etc/client.pass $src $user@$client1::$dst
    done
}


if [[ !-f "$log_file" ]]; then
    touch "$log_file"
fi

inotifyAndRsync >> ${log_file} 2>&1 &
