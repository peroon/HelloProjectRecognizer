# -*- coding: utf-8 -*-

import os
import glob
import numpy as np
import cv2

from keras.utils import np_utils

import idol
from idol import Idol
import constant


def load_image(image_path):
    """load image for keras"""

    X = cv2.imread(image_path)
    X = cv2.cvtColor(X, cv2.COLOR_BGR2RGB)
    X = X.astype('float32')
    # 'RGB'->'BGR'
    X = X[:, :, ::-1]

    # Zero-center by mean pixel
    X[:, :, 0] -= 103.939
    X[:, :, 1] -= 116.779
    X[:, :, 2] -= 123.68
    return X


def get_all_image_num():
    idol_list = get_idol_list()
    image_num = 0
    for an_idol in idol_list:
        glob_path = '../resources/face_224x224/{0}/ok/*.jpg'.format(an_idol.directory_name)
        image_path_list = glob.glob(glob_path)
        image_num += len(image_path_list)
    return image_num


def get_train_and_validation_data():
    import prepare # to get same data as mxnet
    image_path_list_training, image_path_list_validation, labels_training, labels_validation = prepare.train_and_validation_path_list()

    training_num = len(image_path_list_training)
    validation_num = len(image_path_list_validation)

    X_training = np.zeros((training_num, constant.IMAGE_SIZE, constant.IMAGE_SIZE, 3), dtype='float32')
    Y_training = np.zeros((training_num,), dtype='uint8')

    X_validation = np.zeros((validation_num, constant.IMAGE_SIZE, constant.IMAGE_SIZE, 3), dtype='float32')
    Y_validation = np.zeros((validation_num,), dtype='uint8')

    for i in range(training_num):
        X_training[i] = load_image(image_path_list_training[i])
        Y_training[i] = labels_training[i]

    for i in range(validation_num):
        X_validation[i] = load_image(image_path_list_validation[i])
        Y_validation[i] = labels_validation[i]

    # one hot vector
    Y_training = np_utils.to_categorical(Y_training, constant.LABEL_NUM)
    Y_validation = np_utils.to_categorical(Y_validation, constant.LABEL_NUM)

    return X_training, Y_training, X_validation, Y_validation


def get_idol_list():
    idol_list = []
    for i in range(constant.LABEL_NUM):
        idol_list.append(idol.get_idol(i))
    return idol_list


def __make_directory():
    idol_list = get_idol_list()
    for idol in idol_list:
        dir_path = '../resources/youtube/' + idol.directory_name
        os.mkdir(dir_path)


def __rename_images():
    glob_path = r'C:\Users\kt\Documents\github_projects\HelloProjectRecognizer\resources\search\mizuho-ono\*.jpg'
    path_list = glob.glob(glob_path)
    for i, path in enumerate(path_list):
        dir_path = os.path.dirname(path)
        image_id = 40000000 + i
        save_path = dir_path + '/' + str(image_id) + '.jpg'
        os.rename(path, save_path)

if __name__ == '__main__':
    # get_train_and_validation_data()
    pass
