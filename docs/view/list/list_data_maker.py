import glob
import json
import codecs
import numpy as np
import os.path

import common
import idol
import constant
import youtube_api

def __get_videos():
    """
    :rtype: list of youtube_api.VideoInfo
    """
    # id list
    glob_path = constant.PROJECT_ROOT + '/docs/json/*.json'
    id_list = []
    for json_path in glob.glob(glob_path):
        youtube_id = os.path.basename(json_path).split('.')[0]
        id_list.append(youtube_id)

    # video info list
    video_info_list = []
    for youtube_id in id_list:
        video_info = youtube_api.get_video_info(youtube_id)
        print(video_info)
        video_info_list.append(video_info)

    # sort by latest
    video_info_list.sort(key=lambda x: x.published_at)
    return video_info_list


def get_each_videos_data():
    videos = __get_videos()
    data_list = []

    for videoInfo in videos:
        json_path = '../../json/' + videoInfo.id + '.json'

        with open(json_path) as data_file:
            json_data = json.load(data_file)
            print(json_data)

            fps = json_data['fps']
            total_frames = json_data['total_frames']
            interval = json_data['interval']
            idols = json_data['idols']

            print(idols)
            count_list = []
            for i in range(55):
                key = str(i)
                lst = idols[key]
                count = len(lst)
                count_list.append(count)
            arr = np.array(count_list)
            temp = arr.argsort()

            ranking_index = []
            ranking_index.append(temp[-1]) #1st
            ranking_index.append(temp[-2]) #2nd
            ranking_index.append(temp[-3]) #3rd
            ranking = []

            for idol_id in ranking_index:
                idol_name = idol.get_idol(idol_id).name
                cnt = count_list[idol_id]
                print('cnt', cnt)
                bin_num = total_frames // interval
                ratio = cnt / bin_num
                d = {}
                d['name'] = idol_name
                d['ratio'] = ratio
                ranking.append(d)

            data = {}
            data['youtube_id'] = videoInfo.id
            data['ranking'] = ranking
            data['title'] = videoInfo.title
            data['release_date'] = videoInfo.published_at

            data_list.append(data)

    print('data_list')
    print(data_list)
    return data_list


def merge():
    d = {}
    each_videos_data = get_each_videos_data()
    print(each_videos_data)
    d['video_list'] = each_videos_data
    d['groups'] = common.get_groups()
    d['idols'] = common.get_idols()

    with codecs.open('../../data/list.json', 'w', 'utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


if __name__ == '__main__':
    merge()
