#!/usr/bin/env python
#coding = utf-8
import os
import pyinotify
import sys

FileNmae = sys.argv[1]


class OnWriteHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):  # 函数名以"process_"开头,后面跟注册的监测类型
        os.system('echo ' + 'create file:%s' %
                  (os.path.join(event.path, event.name)))  # 之后用于nohup输出
        print "create file: %s " % os.path.join(event.path, event.name)  # 打印


def auto_compile(path='.'):
    wm = pyinotify.WatchManager()
    # 监测类型，如果多种用|分开，pyinotify.IN_CREATE | pyinotify.IN_DELETE
    mask = pyinotify.IN_CREATE
    notifier = pyinotify.Notifier(wm, OnWriteHandler())
    wm.add_watch(path, mask, rec=True, auto_add=True)
    print '==&gt; Start monitoring %s (type c^c to exit)' % path
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break

if __name__ == "__main__":
    auto_compile()
