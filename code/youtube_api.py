# https://github.com/youtube/api-samples/tree/master/python

from google_image_collector import get_api_key, get_cx


def get_video_info(video_id):
    api_key = get_api_key()
    cx = get_cx()

    print(api_key)
    print(cx)

if __name__ == '__main__':
    video_id = 'VA770wpLX-Q'
    info = get_video_info(video_id)
    print(info)