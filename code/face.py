# -*- coding: utf-8 -*-

import sys
import dlib
import pprint
from skimage import io
import glob
import os.path

import data


def detect():
    print(sys.version)
    print('detector load')
    detector = dlib.get_frontal_face_detector()
    print('detector load end')

    idol_list = data.get_idol_list()
    idol_list = idol_list[8:]
    for idol in idol_list:
        print(idol.name)
        glob_path = "C:\\Users\\kt\Documents\\github_projects\\HelloProjectRecognizer\\resources\\search\\{0}\\*.jpg".format(idol.directory_name)
        image_path_list = glob.glob(glob_path)

        for image_path in image_path_list:
            print('load', image_path)
            try:
                img = io.imread(image_path)
                try:
                    detects = detector(img, 1)
                    for i, d in enumerate(detects):
                        cropped = img[d.top():d.bottom(), d.left():d.right()]
                        if d.right() > 0 and d.left() > 0 and d.top() > 0 and d.bottom() > 0 and d.right() - d.left() > 99:
                            save_path = image_path.replace('search', 'face')
                            file_path, ext = os.path.splitext(save_path)
                            save_path = file_path + '-' + str(i) + ext
                            io.imsave(save_path, cropped)
                except RuntimeError:
                    print('detection failed. skip')
            except OSError:
                print('スキップします', image_path)


if __name__ == '__main__':
    detect()
