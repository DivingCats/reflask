# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 16:46
# @Author  : DivingKitten
# @File    : __init__.py
# @Software: PyCharm
# @Desc    : Web程序构造文件，包含工厂函数，方便动态修改配置

from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from flask_neo4j import Neo4j

bootstrap = Bootstrap()
neo4j = Neo4j()
# api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    neo4j.init_app(app)
    # Api.init_app(app)

    # 注册蓝本
    from .main import main as main_bluepoint
    from .api import api_bp as api_bluepoint

    app.register_blueprint(main_bluepoint)
    app.register_blueprint(api_bluepoint)

    return app
