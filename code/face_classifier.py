# -*- coding: utf-8 -*-

"""face classification by CNN"""

from keras.models import Model
from keras.applications.resnet50 import ResNet50
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD

import numpy as np

import constant
import data


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


class FaceClassifier():
    def __init__(self):
        self.model, self.base_model = self.__get_model()

    def __get_model(self):
        image_size = 224
        input_shape = (image_size, image_size, 3)
        base_model = ResNet50(include_top=False, weights='imagenet', input_shape=input_shape)

        # Top層
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(1024, activation='relu')(x)
        x = Dropout(0.5)(x)
        predictions = Dense(constant.LABEL_NUM, activation='softmax')(x)

        # 合体モデル
        model = Model(input=base_model.input, output=predictions)
        return model, base_model

    def learn(self, X_training, Y_training, X_validation, Y_validation):
        # learning for top layer
        for layer in self.base_model.layers:
            layer.trainable = False
        self.model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
        datagen = get_generator()
        self.model.fit_generator(datagen.flow(
            X_training,
            Y_training,
            shuffle=True,
            batch_size=32
        ),
            samples_per_epoch=X_training.shape[0],
            nb_epoch=10,
            verbose=2,
            validation_data=(X_validation, Y_validation)
        )

        # learning for tine tune
        fine_tune_index = 60
        for layer in self.model.layers[:fine_tune_index]:
            layer.trainable = False
        for layer in self.model.layers[fine_tune_index:]:
            layer.trainable = True
        self.model.compile(optimizer=SGD(lr=1e-4, momentum=0.9), loss='categorical_crossentropy',
                           metrics=['accuracy'])
        print('full layer fit()')
        self.model.fit_generator(datagen.flow(
            X_training,
            Y_training,
            shuffle=True,
            batch_size=32
        ),
            samples_per_epoch=X_training.shape[0],
            nb_epoch=100,
            verbose=2, # per epoch
            validation_data=(X_validation, Y_validation)
        )

    def load_weight(self, weight_path):
        pass

    def predict(self, x):
        return [0.1, 0.9]

    def predict_label(self, x):
        probability = self.predict(x)
        return np.argmax(probability)

if __name__ == '__main__':
    classifier = FaceClassifier()

    # 学習時
    enable_learning = True
    if enable_learning:
        X_training, Y_training, X_validation, Y_validation = data.get_train_and_validation_data()
        classifier.learn(X_training, Y_training, X_validation, Y_validation)

    # 予測時
    enable_predict = False
    if enable_predict:
        weight_path = ''
        classifier.load_weight(weight_path)