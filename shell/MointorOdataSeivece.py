#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用前安装 pyinotify
# pip install pyinotify
# 如果没有pip 安装pip
# yum install python-pip
import os
import datetime
import pyinotify
import logging


class MyEventHandler(pyinotify.ProcessEvent):
    logging.basicConfig(level=logging.INFO, filename='/var/log/monitor.log')
    logging.info("Starting monitor...")

    def process_IN_CLOSE_WRITE(self, event):
        # 下面为发现文件有变化执行的操作
        os.chdir('/home/dev/Service/odataSeivece')
        os.system('npm install --proxy http://10.172.6.233:8888')
        os.system('forever restart index.js||forever start index.js')
        logging.info("file updated : %s  %s" % (
            os.path.join(event.path, event.name), datetime.datetime.now()))


def main():
    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch(
        '/home/dev/Service/odataSeivece/README.md', pyinotify.ALL_EVENTS, rec=True)
    # /home/dev/Service/odataSeivece/README.md是可以自己修改的监控的目录或文件
    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()
