# -*- coding: utf-8 -*-

import pandas as pd


class Idol():
    def __init__(self, idol_id, group_id, name, directory_name):
        self.idol_id = idol_id
        self.group_id = group_id
        self.name = name
        self.directory_name = directory_name

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.idol_id, self.group_id, self.name, self.directory_name)


def get_idol(idol_id):
    csv_path = '../data/csv/idols.csv'
    df = pd.read_csv(csv_path)
    row = df.loc[idol_id]
    return Idol(idol_id=row['idol_id'], group_id=row['group_id'], name=row['name'], directory_name=row['directory_name'])


if __name__ == '__main__':
    idol = get_idol(2)
    print(idol)