import glob
import json
import pandas as pd


def generate():
    lst = glob.glob('../../resources/json/*.json')

    columns = ['youtube_id', 'fps', 'total_frames', 'ranking']
    df = pd.DataFrame([[]], index=columns)

    for json_path in lst:
        youtube_id = json_path.split('\\')[-1].split('.')[0]

        with open(json_path) as data_file:
            data = json.load(data_file)
            print(data)

            fps = data['fps']
            total_frames = data['total_frames']

            idols = data['idols']
            # TODO
            ranking = []
            ranking.append('idol_name0,20%')
            ranking.append('idol_name1,19%')
            ranking.append('idol_name2,18%')

            df_row = pd.DataFrame([[youtube_id, fps, total_frames, ranking]], columns=columns)
            print(df_row)
            df.append(df_row)

    print('df')
    print(df)

    csv = df.to_csv()
    print('csv')
    print(csv)


if __name__ == '__main__':
    generate()