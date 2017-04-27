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


def get_image_num():
    idol_list = get_idol_list()
    image_num = 0
    for an_idol in idol_list:
        glob_path = '../resources/face_224x224/{0}/ok/*.jpg'.format(an_idol.directory_name)
        image_path_list = glob.glob(glob_path)
        image_num += len(image_path_list)
    return image_num


def get_train_and_validation_data():
    image_num = get_image_num()

    validation_num_per_label = 20
    validation_num = constant.LABEL_NUM * validation_num_per_label
    training_num = image_num - validation_num

    # 入れ物
    X_validation = np.zeros((validation_num, constant.IMAGE_SIZE, constant.IMAGE_SIZE, 3), dtype='float32')
    Y_validation = np.zeros((validation_num,), dtype='uint8')

    X_training = np.zeros((training_num, constant.IMAGE_SIZE, constant.IMAGE_SIZE, 3), dtype='float32')
    Y_training = np.zeros((training_num,), dtype='uint8')

    print(X_validation.shape)
    print(X_training.shape)

    index_validation = 0
    index_training = 0

    idol_list = get_idol_list()
    for an_idol in idol_list:
        print(an_idol.idol_id, an_idol.name)
        glob_path = '../resources/face_224x224/{0}/ok/*.jpg'.format(an_idol.directory_name)
        image_path_list = glob.glob(glob_path)

        # 最初のX件はvalidation, 残りはtrainingへ
        for i, image_path in enumerate(image_path_list):
            try:
                image = load_image(image_path)
                if i < validation_num_per_label:
                    X_validation[index_validation] = image
                    Y_validation[index_validation] = an_idol.idol_id
                    index_validation += 1
                else:
                    X_training[index_training] = image
                    Y_training[index_training] = an_idol.idol_id
                    index_training += 1
            except IndexError:
                print(i, image_path, index_validation, index_training)
    # one hot
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
    get_train_and_validation_data()
    pass
