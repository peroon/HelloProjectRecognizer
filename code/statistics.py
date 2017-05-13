# -*- coding: utf-8 -*-

import glob

import data


def list_up():
    """list up the number of images for each idle"""

    idol_list = data.get_idol_list()
    print('idol num', len(idol_list))

    jpg_num = 0
    for idol in idol_list:
        glob_path = '../resources/face/{0}/ok/*.jpg'.format(idol.directory_name)
        path_list = glob.glob(glob_path)
        print(idol.name, len(path_list))
        jpg_num += len(path_list)
    print('jpg_num', jpg_num)

if __name__ == '__main__':
    list_up()