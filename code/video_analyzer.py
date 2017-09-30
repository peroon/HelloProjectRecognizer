# -*- coding: utf-8 -*-

"""Analyze the video and save the result to JSON"""

from image_analyzer import ImageAnalyzer
import imageio
import json

import constant
import youtube_api


class VideoAnalyzer():
    def __init__(self):
        self.image_analyzer = ImageAnalyzer()

    def analyze(self, video_path, interval=1000):
        # load video
        reader = imageio.get_reader(video_path, 'ffmpeg')
        frame_num = reader.get_meta_data()['nframes']
        print('frame length', frame_num)

        fps = reader.get_meta_data()['fps']
        print('fps', fps)

        result = {}
        result['total_frames'] = frame_num
        result['fps'] = fps

        detected_frames_for_each_idol = {}
        for i in range(constant.LABEL_NUM):
            detected_frames_for_each_idol[str(i)] = []

        # analyze each frame
        for f in range(0, frame_num, interval):
            print('current frame', f, '/', frame_num)
            try:
                image = reader.get_data(f)
                temp_path = '../temp/temp.jpg'
                imageio.imwrite(uri=temp_path, im=image)
                detects, idol_ids = self.image_analyzer.analyze(temp_path)
                if idol_ids:
                    for idol_id in idol_ids:
                        if idol_id:
                            detected_frames_for_each_idol[str(idol_id)].append(f)
            except imageio.core.format.CannotReadFrameError:
                print('[ERROR]unreadable frame', f)

        result['idols'] = detected_frames_for_each_idol
        result['interval'] = interval

        return result

if __name__ == '__main__':
    video_analyzer = VideoAnalyzer()
    youtube_id = '0EwG_EJ7Aaw'

    # check if it is published now
    #info = youtube_api.get_video_info(youtube_id)
    # TODO

    video_path = '../resources/youtube/' + youtube_id + '.mp4'

    result = video_analyzer.analyze(video_path=video_path, interval=30)
    json_save_path = '../docs/json/' + youtube_id + '.json'
    print('json save to', json_save_path)
    print(result)
    with open(json_save_path, 'w') as f:
        json.dump(result, f, indent=4, sort_keys=True, separators=(',', ': '))
