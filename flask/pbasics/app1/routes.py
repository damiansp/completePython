from flask import Flask#, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'You are at root'


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/product/<name>')
def get_product(name):
    return f'Voila! The product {name}'


@app.route('/sale/<transaction_id>')
def get_sale(transaction_id):
    return f'Transaction {transaction_id}'


@app.route('create/<name>/<surname>')
def create(name=None, surname=None):
    if name is None and surname is None:
        name = 'stranger'
    return f'Hello there, {name} {surname}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
