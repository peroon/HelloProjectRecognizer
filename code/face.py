# -*- coding: utf-8 -*-

import sys
import dlib
import pprint
from skimage import io
import imageio
import glob
import os.path

import data
import name


def detect_idols():
    """一括で顔検出"""

    idol_list = data.get_idol_list()
    idol_list = idol_list[8:]
    for idol in idol_list:
        detect_idol(idol)


def detect_idol(idol, input_dir='search'):
    """アイドル指定で顔検出"""

    print('detector load')
    detector = dlib.get_frontal_face_detector()

    print(idol.name)
    glob_path = "C:\\Users\\kt\Documents\\github_projects\\HelloProjectRecognizer\\resources\\{0}\\{1}\\*.jpg".format(input_dir, idol.directory_name)
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
                        save_path = image_path.replace(input_dir, 'face')
                        file_path, ext = os.path.splitext(save_path)
                        save_path = file_path + '-' + str(i) + ext
                        io.imsave(save_path, cropped)
            except RuntimeError:
                print('detection failed. skip')
        except OSError:
            print('スキップします', image_path)


def detect_from_video(video_path, save_dir, interval=10, image_id = 50000000):
    """ビデオからも顔検出"""

    print('detector load')
    detector = dlib.get_frontal_face_detector()

    print('reader')
    reader = imageio.get_reader(video_path, 'ffmpeg')

    frame_num = reader._meta['nframes']
    print('frame num', frame_num)

    #for i, img in enumerate(reader):
    for i in range(0, frame_num, interval):
        print(i, '/', frame_num)
        save_id = image_id + i
        img = reader.get_data(i)

        # detect
        try:
            detects = detector(img, 1)
            for detect_id, d in enumerate(detects):
                cropped = img[d.top():d.bottom(), d.left():d.right()]
                if d.right() > 0 and d.left() > 0 and d.top() > 0 and d.bottom() > 0 and d.right() - d.left() > 99:
                    save_path = save_dir + str(save_id) + '-' + str(detect_id) + '.jpg'
                    io.imsave(save_path, cropped)
        except RuntimeError:
            print('detection failed. skip')


if __name__ == '__main__':
    # 一括
    #detect_idols()

    # 個別
    if True:
        idol = data.get_tsubaki_list()[-3]
        detect_idol(idol, 'search')

    if False:
        youtube_id = 'fIPA3PbS0w0'
        idol_name = name.momona_kasahara
        image_id = 5044 * 10000
        detect_from_video('../resources/youtube/{0}.mp4'.format(youtube_id), save_dir='../resources/face/{0}/'.format(idol_name), interval=100, image_id=image_id)
