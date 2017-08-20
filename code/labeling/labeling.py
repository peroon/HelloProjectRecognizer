"""Labeling to cropped face images"""

import cv2
import glob

import constant
import youtube

image_index = 0


def open_editor(youtube_id):
    print('youtube id', youtube_id)
    face_images_glob_path = constant.RESOURCES_ROOT + '/youtube_faces/' + youtube_id + '/*.jpg'
    path_list = glob.glob(face_images_glob_path)
    while True:
        image = cv2.imread(path_list[image_index])
        cv2.imshow('labeling', image)

        # Exit
        key = cv2.waitKey(30) & 0xff
        if key == 27:  # ESC
            break

        print(key)

if __name__ == '__main__':
    id_list = youtube.get_youtube_id_list()
    youtube_id = id_list[0]
    open_editor(youtube_id)