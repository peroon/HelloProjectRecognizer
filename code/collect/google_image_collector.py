# -*- coding: utf-8 -*-

"""Collect images using Search API"""

import urllib.parse
import urllib.request
import requests
import json

import data
from constant import PROJECT_ROOT


def get_image(search_word, save_directory, start_index=1):
    api_key = get_api_key()
    cx = get_cx()
    q = urllib.parse.quote(search_word)
    print('q', q)
    url = "https://www.googleapis.com/customsearch/v1?key={0}" \
          "&cx={1}" \
          "&q={2}" \
          "&start={3}" \
          "&searchType=image" \
          "&num=10".format(api_key, cx, q, start_index * 10 + 1)

    print(url)
    r = requests.get(url)
    json_obj = json.loads(r.text)
    for i, item in enumerate(json_obj['items']):
        image_id = 10 * (start_index - 1) + i
        image_id += 99000000 # google sign
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
    path = PROJECT_ROOT + "/secret/" + filename
    with open(path, 'r') as f:
        s = f.readline()
    return s


def get_api_key():
    return get_key('google_search_api_key')


def get_cx():
    return get_key('google_cx')


if __name__ == '__main__':
    idol = data.get_tsubaki_list()[-3]

    # Only the top 100 search results can be acquired
    for i in range(0, 10):
        print(i, idol.name, idol.directory_name)
        get_image(idol.name, '../../resources/search_google/{0}/'.format(idol.directory_name), start_index=i)
