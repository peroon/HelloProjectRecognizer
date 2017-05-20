# -*- coding: utf-8 -*-

import cv2
from constant import PROJECT_ROOT

if __name__ == '__main__':
    image_path = PROJECT_ROOT + '/resources/test/cute1.jpg'
    image = cv2.imread(image_path)
    cv2.imshow('name', image)
    cv2.waitKey()