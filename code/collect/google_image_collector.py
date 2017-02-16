# -*- coding: utf-8 -*-

"""Search APIで画像を集める"""

import urllib.parse
import urllib.request

def get_image(search_word, save_directory):
    api_key = get_api_key()
    cx = get_cx()
    q = urllib.parse.quote(search_word)
    url = "https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&q={2}&hl=ja&start=1&num=10".format(api_key, cx, q)
    print(url)
    #f = request.urlopen(url)
    #print(f.read())
    pass


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
    print(get_cx())
    get_image('矢島舞美', '')