# -*- coding: utf-8 -*-

"""Get YouTube info e.g. Title, etc"""

# https://github.com/youtube/api-samples/tree/master/python

import requests
import json
import dateutil.parser
import codecs

import google_api
import constant

cache_path = constant.PROJECT_ROOT + '/data/json/youtube_info_cache.json'


class VideoInfo:
    def __init__(self, id, title, published_at):
        self.id = id
        self.title = title
        self.published_at = published_at

    def __str__(self):
        return self.id + ' ' + self.title + ' ' + self.published_at

    def __repr__(self):
        return self.__str__()

    def published_at_simple(self):
        date = dateutil.parser.parse(self.published_at)
        return date.strftime('%Y/%m/%d')


def __get_cache_dict():
    f = open(cache_path, 'r', encoding='utf-8')
    dict = json.load(f)
    f.close()
    return dict


def __get_video_info_from_cache(video_id):
    dict = __get_cache_dict()

    if video_id in dict:
        title = dict[video_id][0]
        created_at = dict[video_id][1]
        return VideoInfo(video_id, title, created_at)
    else:
        return None


def __add_to_cache(video_info):
    """
    :param VideoInfo video_info:
    :return:
    """
    dict = __get_cache_dict()
    dict[video_info.id] = [video_info.title, video_info.published_at_simple()]
    # save
    with codecs.open(cache_path, 'w', 'utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


def get_video_info(video_id):

    # search in cache
    cached_video_info = __get_video_info_from_cache(video_id)
    if cached_video_info:
        print('cache hit')
        return cached_video_info
    else:
        api_key = google_api.get_api_key()
        url = 'https://www.googleapis.com/youtube/v3/videos?id=' + video_id + '&key=' + api_key + \
              '&fields=items(id,snippet(title,publishedAt))&part=snippet,contentDetails,statistics'
        r = requests.get(url)
        json_obj = json.loads(r.text)
        print(video_id, json_obj)
        item = json_obj['items'][0]
        id = item['id']
        title = item['snippet']['title']
        published_at = item['snippet']['publishedAt']
        video_info = VideoInfo(id, title, published_at)
        __add_to_cache(video_info)
        return video_info


if __name__ == '__main__':
    video_id = '4eDwWQindJo'
    #info = get_video_info(video_id)
    #print(info)

    video_info = get_video_info(video_id)
    print(video_info)
