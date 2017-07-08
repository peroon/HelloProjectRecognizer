def get_groups():
    groups = []
    with open('../../../data/csv/groups.csv', 'r', encoding='utf8') as f:
        f.readline()
        for s in f:
            group_name = s.strip().split(',')[-1]
            groups.append(group_name)
    return groups


def get_idols():
    idols = []
    with open('../../../data/csv/idols.csv', 'r', encoding='utf8') as f:
        f.readline()
        for s in f:
            idol = s.strip().split(',')
            idols.append(idol)
    return idols