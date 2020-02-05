# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 16:35
# @Author  : DivingKitten
# @File    : config.py
# @Software: PyCharm
# @Desc    : 不同环境下的程序配置

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hardtoguess'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
