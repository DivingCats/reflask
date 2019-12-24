from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello2(name):
    # return 'hello my def %s' % name
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
