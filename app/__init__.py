# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 16:46
# @Author  : DivingKitten
# @File    : __init__.py
# @Software: PyCharm
# @Desc    : Web程序构造文件，包含工厂函数，方便动态修改配置

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_restful import Api, Resource
from config import config

from .main import main as main_bluepoint
from .api import api_bp as api_bluepoint

bootstrap = Bootstrap()
# api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    # Api.init_app(app)

    # 注册蓝本
    app.register_blueprint(main_bluepoint)
    app.register_blueprint(api_bluepoint)

    return app
