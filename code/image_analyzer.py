# -*- coding: utf-8 -*-

"""画像内のどこに誰がいるか分析する"""

import dlib
import cv2
import time
from skimage import io
import pprint


from face_classifier import FaceClassifier
import idol
import data
import color


class ImageAnalyzer():
    def __init__(self):
        self.face_detector = dlib.get_frontal_face_detector()
        self.face_classifier = FaceClassifier()
        self.face_classifier.load_weight('../temp/model_weight/epoch_92')

    def analyze(self, image_path):
        print('analyze')
        """画像を入力として、分析結果を返す"""

        image = io.imread(image_path)

        # face detection
        try:
            detects = self.face_detector(image, 1)
            if len(detects) > 0:
                image = data.load_image(image_path) # cv2
                image_for_draw = cv2.imread(image_path)

                for i, d in enumerate(detects):
                    print(i)
                    cropped = image[d.top():d.bottom(), d.left():d.right()]

                    pprint.pprint(d)
                    print('shape', image.shape)

                    # 画面内か
                    if d.right() > 0 and d.left() > 0 and d.top() > 0 and d.bottom() > 0:
                        in_image = True
                    else:
                        in_image = False

                    # 小さすぎる顔は除外
                    size_threshold = 32
                    if d.right() - d.left() > size_threshold:
                        enough_size = True
                    else:
                        enough_size = False

                    if in_image and enough_size:
                        resized = cv2.resize(cropped, (224, 224))
                        label = self.face_classifier.predict_label(resized)
                        an_idol = idol.get_idol(label)
                        print(an_idol)

                        # draw rect
                        pos0 = (d.left(), d.top())
                        pos1 = (d.right(), d.bottom())
                        print('pos0', pos0)
                        print('pos1', pos1)
                        member_color = color.color_code_to_bgr_tuple(an_idol.member_color)
                        #image_for_draw = cv2.rectangle(image_for_draw, pos0, pos1, color=member_color)

                        # draw circle
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


                        # text
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        # shadow
                        cv2.putText(img=image_for_draw,
                                    text=an_idol.alphabet_name(),
                                    org=(pos0[0] + 1, pos0[1] + 1),
                                    fontFace=font,
                                    fontScale=1,
                                    color=(0, 0, 0),
                                    lineType=cv2.LINE_AA
                                    )
                        # color text
                        cv2.putText(img=image_for_draw,
                                    text=an_idol.alphabet_name(),
                                    org=pos0,
                                    fontFace=font,
                                    fontScale=1,
                                    color=member_color,
                                    lineType=cv2.LINE_AA
                                    )
                    else:
                        print('事前チェックによりスルー', in_image, enough_size)

        except RuntimeError:
            print('detection failed. skip')

        # save
        cv2.imwrite('../resources/result/result.jpg', image_for_draw)

        # classification

        result = []
        return result


if __name__ == '__main__':
    image_analyzer = ImageAnalyzer()
    image_path = r'C:\Users\kt\Documents\github_projects\HelloProjectRecognizer\resources\test\cute1.jpg'
    #image_path = r'C:\Users\kt\Documents\github_projects\HelloProjectRecognizer\resources\search\akane-haga\00000001.jpg'

    image_analyzer.analyze(image_path)
