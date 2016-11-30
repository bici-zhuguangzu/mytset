#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-29 23:39:10
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from celery import Celery
import requests

app = Celery('celery_blog',bloker='redis://192.168.10.117:6379/0')

@app.task
def fetch_url(url):  
     resp = requests.get(url)
     print(resp.status_code)

def func(urls):  
     for url in urls:
       fetch_url.delay(url)

if __name__ == "__main__":  
     func(["http://oneapm.com", "http://jd.com", "https://taobao.com", "http://baidu.com", "http://news.oneapm.com"])