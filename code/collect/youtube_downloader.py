# -*- coding: utf-8 -*-

from pytube import YouTube
from pytube import exceptions
from pprint import pprint
import os.path


def download(youtube_id, save_dir):
    if os.path.exists(save_dir + youtube_id + 'mp4'):
        print('すでにあるのでスキップします')
    else:
        url = "http://www.youtube.com/watch?v={0}".format(youtube_id)
        print('url', url)
        yt = YouTube(url)
        yt.set_filename(youtube_id)
        try:
            video = yt.get('mp4', '720p')
            print('download', youtube_id)
            video.download(save_dir)
            print('done.')
        except exceptions.DoesNotExist:
            video = yt.get('mp4')
            print('低解像度 download', youtube_id)
            video.download(save_dir)
            print('done.')

if __name__ == '__main__':
    download(youtube_id, save_dir='../../resources/youtube/')