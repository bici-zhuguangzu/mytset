#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-08 19:47:29
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import sys
import Queue
import threading
import time


class _Thread(threading.Thread):

    def __init__(self, workQueue, resultQueue, timeout=1, **kwargs):
        threading.Thread.__init__(self, kwargs=kwargs)
        self.timeout = timeout
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue
#       self.start()

    def run(self):
        while True:
            try:
                callable, args, kwargs = self.workQueue.get(
                    timeout=self.timeout)
                res = callable(args, kwargs)
                print res, " | " + self.getName()
                self.resultQueue.put(res + " | " + self.getName())
            except Queue.Empty:
                break
            except:
                print sys.exc_info()
                raise


class ThreadPool:

    def __init__(self, num_of_threads=2):
        self.workQueue = Queue.Queue()  # work queue func args
        self.resultQueue = Queue.Queue()  # resulst queue
        self.threads = []  # threadlist
        self.__createThreadPool(num_of_threads)

    def __createThreadPool(self, num_of_threads):
        for i in range(num_of_threads):
            thread = _Thread(self.workQueue, self.resultQueue)
            self.threads.append(thread)

    def wait_for_complete(self):
        while len(self.threads):
            thread = self.threads.pop()
            if thread.isAlive():
                thread.join()

    def start(self):
        for th in self.threads:
            th.start()

    def add_job(self, callable, *args, **kwargs):
        self.workQueue.put((callable, args, kwargs))  # put msg


def test_job(id, sleep=0.001):
    time.sleep(0.1)
    return str(id)


def test():
    print 'start testing'
    tp = ThreadPool(5)
    for i in range(50):
        tp.add_job(test_job, i, i)
    tp.start()
    tp.wait_for_complete()

    print 'result Queue\'s length == %d ' % tp.resultQueue.qsize()

    while tp.resultQueue.qsize():
        print tp.resultQueue.get()
    print 'end testing'

if __name__ == '__main__':
    test()
