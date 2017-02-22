# -*- coding: utf-8 -*-

from pytube import YouTube
from pprint import pprint


def download(youtube_id, save_dir):
    url = "http://www.youtube.com/watch?v={0}".format(youtube_id)
    yt = YouTube(url)
    yt.set_filename(youtube_id)
    video = yt.get('mp4', '720p')
    print('download', youtube_id)
    video.download(save_dir)
    print('done.')

if __name__ == '__main__':
    download('8H1Ex9voW64', save_dir='../../resources/youtube/')