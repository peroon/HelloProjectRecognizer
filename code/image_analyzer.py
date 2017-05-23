# -*- coding: utf-8 -*-

"""Analyze where in the image who is."""

import dlib
import cv2
from skimage import io
import numpy as np

from face_classifier import FaceClassifier
import idol
import color
from constant import PROJECT_ROOT
import data

class ImageAnalyzer():
    def __init__(self):
        self.face_detector = dlib.get_frontal_face_detector()
        self.face_classifier = FaceClassifier()
        self.face_classifier.load_weight('../temp/model_weight/keras/resnet/epoch_95')

    def analyze(self, image_path):
        """
        :param image_path:
        :return: detects, idol_ids
        """
        io_image = io.imread(image_path)

        # face detection
        try:
            detects = self.face_detector(io_image, 1)
        except RuntimeError:
            print('detection failed. skip')

        cv2_image = data.load_image(image_path)
        if detects:
            idol_ids = self.classify(detects, cv2_image)
            return detects, idol_ids
        else:
            return None, None

    def classify(self, detects, image):
        """classify cropped faces"""
        idol_ids = []
        for i, d in enumerate(detects):
            cropped = image[d.top():d.bottom(), d.left():d.right()]

            if d.right() > 0 and d.left() > 0 and d.top() > 0 and d.bottom() > 0:
                in_image = True
            else:
                in_image = False

            # Exclude small faces
            size_threshold = 64
            if d.right() - d.left() > size_threshold:
                enough_size = True
            else:
                enough_size = False

            if in_image and enough_size:
                resized = cv2.resize(cropped, (224, 224))
                probability = self.face_classifier.predict(resized)
                idol_id = int(np.argmax(probability))
                idol_ids.append(idol_id)
            else:
                idol_ids.append(None)
        return idol_ids

    def draw_face_detection_result_to_image(self, detects, image):
        """
        :type image: cv2.Image
        """

        if len(detects) == 0 or detects is None:
            return image

        print('detected face num', len(detects))

        image_for_draw = image.copy()

        for i, d in enumerate(detects):
            cropped = image[d.top():d.bottom(), d.left():d.right()]

            if d.right() > 0 and d.left() > 0 and d.top() > 0 and d.bottom() > 0:
                in_image = True
            else:
                in_image = False

            # Exclude too small faces
            size_threshold = 64
            if d.right() - d.left() > size_threshold:
                enough_size = True
            else:
                enough_size = False

            if in_image and enough_size:
                resized = cv2.resize(cropped, (224, 224))
                cv2.imshow(str(i), resized)
                probability = self.face_classifier.predict(resized)
                label = np.argmax(probability)
                probability_max = np.max(probability)
                an_idol = idol.get_idol(int(label))

                # draw circle
                pos0 = (d.left(), d.top())
                pos1 = (d.right(), d.bottom())
                member_color = color.color_code_to_bgr_tuple(an_idol.member_color)
                x_center = (d.left() + d.right()) / 2
                y_center = (d.top() + d.bottom()) / 2
                center = (int(x_center), int(y_center))
                radius = int(center[0] - pos0[0])
                thickness = 2
                cv2.circle(img=image_for_draw,
                           center=center,
                           radius=radius,
                           color=member_color,
                           thickness=thickness)

                font = cv2.FONT_HERSHEY_SIMPLEX
                # text = an_idol.alphabet_name() + ' {0:10.2f}'.format(probability_max)
                text = an_idol.alphabet_name() + ' ' + str(probability_max)
                # shadow text
                cv2.putText(img=image_for_draw,
                            text=text,
                            org=(pos0[0] + 1, pos0[1] + 1),
                            fontFace=font,
                            fontScale=1,
                            color=(0, 0, 0),
                            lineType=cv2.LINE_AA
                            )
                # color text
                cv2.putText(img=image_for_draw,
                            text=text,
                            org=pos0,
                            fontFace=font,
                            fontScale=1,
                            color=member_color,
                            lineType=cv2.LINE_AA
                            )

            else:
                print('事前チェックによりスルー', in_image, enough_size)
        return image_for_draw

    def test(self):
        image_path = PROJECT_ROOT + '/resources/test/cute1.jpg'
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        dets = self.face_detector(image_rgb, 1)
        print("Number of faces detected: {}".format(len(dets)))
        for i, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                i, d.left(), d.top(), d.right(), d.bottom()))

        win = dlib.image_window()
        win.clear_overlay()
        win.set_image(image_rgb)
        win.add_overlay(dets)
        dlib.hit_enter_to_continue()



def __detect_and_draw_test():
    image_analyzer = ImageAnalyzer()
    test_image_path = PROJECT_ROOT + '/resources/test/cute1.jpg'
    result_image = image_analyzer.analyze(test_image_path)
    cv2.imshow('windows name', result_image)
    cv2.waitKey()


if __name__ == '__main__':
    #__detect_and_draw_test()

    image_analyzer = ImageAnalyzer()
    image_path = PROJECT_ROOT + '/resources/test/cute1.jpg'
    detects, idol_ids = image_analyzer.analyze(image_path)
    print('detects', detects)
    print('idol_ids', idol_ids)