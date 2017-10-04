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


def get_a_unlabeled_youtube_id():
    id_list = get_youtube_id_list()
    for youtube_id in id_list:
        jpg_list = glob.glob(RESOURCES_ROOT + '/youtube_faces/' + youtube_id + '/*.jpg')
        if len(jpg_list) != 0:
            return youtube_id
    return None

if __name__ == '__main__':
    # test
    print(get_a_unlabeled_youtube_id())