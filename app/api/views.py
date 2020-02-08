# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 15:29
# @Author  : DivingKitten
# @File    : views.py
# @Software: PyCharm
# @Desc    : restful路由函数，包含swagger

from . import api
from flask_restplus import reqparse, Resource, fields
from .. import neo4j

api = api.namespace('TestAPI', discription='Test operation')

model = api.model('string', {
    'rate': fields.String(require=True, descripiton="测试用字符串")
})


# 删改查操作封装在一个类中
@api.route('/rest/<int:rate>')
@api.param('rate', '测试用整型字段')
class Rest(Resource):
    @api.doc('查询一个')
    @api.response(201, 'Found')
    def get(self, rate):
        # for rel in graph.match((person,), r_type="Person"):
        #     print(rel.end_node["name"])
        g=neo4j.gdb.run("MATCH (n:Person) RETURN n LIMIT 5")
        for i in g:
            print(g.data())
        return rate

    @api.doc('删除一个')
    @api.response(204, 'delete complete')
    def delete(self, rate):
        return rate, 204


# 增加和查询整个表封装在一个类中
@api.route('/post')
class Post(Resource):
    @api.doc('create string')
    # @api.marshal_with(model, code=201)
    @api.expect(model)
    def post(self):
        """新建信息"""
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=str, help='Rate to charge for this resource')
        args = parser.parse_args()
        task = {'task': args['rate']}
        return task, 201
