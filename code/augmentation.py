# -*- coding: utf-8 -*-

from keras.preprocessing.image import ImageDataGenerator


def get_generator():
    datagen = ImageDataGenerator(
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range=0,  # 回転角度範囲 (degrees, 0 to 180)

        zoom_range=0.2,
        shear_range=0.2,

        width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=True,  # 横反転
        vertical_flip=False)  # 縦反転
    return datagen