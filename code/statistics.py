# -*- coding: utf-8 -*-

import glob

import data


def list_up_file_num():
    idol_list = data.get_idol_list()
    print('idol num', len(idol_list))

    video_num = 0
    for idol in idol_list:
        glob_path = '../resources/face/{0}/ok/*.jpg'.format(idol.directory_name)
        path_list = glob.glob(glob_path)
        print(idol.name, len(path_list))
        video_num += len(path_list)
    print('video_num', video_num)

if __name__ == '__main__':
    list_up_file_num()