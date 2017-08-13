import os


def get_key(file_name):
    path = os.path.dirname(__file__) + r'/../secret/' + file_name
    with open(path, 'r') as f:
        s = f.readline()
    return s


if __name__ == '__main__':
    # test
    print(get_key('bing_api_key'))