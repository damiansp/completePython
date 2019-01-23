'''Download 20 flag images sequentially (synchronous) for baseline comparison'''
import os
import sys
import time

import requests


POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR')\
           .split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'images'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as f:
        f.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    if resp.status_code != 200:
        reps.raise_for_status()
    return resp.content


def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(base_url, cc)
    except requests.exceptions.HTTPError as e:
        res = e.response
        if res.status_code == 404:
            status = HTTPStatus.not_found
            msg = 'not found'
        else:
            raise
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
    if verbose:
        print(cc, msg)
    return Result(status, cc)


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_all(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')
    return len(cc_list)


# pass download_all to main so main can be used as lib func with other
# implementations for downloading
def main(download_all):
    t0 = time.time()
    count = download_all(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


    
if __name__ == '__main__':
    main(download_all)
