# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 20:50
# @Author  : DivingKitten
# @File    : forms.py
# @Software: PyCharm
# @Desc    : 表单对象

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# 自定义表单的数据格式和预设内容
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
