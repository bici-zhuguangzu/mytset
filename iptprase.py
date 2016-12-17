
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-13 11:38:49
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import os
import re
import json
import time


class Fileparse(object):
    """docstring for ClassName"""

    def __init__(self):
        # self.host_group = host_group
        self.filename = "iptables"
        self.iptPath = "/Users/zhuguangzu/Downloads/templates"
        self.erb_path = "index.html.erb"

    def get_host_group(self):
        host_groups = os.listdir(self.iptPath)
        return host_groups

    def get_all_flist(self):
        abs_path_list = []
        filelist = self.get_host_group()
        for group in filelist:
            abs_path = self.iptPath + "/" + group
            role = group.split(".")[0]
            if role != "ha" and role != "ssl" and os.path.isdir(abs_path):
                abs_path_list.append(abs_path + '/' + self.filename)
        return abs_path_list

    def get_ipt_flist(self):
        all_flist = self.get_all_flist()
        ipt_flist = []
        for file in all_flist:
            if os.path.isfile(file) and os.path.getsize(file) > 0:
                ipt_flist.append(file)
        return ipt_flist

    def ParseSigleFile(self, filename):
        lan_ip_re = r'\d+.\d+.\d+.\d+\/\d+'
        source_ip_re = r'\d+.\d+.\d+.\d+'
        _ipt_dict = {}
        _belong_dict = {}
        host_group = os.path.dirname(filename).split('/')[-1]
        with open(filename) as nf:
            lines = nf.readlines()
            nf.close
            for line in lines:
                snat_prog = re.search(r'SNAT', line)
                if snat_prog:
                    line_list = line.split()
                    for content in line_list:
                        if re.match(lan_ip_re, content):
                            lan_ip = content
                        if re.match(source_ip_re, content):
                            source_ip = content
                    _ipt_dict[lan_ip] = source_ip
                    _belong_dict[lan_ip] = host_group
                    # self.create_ERB(lan_ip, source_ip, host_group)
        return _ipt_dict, _belong_dict, host_group

    def ParseAllFile(self):
        host_group = ''
        _ipdict = {}
        _belong_dict = {}
        _alliptdict = {}
        _allbelong_dict = {}
        if os.path.exists(self.erb_path):
            os.remove(self.erb_path)
        ipt_flist = self.get_ipt_flist()
        for file in ipt_flist:
            _ipdict, _belong_dict, host_group = self.ParseSigleFile(file)
            _alliptdict.update(_ipdict)
            _allbelong_dict.update(_belong_dict)
        snatSourceJson = json.dumps({'allipblocksource': _alliptdict,'allipblockbelong':_allbelong_dict})
        snatFilename = 'snat.json'
        _f = open(snatFilename, 'w')
        _f.write(snatSourceJson)
        _f.close

    def create_ERB(self, lan_ip, source_ip, host_group):
        f = open(self.erb_path, 'a')
        if os.path.getsize == 0:
            f.write("lanip \t source_ip")
        content = "<p>%s sourceip %s</p>" % (lan_ip, source_ip)
        print(content)
        f.write(content)
        f.close


if __name__ == '__main__':
    test = Fileparse()
    # test.ParseSigleFile('/Users/zhuguangzu/Downloads/templates/lvsx.sg8.xd/iptables')
    test.ParseAllFile()
