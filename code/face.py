# -*- coding: utf-8 -*-

import sys
import dlib
import pprint
from skimage import io
import glob
import os.path


def detect():
    print(sys.version)
    print('detector load')
    detector = dlib.get_frontal_face_detector()
    print('detector load end')

    image_path_list = glob.glob("C:\\Users\\kt\Documents\\github_projects\\HelloProjectRecognizer\\resources\\search\\maimi-yajima\\*.jpg")
    image_path_list = image_path_list[300:]

    for image_path in image_path_list:
        print('load', image_path)
        try:
            img = io.imread(image_path)
            detects = detector(img, 1)
            print("Number of faces detected: {}".format(len(detects)))
            for i, d in enumerate(detects):
                cropped = img[d.top():d.bottom(), d.left():d.right()]
                if d.right() > 0 and d.left() > 0 and d.top() > 0 and d.bottom() > 0 and d.right() - d.left() > 99:
                    pprint.pprint(d)
                    save_path = image_path.replace('search', 'face')
                    file_path, ext = save_path = os.path.splitext(save_path)
                    save_path = file_path + '-' + str(i) + ext
                    print(save_path)
                    io.imsave(save_path, cropped)
        except OSError:
            print('スキップします', image_path)




if __name__ == '__main__':
    detect()
