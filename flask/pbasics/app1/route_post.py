from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route('/dashboard/<name>')
def dashboard(name):
    return f'Welcome, {name}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('dashboard', name=user))

    #user = request.args.get('name') # line seems pointless
    return render_template('login.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
