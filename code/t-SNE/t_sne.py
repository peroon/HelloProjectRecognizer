# -*- coding: utf-8 -*-

"""Visualization on the distribution of idol faces"""

import glob
from keras.models import Model
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

from idol import get_idol_list
from face_classifier import FaceClassifier
import data

IMAGE_NUM_PER_IDOL = 50


def get_feature_extractor():
    # 分類用モデル
    face_classifier = FaceClassifier()
    print('weight load...')
    face_classifier.load_weight('../../temp/model_weight/epoch_92')
    model = face_classifier.model

    # for layer in model.layers:
    #     print(layer.name, layer.output.get_shape())

    feature_extractor = Model(input=model.input, output=model.get_layer('avg_pool').output)
    return  feature_extractor


def visualize():
    feature_extractor = get_feature_extractor()

    idol_list = get_idol_list()
    #idol_list = idol_list[:10]
    colors = []

    data_num = len(idol_list) * IMAGE_NUM_PER_IDOL
    X = np.zeros((data_num, 2048))
    i = 0

    for idol in idol_list:
        glob_path = '../../resources/face_224x224/{}/ok/*.jpg'.format(idol.directory_name)
        image_path_list = glob.glob(glob_path)
        image_path_list = image_path_list[:IMAGE_NUM_PER_IDOL]

        for image_path in image_path_list:
            print(image_path)
            x = data.load_image(image_path)
            x = np.expand_dims(x, axis=0)
            feature_vector = feature_extractor.predict(x)

            # print(feature_vector.shape)
            # => (1, 1, 1, 2048)
            feature_vector = np.reshape(feature_vector, (1, 2048))

            X[i] = feature_vector
            i += 1

            colors.append(idol.member_color)

    print('t-SNE...')
    t_sne_model = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    ret = t_sne_model.fit_transform(X)
    return ret, colors


def draw_graph(arr, colors):
    #arr = np.array([[ 0.00017882, 0.00004002], [ 0.00009546, 0.00022409]])
    for i, v in enumerate(arr):
        plt.scatter(v[0], v[1], color=colors[i])
    plt.show()
    # vis_x = arr[:, 0]
    # vis_y = arr[:, 1]
    # plt.scatter(vis_x, vis_y, cmap=plt.cm.get_cmap("jet", 10))
    # plt.show()

if __name__ == '__main__':
    arr, colors = visualize()
    draw_graph(arr, colors)
