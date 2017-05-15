# -*- coding: utf-8 -*-

"""face classification Keras version"""

from keras.models import Model
from keras.applications.resnet50 import ResNet50
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, EarlyStopping

from skimage import io
import cv2
import numpy as np

import constant
import data
import idol
import augmentation


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
        datagen = augmentation.get_generator()
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

        # learning for fine tune
        fine_tune_index = 60
        for layer in self.model.layers[:fine_tune_index]:
            layer.trainable = False
        for layer in self.model.layers[fine_tune_index:]:
            layer.trainable = True
        self.model.compile(optimizer=SGD(lr=1e-4, momentum=0.9), loss='categorical_crossentropy',
                           metrics=['accuracy'])
        # save model weight
        file_path = "../temp/model_weight/epoch_{epoch:02d}"
        check_point = ModelCheckpoint(filepath=file_path, verbose=1, save_best_only=True)

        # early stopping
        #early_stopping = EarlyStopping()

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
            validation_data=(X_validation, Y_validation),
            callbacks=[check_point]
        )

    def load_weight(self, weight_path):
        self.model.load_weights(weight_path)

    def predict(self, x):
        x = np.expand_dims(x, axis=0)
        return self.model.predict(x)

    def predict_label(self, x):
        probability = self.predict(x)
        return np.argmax(probability)

if __name__ == '__main__':
    classifier = FaceClassifier()

    # 学習時
    enable_learning = False
    if enable_learning:
        X_training, Y_training, X_validation, Y_validation = data.get_train_and_validation_data()
        classifier.learn(X_training, Y_training, X_validation, Y_validation)

    # 予測時
    enable_predict = True
    if enable_predict:
        weight_path = '../temp/model_weight/epoch_92'
        classifier.load_weight(weight_path)

        face_image_path = r'C:\Users\kt\Documents\github_projects\HelloProjectRecognizer\resources\face_224x224\airi-suzuki\ok\00000002-0.jpg'
        image = data.load_image(face_image_path)

        probability = classifier.predict(image)
        print(probability)

        label = np.argmax(probability)
        predicted_idol = idol.get_idol(label)
        print(predicted_idol)

