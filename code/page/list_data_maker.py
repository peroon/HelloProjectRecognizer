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
            ranking = 'TODO'

            df_row = pd.DataFrame([[youtube_id, fps, total_frames, ranking]], columns=columns)
            df.append(df_row)

    print('df')
    print(df)


if __name__ == '__main__':
    generate()