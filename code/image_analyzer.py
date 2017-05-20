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


class ImageAnalyzer():
    def __init__(self):
        self.face_detector = dlib.get_frontal_face_detector()
        self.face_classifier = FaceClassifier()
        self.face_classifier.load_weight('../temp/model_weight/keras/resnet/epoch_95')

    def analyze(self, image_path):
        image = io.imread(image_path)

        # face detection
        try:
            detects = self.face_detector(image, 1)
        except RuntimeError:
            print('detection failed. skip')

        cv2_image = cv2.imread(image_path)
        if detects:
            drawn_image = self.draw_face_detection_result_to_image(detects, cv2_image)
            return drawn_image
        else:
            cv2_image

    def draw_face_detection_result_to_image(self, detects, image):
        """
        :type image: cv2.Image
        """

        if len(detects) == 0 or detects is None:
            return image

        print('detected face num', len(detects))

        #image = data.load_image(image_path)  # cv2
        #image_for_draw = cv2.imread(image_path)
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
                an_idol = idol.get_idol(label)

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



def __detect_and_draw_test():
    image_analyzer = ImageAnalyzer()
    test_image_path = PROJECT_ROOT + '/resources/test/cute1.jpg'
    result_image = image_analyzer.analyze(test_image_path)
    cv2.imshow('windows name', result_image)
    cv2.waitKey()

if __name__ == '__main__':
    __detect_and_draw_test()