# -*- coding: utf-8 -*-

"""Get face images for training"""

import dlib
from skimage import io
import imageio
import time
import pandas as pd
import glob
import os.path

from constant import PROJECT_ROOT, RESOURCES_ROOT, MOVIES_CSV_PATH
import colname
import idol


def detect_from_video(video_path, save_dir, interval=100):
    """Face detection from video"""

    print('load face detector')
    detector = dlib.get_frontal_face_detector()

    print('load mp4 reader')
    reader = imageio.get_reader(video_path, 'ffmpeg')

    frame_num = reader._meta['nframes']
    print('frame num', frame_num)

    youtube_id = path_to_youtube_id(video_path)
    print('youtube id', youtube_id)

    for frame in range(0, frame_num, interval):
        print(frame, '/', frame_num)
        img = reader.get_data(frame)

        # detect
        try:
            detects = detector(img, 1)
            for detect_id, d in enumerate(detects):
                cropped = img[d.top():d.bottom(), d.left():d.right()]

                # confirm it is croppable and big enough
                if d.right() > 0 and d.left() > 0 and d.top() > 0 and d.bottom() > 0 and d.right() - d.left() > 99:
                    filename = 'youtube_id_{}_frame_{}_detect_index_{}.jpg'.format(youtube_id, frame, detect_id)
                    save_path = save_dir + filename
                    io.imsave(save_path, cropped)
        except RuntimeError:
            print('detection failed. skip')


def face_crop_batch():
    # read csv
    df = pd.read_csv(MOVIES_CSV_PATH)

    # not cropped yet only
    for i, row in df.iterrows():
        if not row[colname.is_face_cropped]:
            movie_id = row[colname.movie_id]
            print('crop this movie', movie_id)

            print(row[colname.specific_idol_id])
            if row[colname.specific_idol_id] == 'None':
                save_dir = PROJECT_ROOT + '/resources/face/__uncategorized/'
            else:
                idol_id = int(row[colname.specific_idol_id])
                dir_name = idol.get_idol_directory(idol_id)
                save_dir = PROJECT_ROOT + '/resources/face/{}/candidates/'.format(dir_name)

            # execute crop
            video_path = youtube_id_to_path(movie_id)
            interval = 10000  # temp
            detect_from_video(video_path=video_path, save_dir=save_dir, interval=interval)

            # update df
            df.loc[df.movie_id == movie_id, colname.is_face_cropped] = True

    # update csv
    #df.to_csv(MOVIES_CSV_PATH, index=False)


def youtube_id_to_path(youtube_id):
    return RESOURCES_ROOT + '/youtube/' + youtube_id + '.mp4'


def path_to_youtube_id(path):
    base = os.path.basename(path)
    return os.path.splitext(base)[0]


def extract_faces_from_youtube_video(youtube_id):
    print('youtube id : ', youtube_id)
    # makedir
    dir_path = RESOURCES_ROOT + '/youtube_faces/'+ youtube_id
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # extract
    detect_from_video(
        video_path=youtube_id_to_path(youtube_id),
        save_dir=dir_path + '/',
        interval=1000
    )


def __get_youtube_id_list():
    path_list = glob.glob(RESOURCES_ROOT + '/youtube/*.mp4')
    id_list = []
    for path in path_list:
        id_list.append(path_to_youtube_id(path))
    id_list.sort()
    return id_list

if __name__ == '__main__':
    id_list = __get_youtube_id_list()
    print(id_list)

    # test
    youtube_id = id_list[0]
    extract_faces_from_youtube_video(youtube_id)