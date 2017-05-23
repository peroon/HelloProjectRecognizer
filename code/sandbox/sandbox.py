# -*- coding: utf-8 -*-

import cv2
import json
from constant import PROJECT_ROOT

def imshow_need_waitkey():
    image_path = PROJECT_ROOT + '/resources/test/cute1.jpg'
    image = cv2.imread(image_path)
    cv2.imshow('name', image)
    cv2.waitKey()

def save_dict_as_json():
    d = {0: [36, 51]}
    save_path = PROJECT_ROOT + '/resources/test/test.json'
    with open(save_path, 'w') as f:
        json.dump(d, f)

if __name__ == '__main__':
    save_dict_as_json()