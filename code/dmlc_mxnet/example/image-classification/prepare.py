# -*- coding: utf-8 -*-

"""Prepare for Training"""

import glob
import cv2
import os
import shutil
from collections import deque

from tqdm import tqdm

import data
from constant import PROJECT_ROOT


def split_list(list_input, fold_num=5, fold_index=0):
    """split data for train and validation"""

    num_all = len(list_input)
    num_val = int(num_all / fold_num)
    num_tra = num_all - num_val

    deq = deque(list_input)
    deq.rotate(fold_index * num_val)
    return list(deq)[:num_tra], list(deq)[num_tra:]


def get_labels():
    labels = []
    with open(IMAGES_ROOT + 'clf_train_master.tsv', 'r') as f:
        f.readline()
        for s in f:
            label = int(s.split()[-1])
            labels.append(label)
    return labels


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

        # DEBUG
        image_path_list = image_path_list[:20]

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
    lst_output_dir = PROJECT_ROOT + '/resources/rec_files'

    # ファイルに書き込む
    train_lst_path = lst_output_dir + '/training.lst'
    write_lst(train_lst_path, image_path_list_training, labels_training)

    validation_lst_path = lst_output_dir + '/validation.lst'
    write_lst(validation_lst_path, image_path_list_validation, labels_validation)


def make_test_lst():

    # 各cropごとに1ファイルにする
    for crop_i in range(0, 4):
        glob_path = IMAGES_ROOT + 'clf_test_224x224_{}/*'.format(crop_i)
        image_path_list = glob.glob(glob_path)

        if DEBUG:
            image_path_list = image_path_list[:100]

        labels = [0] * len(image_path_list)

        # ファイルに書き込む
        lst_path = mxnet_dir + 'test_224x224_crop_{}.lst'.format(crop_i)
        write_lst(lst_path, image_path_list, labels)


def make_rec():
    im2rec_fullpath = os.path.abspath('./dmlc_mxnet/tools/im2rec.py')
    lst_path_list = glob.glob(mxnet_dir + '*.lst')

    # make bat
    with open(mxnet_dir + 'make_rec.bat', 'w') as f:
        for lst_path in lst_path_list:
            filename_without_ext = os.path.basename(lst_path).split('.')[0]
            print(filename_without_ext)
            s = 'python {} --encoding .png {} .'.format(im2rec_fullpath, filename_without_ext)
            f.write(s + '\n')

    print('Execute .bat to make rec file.')
    print(mxnet_dir)




if __name__ == '__main__':
    make_train_and_validation_lst()