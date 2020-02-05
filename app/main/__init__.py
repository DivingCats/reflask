# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 16:44
# @Author  : DivingKitten
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    : 主蓝本初始化

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
