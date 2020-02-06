# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 20:27
# @Author  : DivingKitten
# @File    : views.py
# @Software: PyCharm
# @Desc    : 路由处理函数

from flask import render_template

from . import main
from .forms import NameForm


@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', )


@main.route('/hello', methods=['GET', 'POST'])
def hello():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html', form=form, name=name)
