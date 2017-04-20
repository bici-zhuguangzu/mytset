#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-14 15:08:32
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from flask import Flask, jsonify, make_response, Response, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class test(Resource):
    """docstring for test"""
    def __init__(self):
        super(test, self).__init__()

    def post(self):
        body = request.get_json()
        for key in body:
            print(key,body[key])
            


api.add_resource(test, '/test', endpoint='test')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8004, debug=True)



