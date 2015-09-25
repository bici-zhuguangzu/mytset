#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-22 14:52:52
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import os
import datetime
import pyinotify
import logging
import time

# 指定监控的文件夹路径
DirName = '/home/dev/Service/expressSeivece/'


class MyEventHandler(pyinotify.ProcessEvent):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d]  \
    %(levelname)s %(message)s',
                        datefmt='%a, %Y-%m-%d %H:%M:%S',
                        filename='var/log/monitorexpress.log',
                        filemode='a')
    logging.info("Starting monitor...")

    def process_IN_CLOSE_WRITE(self, event):
        # 下面为发现文件有变化执行的操作
        os.chdir(DirName)
        time.sleep(30)
        os.system('npm install --proxy http://******:8888')
        message = os.popen('forever restart bin/www||forever start bin/www')
        logging.info("file updated : %s  %s" % (
            os.path.join(event.path, event.name), datetime.datetime.now()))
        logging.debug(message.read())


def main():
    # watch manager
    wm = pyinotify.WatchManager()
    excl_lst = ['^/home/dev/Service/expressSeivece/log/*.log']
    excl = pyinotify.ExcludeFilter(excl_lst)
    wm.add_watch(
        DirName, pyinotify.ALL_EVENTS,
        rec=True, exclude_filter=excl)
    # event handler
    eh = MyEventHandler()
    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()


if __name__ == '__main__':
    main()
