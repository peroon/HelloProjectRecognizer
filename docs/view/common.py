import constant


def get_groups():
    groups = []
    with open(constant.PROJECT_ROOT + '/data/csv/groups.csv', 'r', encoding='utf8') as f:
        f.readline()
        for s in f:
            group_name = s.strip().split(',')[-1]
            groups.append(group_name)
    return groups


def get_idols():
    idols = []
    with open(constant.PROJECT_ROOT + '/data/csv/idols.csv', 'r', encoding='utf8') as f:
        f.readline()
        for s in f:
            idol = s.strip().split(',')
            idols.append(idol)
    return idols


if __name__ == '__main__':
    # test
    print(get_groups())
    print(get_idols())