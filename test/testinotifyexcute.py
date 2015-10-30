#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-22 14:46:29
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

# Example: exclude items from being monitored.
#
import os
import pyinotify

wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm)

# Method 1:
# Exclude patterns from file
excl_file = os.path.join(os.getcwd(), 'exclude.lst')
excl = pyinotify.ExcludeFilter(excl_file)
# Add watches
res = wm.add_watch(['/etc/hostname', '/etc/cups', '/etc/rc0.d'],
                   pyinotify.ALL_EVENTS, rec=True, exclude_filter=excl)

# Method 2 (Equivalent)
# Exclude patterns from list
excl_lst = ['^/etc/apache[2]?/',
            '^/etc/rc.*',
            '^/etc/hostname',
            '^/etc/hosts',
            '^/etc/(fs|m)tab',
            '^/etc/cron\..*']
excl = pyinotify.ExcludeFilter(excl_lst)
# Add watches
res = wm.add_watch(['/etc/hostname', '/etc/cups', '/etc/rc0.d'],
                   pyinotify.ALL_EVENTS, rec=True, exclude_filter=excl)

# notifier.loop()
