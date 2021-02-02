from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return f'Welcome, {name}!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    
    user = request.args.get('nm')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
