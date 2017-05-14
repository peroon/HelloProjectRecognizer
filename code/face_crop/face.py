# -*- coding: utf-8 -*-

import dlib
from skimage import io
import imageio
import time
import pandas as pd

from constant import PROJECT_ROOT, MOVIES_CSV_PATH
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

    timestr = time.strftime("%Y%m%d-%H%M%S")

    for i in range(0, frame_num, interval):
        print(i, '/', frame_num)
        img = reader.get_data(i)

        # detect
        try:
            detects = detector(img, 1)
            for detect_id, d in enumerate(detects):
                cropped = img[d.top():d.bottom(), d.left():d.right()]

                # confirm it is croppable and big enough
                if d.right() > 0 and d.left() > 0 and d.top() > 0 and d.bottom() > 0 and d.right() - d.left() > 99:
                    filename = '{}-{}-{}.jpg'.format(timestr, i, detect_id)
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
            video_path = PROJECT_ROOT + '/resources/youtube/{}.mp4'.format(movie_id)
            interval = 10000  # temp
            detect_from_video(video_path=video_path, save_dir=save_dir, interval=interval)

            # update df
            df.loc[df.movie_id == movie_id, colname.is_face_cropped] = True

    # update csv
    #df.to_csv(MOVIES_CSV_PATH, index=False)

if __name__ == '__main__':
    face_crop_batch()