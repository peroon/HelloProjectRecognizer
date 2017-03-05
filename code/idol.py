# -*- coding: utf-8 -*-

import pandas as pd
import os

import constant


class Idol():
    def __init__(self, idol_id, group_id, name, directory_name, member_color):
        self.idol_id = idol_id
        self.group_id = group_id
        self.name = name
        self.directory_name = directory_name
        self.member_color = member_color

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(
            self.idol_id,
            self.group_id,
            self.name,
            self.directory_name,
            self.member_color
        )

    def alphabet_name(self):
        sep = self.directory_name.split('-')
        return sep[0].capitalize() + ' ' + sep[1].capitalize()


def get_idol(idol_id):
    csv_path = os.path.dirname(__file__) + '/../data/csv/idols.csv'
    df = pd.read_csv(csv_path)
    row = df.loc[idol_id]
    return Idol(
        idol_id=row['idol_id'],
        group_id=row['group_id'],
        name=row['name'],
        directory_name=row['directory_name'],
        member_color=row['member_color']
    )


def get_idol_list():
    idol_list = []
    for i in range(constant.LABEL_NUM):
        idol = get_idol(i)
        idol_list.append(idol)
    return idol_list


if __name__ == '__main__':
    idol = get_idol(2)
    print(idol)
    print(idol.alphabet_name())