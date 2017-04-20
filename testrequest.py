#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-21 10:07:15
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from flask import Flask, jsonify, make_response, Response, request
from flask_restful import Api, Resource, reqparse
from flask_json import FlaskJSON, JsonError, json_response, as_json
from werkzeug.datastructures import Headers




class MyResponse(Response):

    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods',
                   'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        useragent = ("Access-Control-Allow-Headers",
                     "Origin, X-Requested-With, Content-Type, Accept, X-ID, X-TOKEN, X-ANY-YOUR-CUSTOM-HEADER")
        if headers:
            headers.add(*origin)
            headers.add(*methods)
            headers.add(*useragent)
        else:
            headers = Headers([origin, methods, useragent])
        kwargs['headers'] = headers
        return super().__init__(response, **kwargs)

app = Flask(__name__)
app.response_class = MyResponse
FlaskJSON(app)
api = Api(app)

class test(Resource):
    """docstring for test"""
    def __init__(self):
        super(test, self).__init__()

    def post(self):
        body = request.get_json()
        print(body)


api.add_resource(test, '/', endpoint='test')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


