# To execute
# > export FLASK_APP=app.py
# > flask run 
from flask import (
    Flask, jsonify, make_response, redirect, render_template, request, url_for)
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    # Get cookie
    username = request.cookies.get('username', None)
    # ...
    # set cookie:
    resp = make_response(render_template('...'))
    resp.set_cookie('username', 'the username')
    return resp


@app.route('/oldpage')
def redirect_example():
    return redirct(url_for('newpage'))


@app.route('/abort')
def abort_example():
    abort(401)
    unreachable_call()
    

@app.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if is_valid_login(request.form['username'], request.form['password']):
            return log_user_in(request.form['username'])
        error = 'Invalid username/password'
    # GET or bad POST
    return render_template('login.html', error=error) 


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        #f.save('/var/www/uploads/uploaded_file.txt') # or
        f.save('/var/www/uploads/' + secure_filename(f.filename))
    # ...
    

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


# APIs with JSON
@app.route('/me')
def me_api():
    user = get_current_user()
    return {'username': user.username,
            'theme': user.theme,
            'image': url_for('user_image', filename=user.image)}

@app.route('/users')
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='Bob Dobolina'))
