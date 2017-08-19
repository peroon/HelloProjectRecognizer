import glob
import os

from constant import RESOURCES_ROOT


def youtube_id_to_path(youtube_id):
    return RESOURCES_ROOT + '/youtube/' + youtube_id + '.mp4'


def path_to_youtube_id(path):
    base = os.path.basename(path)
    return os.path.splitext(base)[0]


def get_youtube_id_list():
    path_list = glob.glob(RESOURCES_ROOT + '/youtube/*.mp4')
    id_list = []
    for path in path_list:
        id_list.append(path_to_youtube_id(path))
    id_list.sort()
    return id_list
