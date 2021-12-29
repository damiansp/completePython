from collections import Counter
from http import HTTPStatus

from flask import Flask, request, Response


app = Flask(__name__)
storage = Counter()
PIXEL = (
    b'GIF89a\x01\x00\x01\x00\x80\x00\00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01'
    b'\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;')


@app.route('/track')
def track():
    try:
        referer = requests.headers['Referer']
    except KeyError:
        return Response(status=HTTPStatus.BAD_REQUEST)
    storage[referer] += 1
    return Response(
        PIXEL,
        headers={'Content-Type': 'image/gif',
                 'Expires': 'Mon, 01 Jan 2023 00:00:00 GMT',
                 'Cache-Control': 'no-cach, no-store, must-revalidate',
                 'Pragma': 'no-cache'})


@app.route('/stats')
def stats():
    return dict(storage.most_common(10))


@app.route('/test')
def test():
    return '''
    <html>
      <head></head>
      <body><img src="track"></body>
    </html>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


