# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 15:29
# @Author  : DivingKitten
# @File    : views.py
# @Software: PyCharm
# @Desc    : restful路由函数

from . import api
from flask_restful import reqparse, Resource


# 删改查操作封装在一个类中
class rest(Resource):
    def get(self, rate):
        # parser = reqparse.RequestParser()
        # parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        # args = parser.parse_args()
        print(rate)
        return rate


# 增加和查询整个表封装在一个类中
class post(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=str, help='Rate to charge for this resource')
        args = parser.parse_args()
        task = {'task': args['rate']}
        # return 'oall', 201
        return task

api.add_resource(rest, '/rest/<string:rate>/')
api.add_resource(post, '/post')
