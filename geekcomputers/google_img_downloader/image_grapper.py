import json
from os import chdir, system, walk
from os.path import curdir, pardir
import ssl
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import requests

from create_dir import create_dir


ssl._create_default_https_context = ssl._create_unverified_context


GOOGLE_IMAGE = (
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&')
WALLPAPERS_KRAFT = 'https://wallpaperscraft.com/search/keywords?'
usr_agent = {
    'User-Agent':(
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 '
        '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
    'Accept': (
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
FX = {
    1: "search_for_image",
    2: "download_wallpapers_1080p",
    3: "view_images_directory",
    4: "set_directory",
    5: "quit"}


def main():
    run = True


if __name__ == '__main__':
    main()
