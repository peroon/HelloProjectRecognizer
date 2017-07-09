import codecs
import json
import common


def merge():
    d = {}
    d['groups'] = common.get_groups()
    d['idols'] = common.get_idols()

    with codecs.open('./data/viewer.json', 'w', 'utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


if __name__ == '__main__':
    merge()