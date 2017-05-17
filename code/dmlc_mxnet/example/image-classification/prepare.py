# -*- coding: utf-8 -*-

"""Prepare for Training"""

import glob
import os
from collections import deque

import data
from constant import PROJECT_ROOT

lst_output_dir = PROJECT_ROOT + '/resources/rec_files'


def split_list(list_input, fold_num=5, fold_index=0):
    """split data for train and validation"""

    num_all = len(list_input)
    num_val = int(num_all / fold_num)
    num_tra = num_all - num_val

    deq = deque(list_input)
    deq.rotate(fold_index * num_val)
    return list(deq)[:num_tra], list(deq)[num_tra:]


def write_lst(save_path, image_path_list, labels):
    f = open(save_path, 'w')
    for i in range(len(image_path_list)):
        s = '{}\t{}\t{}\n'.format(i, labels[i], image_path_list[i])
        f.write(s)
    f.close()


def make_train_and_validation_lst():

    image_path_list_training = []
    image_path_list_validation = []
    labels_training = []
    labels_validation = []

    for idol in data.get_idol_list():
        glob_path = PROJECT_ROOT + "/resources/face_224x224/{}/ok/*.jpg".format(idol.directory_name)
        image_path_list = glob.glob(glob_path)
        image_path_list = image_path_list[:100]

        # DEBUG
        #image_path_list = image_path_list[:20]

        # split
        trains, validations = split_list(image_path_list, fold_index=0)
        train_labels = [idol.idol_id] * len(trains)
        validation_labels = [idol.idol_id] * len(validations)

        # concatenate
        image_path_list_training += trains
        image_path_list_validation += validations
        labels_training += train_labels
        labels_validation += validation_labels

    # save
    train_lst_path = lst_output_dir + '/training.lst'
    write_lst(train_lst_path, image_path_list_training, labels_training)

    validation_lst_path = lst_output_dir + '/validation.lst'
    write_lst(validation_lst_path, image_path_list_validation, labels_validation)


def make_bat():
    im2rec_fullpath = os.path.abspath('../..//tools/im2rec.py')
    lst_path_list = glob.glob(lst_output_dir + '/*.lst')

    # make bat
    with open(lst_output_dir + '/make_rec.bat', 'w') as f:
        for lst_path in lst_path_list:
            filename_without_ext = os.path.basename(lst_path).split('.')[0]
            print(filename_without_ext)
            s = 'python {} --encoding .jpg {} .'.format(im2rec_fullpath, filename_without_ext)
            f.write(s + '\n')

    print('Execute .bat to make rec file.')
    print(lst_output_dir)




if __name__ == '__main__':
    make_train_and_validation_lst()
    make_bat()