# -*- coding: utf-8 -*-

from pytube import YouTube
from pytube import exceptions
from pprint import pprint
import os.path
import glob
import pandas as pd

from constant import PROJECT_ROOT, MOVIES_CSV_PATH
import colname

def download(youtube_id, save_dir, video_size='720p'):
    if os.path.exists(save_dir + youtube_id + 'mp4'):
        print('SKIP because the video was already downloaded.')
    else:
        url = "http://www.youtube.com/watch?v={0}".format(youtube_id)
        print('url', url)
        yt = YouTube(url)
        pprint(yt.get_videos())
        yt.set_filename(youtube_id)

        try:
            video = yt.get('mp4', video_size)
            print('download', youtube_id)
            video.download(save_dir)
            print('done.')

        except exceptions.DoesNotExist:
            video = yt.get('mp4')
            print('[exception] low res download', youtube_id)
            video.download(save_dir)
            print('done.')


def get_already_downloaded_list():
    lst = []
    path_list = glob.glob(PROJECT_ROOT + '/resources/youtube/*.mp4')
    for path in path_list:
        filename_without_ext = os.path.basename(path).split('.')[0]
        lst.append(filename_without_ext)
    return lst


if __name__ == '__main__':
    df = pd.read_csv(MOVIES_CSV_PATH)
    for i, row in df.iterrows():
        if not row[colname.is_downloaded]:
            movie_id = row[colname.movie_id]
            download(youtube_id=movie_id, save_dir='../../resources/youtube/')

            # update df
            df.loc[df.movie_id == movie_id, colname.is_downloaded] = True
    # save
    df.to_csv(MOVIES_CSV_PATH, index=False)