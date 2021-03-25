from flask import Flask, redirect, request, session, url_for
from markupsafe import escape


app = Flask(__name__)


app.secret_key = load_my_secret(KEYS_PATH)


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {escape(session["username"])}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type="text" name="username"></p>
            <p><input type="submit" value="Login"></p>
        </form>'''


@app.route('/logout')
def logout():
    # remove username from sess if present
    session.pop('username', None)
    return redirect(url_for('index'))
