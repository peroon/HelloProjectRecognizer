import glob
import shutil
import os

from constant import PROJECT_ROOT
import idol

def rename_images_sequentially(glob_dir):
    pass

def rename_face_images(idol_name):
    glob_path = PROJECT_ROOT + '/resources/face/{}/'

    pass

def move_miss_classified_images():
    idol_list = idol.get_idol_list()
    for an_idol in idol_list:
        glob_path = PROJECT_ROOT + '/resources/face/{}/not/*.jpg'.format(an_idol.directory_name)
        path_list = glob.glob(glob_path)
        for image_path in path_list:
            filename = an_idol.directory_name + os.path.basename(image_path)
            dst = PROJECT_ROOT + '/resources/face/__miss_classified/{}'.format(filename)
            shutil.move(image_path, dst)


if __name__ == '__main__':
    #rename_face_images('airi-suzuki')
    move_miss_classified_images()