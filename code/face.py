# -*- coding: utf-8 -*-

import sys
import dlib
import pprint
from skimage import io

print(sys.version)
print('detector load')
detector = dlib.get_frontal_face_detector()
print('detector load end')

image_path = r"C:\Users\kt\Documents\github_projects\HelloProjectRecognizer\resources\search\maimi-yajima\00000032.jpg"
img = io.imread(image_path)

dets = detector(img, 1)
print("Number of faces detected: {}".format(len(dets)))
for i, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(i, d.left(), d.top(), d.right(), d.bottom()))
