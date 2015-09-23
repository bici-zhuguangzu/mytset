#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-22 11:28:02
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$


import os
import datetime
import pyinotify
import logging


class MyEventHandler(pyinotify.ProcessEvent):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d]  \
                    %(levelname)s %(message)s',
                        datefmt='%a, %Y-%m-%d %H:%M:%S',
                        filename='../logs/executeResult.log',
                        filemode='a')
    logging.info("Starting monitor...")

    def process_IN_CLOSE_WRITE(self, event):
        # 下面为发现文件有变化执行的操作
        os.chdir('/home/dev/Service/expressSeivece')
        os.system('npm install --proxy http://10.172.6.233:8888')
        resultOfcommamd = os.popen('forever restart  \
            bin/www||forever start bin/www')
        logging.info("file updated : %s  %s" % (
            os.path.join(event.path, event.name), datetime.datetime.now()))
        logging.info(resultOfcommamd.read())


def main():
    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch(
        '/home/dev/Service/expressSeivece/README.md',  \
        pyinotify.ALL_EVENTS, rec=True)
    # /root/Service/expressSeivece/README.md是可以自己修改的监控的目录或文件
    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()
