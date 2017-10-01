import glob
import constant

def face_image_stats():
    dir_list = glob.glob(constant.RESOURCES_ROOT + '/youtube_faces/*')
    print(dir_list)
    count_list = [0] * constant.LABEL_NUM
    for dir_path in dir_list:
        for idol_id in range(constant.LABEL_NUM):
            idol_dir_path = dir_path + '/' + '%04d' % idol_id + '/*.jpg'
            face_image_list = glob.glob(idol_dir_path)
            count_list[idol_id] += len(face_image_list)

    for i, c in enumerate(count_list):
        print('idol id', i, 'count', c)
    print('total', sum(count_list))

if __name__ == '__main__':
    face_image_stats()