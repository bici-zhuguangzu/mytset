#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-14 15:05:48
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

d = {'before': 'c310113f6ffe7c34d29e9a82357db1c71c30497e', 'ref': 'refs/heads/master', 'object_kind': 'push', 'user_email': 'guangzu@staff.sina.com.cn', 'user_name': '朱光祖', 'message': None, 'commits': [{'id': '4d2de65a9f686f9802c19698de5997cb62b7d43f', 'author': {'name': '朱光祖', 'email': 'guangzu@staff.sina.com.cn'}, 'message': 'sorted return list\n\n', 'timestamp': '2017-04-14T13:19:46+08:00', 'url': 'http://gitlab/load-balance/lb-conf/commit/4d2de65a9f686f9802c19698de5997cb62b7d43f'}, {'id': 'dc8957bc95b1036b4ffa594a6b62cf209c0bdbc6', 'author': {'name': '朱光祖', 'email': 'guangzu@staff.sina.com.cn'}, 'message': 'add host get loginip\n\n', 'timestamp': '2017-04-14T10:45:21+08:00', 'url': 'http://gitlab/load-balance/lb-conf/commit/dc8957bc95b1036b4ffa594a6b62cf209c0bdbc6'}, {
    'id': 'c310113f6ffe7c34d29e9a82357db1c71c30497e', 'author': {'name': '朱光祖', 'email': 'guangzu@staff.sina.com.cn'}, 'message': 'add idc search   idc can get host\n\n', 'timestamp': '2017-04-13T16:51:34+08:00', 'url': 'http://gitlab/load-balance/lb-conf/commit/c310113f6ffe7c34d29e9a82357db1c71c30497e'}], 'project_id': 429, 'repository': {'visibility_level': 10, 'homepage': 'http://gitlab/load-balance/lb-conf', 'url': 'git@gitlab:load-balance/lb-conf.git', 'git_http_url': 'http://gitlab/load-balance/lb-conf.git', 'git_ssh_url': 'git@gitlab:load-balance/lb-conf.git', 'name': 'lb-conf', 'description': 'conf parse for load-balance'}, 'user_id': 297, 'checkout_sha': '4d2de65a9f686f9802c19698de5997cb62b7d43f', 'total_commits_count': 3, 'after': '4d2de65a9f686f9802c19698de5997cb62b7d43f'}


for i in d:
    print(i,d[i])