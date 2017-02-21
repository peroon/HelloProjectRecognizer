# -*- coding: utf-8 -*-

import glob
import os
from functools import cmp_to_key
from skimage import io

import data


def cmp(a, b):
    if a == b: return 0
    return -1 if a < b else 1


def cmp_by_file_size(path0, path1):
    return cmp(os.path.getsize(path0), os.path.getsize(path1))


def is_same_image(path0, path1):
    image0 = io.imread(path0)
    image1 = io.imread(path1)
    if image0.shape == image1.shape and os.path.getsize(path0) == os.path.getsize(path1):
        return True
    else:
        return False


def remove(target_directory):
    image_path_list = glob.glob(target_directory)
    print('sort')
    image_path_list = sorted(image_path_list, key=cmp_to_key(cmp_by_file_size))

    print('compare')
    for i in range(0, len(image_path_list) - 1):
        path0 = image_path_list[i]
        path1 = image_path_list[i+1]
        if is_same_image(path0, path1):
            os.remove(path0)


if __name__ == '__main__':
    idol_list = data.get_country_list() + data.get_tsubaki_list() + data.get_kobushi_list()
    for idol in idol_list:
        print(idol.name)
        target_dir = '..\\resources\\face\\{0}\\*.jpg'.format(idol.directory_name)
        remove(target_dir)