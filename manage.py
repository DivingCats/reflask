# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 20:55
# @Author  : DivingKitten
# @File    : manage.py
# @Software: PyCharm
# @Desc    : 启动脚本

from app import create_app
from flask_script import Manager, Shell

app = create_app('default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    # app.run()
    manager.run()
