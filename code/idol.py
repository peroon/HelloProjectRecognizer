# -*- coding: utf-8 -*-

import pandas as pd
import os

import constant


class Idol:
    def __init__(self, idol_id, group_id, name, directory_name, member_color, quit):
        self.idol_id = idol_id
        self.group_id = group_id
        self.name = name
        self.directory_name = directory_name
        self.member_color = member_color
        self.quit = quit

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5}'.format(
            self.idol_id,
            self.group_id,
            self.name,
            self.directory_name,
            self.member_color,
            self.quit
        )

    def __repr__(self):
        return self.__str__()

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
        member_color=row['member_color'],
        quit=row['quit']
    )


def directory_name_to_idol_id(directory_name):
    # e.g. yajima-maimi => 1
    idol_list = get_idols()
    for an_idol in idol_list:
        if an_idol.directory_name == directory_name:
            return an_idol.idol_id


def get_idol_directory(idol_id):
    return get_idol(idol_id).directory_name


def get_idols():
    """
    :rtype: list[Idol]
    """
    idol_list = []
    for i in range(constant.LABEL_NUM):
        an_idol = get_idol(i)
        idol_list.append(an_idol)
    return idol_list

def get_idols_by_group():
    """
    :rtype: list[list[Idol]]
    """
    groups = []
    for i in range(constant.GROUP_NUM):
        groups.append([])
    idols = get_idols()
    for an_idol in idols:
        groups[an_idol.group_id].append(an_idol)
    for g in groups:
        g.sort(key=lambda i: i.quit)
    return groups


def get_groups():
    groups = []
    with open(constant.PROJECT_ROOT + '/data/csv/groups.csv', 'r', encoding='utf8') as f:
        f.readline()
        for s in f:
            group_name = s.strip().split(',')[-1]
            groups.append(group_name)
    return groups


if __name__ == '__main__':
    groups = get_idols_by_group()
    for group in groups:
        print(group)
