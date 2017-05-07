import os

import idol
from constant import PROJECT_ROOT

def make_candidate_directory():
    lst = idol.get_idol_list()
    for an_idol in lst:
        path = PROJECT_ROOT + '/resources/face/{}/candidates'.format(an_idol.directory_name)
        os.makedirs(path, exist_ok=True)
    pass

if __name__ == '__main__':
    make_candidate_directory()