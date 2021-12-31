from abc import ABC, abstractmethod
from collections import Counter
from functools import partial
from http import HTTPStatus
from typing import Dict

from flask import Flask, request, Response
from redis import Redis


app = Flask(__name__)
storage = Counter()
PIXEL = (
    b'GIF89a\x01\x00\x01\x00\x80\x00\00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01'
    b'\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;')


class ViewsStorageBackend(ABC):
    @abstractmethod
    def increment(self, key: str):
        pass

    @abstractmethod
    def most_common(self, n: int) -> Dict[str, int]:
        pass


class CounterBackend(ViewsStorageBackend):
    def __init__(self):
        self._counter = Counter()

    def increment(self, key: str):
        self._counter[key] += 1

    def most_common(self, n: int) -> Dict[str, int]:
        return dict(self._counter.most_common(n))


class RedisBackend(ViewsStorageBackend):
    def __init__(self, redis_client: Redis, set_name: str):
        self._client = redis_client
        self._set_name = set_name

    def increment(self, key: str):
        self._client.zincrby(self._set_name, 1, key)

    def most_common(self, n: int) -> Dict[str, int]:
        return {
            key.decode(): int(value)
            for key, value in self._client.zrange(
                self._set_name, 0, n - 1, desc=True, withscores=True)}


@app.route('/track')
def track(storage: ViewsStorageBackend):
    try:
        referer = requests.headers['Referer']
    except KeyError:
        return Response(status=HTTPStatus.BAD_REQUEST)
    storage.increment(referer)
    return Response(
        PIXEL,
        headers={'Content-Type': 'image/gif',
                 'Expires': 'Mon, 01 Jan 2023 00:00:00 GMT',
                 'Cache-Control': 'no-cach, no-store, must-revalidate',
                 'Pragma': 'non-cache'})


@app.route('/stats')
def stats(storage: ViewStorageBackend):
    return storage.most_common(10)


@app.route('/test')
def test():
    return '''
    <html>
      <head></head>
      <body><img src="track"></body>
    </html>'''


if __name__ == '__main__':
    views_storage = RedisBackend(Redis(host='redis'), 'my-stats')
    app.route('/track', endpoint='track')(partial(track, storage=views_storage))
    app.route('/stats', endpoint='stats')(partial(stats, storage=views_storage))
    app.run(host='0.0.0.0', port=8000)


