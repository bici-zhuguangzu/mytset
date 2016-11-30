#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-29 23:39:10
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import requests
from celery_config import app
@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)
def func(urls):
    for url in urls:
        fetch_url.delay(url)
if __name__ == "__main__":
    func(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
