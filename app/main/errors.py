# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 20:19
# @Author  : DivingKitten
# @File    : errors.py
# @Software: PyCharm
# @Desc    : 错误路由处理文件

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500'), 500
