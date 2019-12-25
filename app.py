from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
#在wtf的模块中防止表单的跨站点攻击，设置一个验证加密串
app.config['SECRET_KEY'] = 'hardtoguess'
#调用bootstrap模块
bootstrap = Bootstrap(app)

#自定义表单的数据格式和预设内容
class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

#路由函数
@app.route('/')
def hello_world():
    return render_template('index.html')

#路由函数
@app.route('/hello', methods=['GET', 'POST'])
def hello2():
    # return 'hello my def %s' % name
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html', form=form, name=name)

#资源错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#服务器异常处理函数
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
