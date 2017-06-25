import glob
import json
import codecs
import numpy as np

import idol


def generate():
    path_list = glob.glob('../../resources/json/*.json')
    data_list = []

    for json_path in path_list:
        youtube_id = json_path.split('\\')[-1].split('.')[0]

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

            data_list.append(data)

    print('data_list')
    print(data_list)

    #with open('./data/temp.json', 'w') as f:
    with codecs.open('./data/temp.json', 'w', 'utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

if __name__ == '__main__':
    generate()