# -*- coding: utf-8 -*-

"""Analyze the video and save the result to JSON"""

from image_analyzer import ImageAnalyzer
import imageio
import time
import json


class VideoAnalyzer():
    def __init__(self):
        self.image_analyzer = ImageAnalyzer()

    def analyze(self, video_path, interval=1000):
        # load video
        reader = imageio.get_reader(video_path, 'ffmpeg')
        frame_num = reader._meta['nframes']
        print('frame num', frame_num)

        result = {}

        # analyze each frame
        for i in range(0, frame_num, interval):
            print('current frame', i)
            image = reader.get_data(i)
            temp_path = '../temp/temp.jpg'
            imageio.imwrite(uri=temp_path, im=image)
            detects, idol_ids = self.image_analyzer.analyze(temp_path)
            print(i, idol_ids)
            result[i] = idol_ids

        return result

if __name__ == '__main__':
    video_analyzer = VideoAnalyzer()
    video_path = '../resources/youtube/N0c-jH-r_lo.mp4'

    result = video_analyzer.analyze(video_path=video_path)
    json_save_path = video_path.replace('youtube', 'json').replace('mp4', 'json')
    print('json', json_save_path)
    print(result)
    with open(json_save_path, 'w') as f:
        json.dump(result, f)
