# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 15:28
# @Author  : DivingKitten
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    : restful_api蓝本初始化

from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp)

from . import views
