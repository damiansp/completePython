import this

from flask import Flask


app = Flask(__name__)
rot13 = str.maketrans(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM')
tr = str.maketrans(
    'aeiouwyAEIOUWYbcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ',
    'iouaeywIOUAEYWpxtvkjhgmnrbxlzdfqsPXTVKJHGMNRBXLZDFQS')


def simple_html(body):
    return (
        f'''
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8" />
            <title>Some Example</title>
          </head>
          <body>{body}</body>
        </html>''')


@app.route('/')
def hello():
    return simple_html('<a href=/zen>Python Zen</a>')


@app.route('/zen')
def zen():
    return simple_html(
        '<br />'.join(this.s.translate(rot13).translate(tr).split('\n')))


if __name__ == '__main__':
    app.run()
