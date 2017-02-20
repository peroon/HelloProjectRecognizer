# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
import requests
import json
import pprint
import os.path
from PIL import Image

import secret
import data


def get_image(search_word, save_directory, start_index=1):
    offset = start_index * 35
    q = urllib.parse.quote(search_word)
    url = "https://api.cognitive.microsoft.com/bing/v5.0/images/search?q={0}&offset={1}".format(q, offset)
    print(url)
    headers = {'Ocp-Apim-Subscription-Key': get_api_key()}
    r = requests.get(url, headers=headers)
    print(r.text)
    json_obj = json.loads(r.text)
    pprint.pprint(json_obj)
    for i, value in enumerate(json_obj['value']):
        image_url = value['contentUrl']
        print(image_url)
        image_id = start_index * 10000 + i
        download_image(image_url, save_directory, image_id=image_id)


def download_image(url="", save_dir="", image_id=1):
    print('download', image_id, url)
    if url.find('.jpg') != -1 or url.find('.jpeg') != -1:
        ext = '.jpg'
    elif url.find('.png') != -1:
        ext = '.png'
    else:
        ext = None

    if ext == '.jpg' or ext == '.png':
        # download and save
        filename = '%08d' % image_id + ext
        try:
            urllib.request.urlretrieve(url, save_dir + filename)
        except urllib.error.HTTPError:
            print('DL error. so skip')
    else:
        print('skip')


def get_api_key():
    return secret.get_key('bing_api_key')

if __name__ == '__main__':
    cute_list = data.get_cute_list()
    cute_list = cute_list[1:]

    for idol in cute_list:
        print(idol.name)
        for i in range(0, 20):
            get_image(idol.name, '..\\..\\resources\\search\\{0}\\'.format(idol.directory_name), start_index=i)
