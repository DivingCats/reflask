# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 15:28
# @Author  : DivingKitten
# @File    : __init__.py
# @Software: PyCharm
# @Desc    : restful_api蓝本初始化

from flask import Blueprint
from flask_restplus import Api

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp, version='0.1', title='TEST API', description='There are many APIs')

from . import views

# from .. import neo4j