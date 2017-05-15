# -*- coding: utf-8 -*-

import glob

import data


def list_up():
    """list up the number of images for each idle"""

    idol_list = data.get_idol_list()
    print('idol num', len(idol_list))

    num_list = []
    for idol in idol_list:
        glob_path = '../resources/face/{0}/ok/*.jpg'.format(idol.directory_name)
        path_list = glob.glob(glob_path)
        print(idol.name, len(path_list))
        num_list.append(len(path_list))

    print('-----')
    print('jpg num', sum(num_list))

    v = max(num_list)
    i = num_list.index(v)
    print('max', v, idol_list[i].name)

    v = min(num_list)
    i = num_list.index(v)
    print('min', v, idol_list[i].name)


if __name__ == '__main__':
    list_up()