# -*- coding: utf-8 -*-

import dlib
from skimage import io
import imageio
import glob
import os
import pandas as pd

import data
from constant import PROJECT_ROOT, MOVIES_CSV_PATH
import colname


def detect_idol(idol, input_dir='search'):
    """Face detection with idle designation"""

    print('detector load')
    detector = dlib.get_frontal_face_detector()

    print(idol.name)
    glob_path = PROJECT_ROOT + "/resources/{0}/{1}/*.jpg".format(input_dir, idol.directory_name)
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
            print('[OSError] skip', image_path)


def detect_from_video(video_path, save_dir, interval=100, image_id = 50000000):
    """Face detection from video"""

    print('detector load')
    detector = dlib.get_frontal_face_detector()


    print('reader')
    reader = imageio.get_reader(video_path, 'ffmpeg')

    frame_num = reader._meta['nframes']
    print('frame num', frame_num)

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


def face_crop_batch():
    # read csv
    df = pd.read_csv(MOVIES_CSV_PATH)

    # not cropped only
    for i, row in df.iterrows():
        if not row[colname.is_face_cropped]:
            movie_id = row[colname.movie_id]
            print('crop this movie', movie_id)

            # crop
            # TODO

            # update df
            df.loc[df.movie_id == movie_id, colname.is_face_cropped] = True

    # update csv
    #df.to_csv(MOVIES_CSV_PATH, index=False)

if __name__ == '__main__':
    face_crop_batch()

    # 個別
    if False:
        idol = data.get_tsubaki_list()[-3]
        detect_idol(idol, 'search')

    if False:
        youtube_id = 'fIPA3PbS0w0'
        idol_name = name.momona_kasahara
        image_id = 5044 * 10000
        detect_from_video(video_path='../resources/youtube/{0}.mp4'.format(youtube_id),
                          save_dir='../resources/face/{0}/'.format(idol_name),
                          interval=100,
                          image_id=image_id)
