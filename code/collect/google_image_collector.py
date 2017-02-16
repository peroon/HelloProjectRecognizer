# -*- coding: utf-8 -*-

"""Search APIで画像を集める"""

import urllib.parse
import urllib.request
import requests
import json
import pprint
import os.path
from PIL import Image


def get_image(search_word, save_directory, start_index=1):
    api_key = get_api_key()
    cx = get_cx()
    q = urllib.parse.quote(search_word)
    url = "https://www.googleapis.com/customsearch/v1?key={0}" \
          "&cx={1}" \
          "&q={2}" \
          "&hl=ja" \
          "&start={3}" \
          "&searchType=image" \
          "&num=10".format(api_key, cx, q, start_index)
    print(url)
    r = requests.get(url)
    json_obj = json.loads(r.text)
    for i, item in enumerate(json_obj['items']):
        image_id = 10 * (start_index - 1) + i
        image_url = item['link']
        download_image(image_url, save_directory, image_id)
    pass


def download_image(url, save_dir, image_id):
    print('download', image_id, url)
    ext = url[-4:]
    if ext == '.jpg' or ext == '.png':
        # download and save
        filename = '%04d' % image_id + ext
        try:
            urllib.request.urlretrieve(url, save_dir + filename)
        except urllib.error.HTTPError:
            print('DL error. so skip')
    else:
        print('skip')


def get_key(filename):
    path = r"C:\Users\kt\Documents\github_projects\HelloProjectRecognizer\secret\\" + filename
    with open(path, 'r') as f:
        s = f.readline()
    return s


def get_api_key():
    return get_key('google_search_api_key')


def get_cx():
    return get_key('google_cx')


if __name__ == '__main__':
    get_image('矢島舞美', r'C:\Users\kt\Documents\github_projects\HelloProjectRecognizer\resources\search\maimi-yajima\\')