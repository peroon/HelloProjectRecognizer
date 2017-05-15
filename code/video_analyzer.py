# -*- coding: utf-8 -*-

"""ビデオを分析して結果をJSONに保存する"""

from image_analyzer import ImageAnalyzer
import imageio
import cv2
import time


class VideoAnalyzer():
    def __init__(self):
        self.image_analyzer = ImageAnalyzer()

    def analyze(self, video_path, output_directory, interval=100):
        # load video
        reader = imageio.get_reader(video_path, 'ffmpeg')
        frame_num = reader._meta['nframes']
        print('frame num', frame_num)

        # analyze each frame
        for i in range(0, frame_num, interval):
            print('current frame', i)
            image = reader.get_data(i)
            temp_path = '../temp/temp.jpg'
            imageio.imwrite(uri=temp_path, im=image)
            result_image = self.image_analyzer.analyze(temp_path)

            save_path = output_directory + '{0:08d}'.format(i) + '.jpg'
            cv2.imwrite(save_path, result_image)

if __name__ == '__main__':
    video_analyzer = VideoAnalyzer()
    video_path = '../resources/youtube_1080p/bfoogf5i6N8.mp4'
    output_dir =  '../temp/video_analyze_result/'

    start_time = time.time()
    video_analyzer.analyze(video_path=video_path, output_directory=output_dir)
    end_time = time.time()
    print('analyze time:', end_time - start_time)
