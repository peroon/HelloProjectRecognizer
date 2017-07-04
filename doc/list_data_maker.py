import glob
import json
import codecs
import numpy as np

import idol


def __get_videos():
    videos = []
    with open('./data/videos.csv', 'r', encoding='utf8') as f:
        lines = f.readlines()[1:]
        for line in lines:
            data = line.strip().split(',')
            videos.append(data)
    return videos


def __get_groups():
    groups = []
    with open('../data/csv/groups.csv', 'r', encoding='utf8') as f:
        f.readline()
        for s in f:
            group_name = s.strip().split(',')[-1]
            groups.append(group_name)
    return groups


def __get_idols():
    idols = []
    with open('../data/csv/idols.csv', 'r', encoding='utf8') as f:
        f.readline()
        for s in f:
            idol = s.strip().split(',')
            idols.append(idol)
    return idols


def get_each_videos_data():
    videos = __get_videos()
    data_list = []

    for video in videos:
        youtube_id = video[0]
        json_path = '../resources/json/' + youtube_id + '.json'

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
            data['youtube_id'] = youtube_id
            data['ranking'] = ranking
            data['title'] = video[1]
            data['release_date'] = video[2]

            data_list.append(data)

    print('data_list')
    print(data_list)
    return data_list


def merge():
    d = {}
    each_videos_data = get_each_videos_data()
    d['video_list'] = each_videos_data
    d['groups'] = __get_groups()
    d['idols'] = __get_idols()

    with codecs.open('./data/list.json', 'w', 'utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


if __name__ == '__main__':
    merge()
