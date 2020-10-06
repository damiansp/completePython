from flask import abort
from flask import Flask
from flask import make_response
from flask import redirect


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'


@app.route('/set_cookie')
def set_cookie():
    resp = make_response('<h1>This page sets a cookie!</h1>')
    resp.set_cookie('answer', '42')
    return resp


@app.route('/redirect')
def redirect():
    return redirect('http://www.example.com')


@app.route('/login/<init>')
def validate_user(init):
    known = {'d': 'damian', 'a': 'abner'}
    user = known.get(init, None)
    if user is None:
        abort(404)
    return f'<h1>Hello, {user}</h1>'
