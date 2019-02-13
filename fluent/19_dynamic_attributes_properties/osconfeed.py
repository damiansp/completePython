import json
import os
import warnings
from urllib.request import urlopen

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = '../data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = f'Downloading {URL} to {JSON}'
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
        with open(JSON) as fp:
            return json.load(fp)

feed = load()
print(sorted(feed['Schedule'].keys()))
for k, v in sorted(feed['Schedule'].items()):
    print(f'{len(v):3} {k}')
print(feed['Schedule']['speakers'][-1]['name'])
print(feed['Schedule']['speakers'][-1]['serial'])
print(feed['Schedule']['events'][40]['name'])
print(feed['Schedule']['events'][40]['speakers'])
          
        
