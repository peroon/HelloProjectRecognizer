# https://github.com/youtube/api-samples/tree/master/python

import requests
import json
import pprint

import google_api

def get_video_info(video_id):
    api_key = google_api.get_api_key()
    url = 'https://www.googleapis.com/youtube/v3/videos?id=' + video_id + '&key=' + api_key + \
          '&fields=items(id,snippet(title,publishedAt))&part=snippet,contentDetails,statistics'
    r = requests.get(url)
    json_obj = json.loads(r.text)
    for i, item in enumerate(json_obj['items']):
        pprint.pprint(item)
        id = item['id']
        published_at = item['snippet']['publishedAt']
        title = item['snippet']['title']
        print(id, published_at, title)


if __name__ == '__main__':
    video_id = '0EwG_EJ7Aaw'
    info = get_video_info(video_id)
    print(info)