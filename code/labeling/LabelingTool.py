import sys
import glob
import os
import shutil

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton

from constant import RESOURCES_ROOT
import Carousel
import TitleAndForm
import Info
import LabelButtons

W = 1900
H = 1900
DEBUG = False
WINDOW_NAME = 'Labeling Tool'


class LabelingTool(QWidget):
    def __init__(self):
        super().__init__()
        self.image_index = 0
        self.resize(W, H)
        self.__center()
        self.setWindowTitle(WINDOW_NAME)

        # add carousel
        self.carousel = Carousel.Carousel()
        self.carousel.setParent(self)
        self.carousel.test()

        # youtube id form
        self.youtube_id_form = TitleAndForm.TitleAndForm('youtube id', self.__on_enter_youtube_id)
        self.youtube_id_form.setParent(self)
        self.youtube_id_form.move(0, 400)
        youtube_id_sample = '_sample'
        #youtube_id_sample = '0EwG_EJ7Aaw'

        self.youtube_id_form.set_text(youtube_id_sample)

        # info
        self.info = Info.Info()
        self.info.setParent(self)
        self.info.move(W / 2 - 75, 450)

        # next button
        next_button = QPushButton('next', self)
        next_button.setFixedSize(80, 80)
        next_button.clicked.connect(self.__next)
        next_button.move(1200, 500)

        # prev button
        next_button = QPushButton('prev', self)
        next_button.setFixedSize(80, 80)
        next_button.clicked.connect(self.__prev)
        next_button.move(600, 500)

        # move button
        move_button = QPushButton('move', self)
        move_button.setFixedSize(80, 80)
        move_button.clicked.connect(self.__move)
        move_button.move(1600, 500)

        self.label_buttons = LabelButtons.LabelButtons(self.__on_click_idol_button)
        self.label_buttons.setParent(self)
        self.label_buttons.move(600, 600)

        self.label_list = []
        self.image_num = 0

        self.__update_by_youtube_id(youtube_id_sample)
        self.show()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __on_click_idol_button(self, idol_id):
        print('idol id', idol_id)
        self.label_list[self.image_index] = idol_id
        self.info.set_labeled_num(self.__get_labeled_num())
        self.__next()

    def __get_labeled_num(self):
        return sum(1 for i in self.label_list if i is not None)

    def __next(self):
        self.image_index += 1
        if self.image_index >= self.image_num:
            self.image_index -= self.image_num
        self.__update_by_index()

    def __prev(self):
        self.image_index -= 1
        if self.image_index < 0:
            self.image_index += self.image_num
        self.__update_by_index()

    def __move(self):
        if self.image_num == self.__get_labeled_num():
            print('Done! I move images.')
            for i, path in enumerate(self.carousel.image_path_list):
                label = self.label_list[i]
                mv_dir = os.path.dirname(path) + '/' + '%04d' % label
                print('index', i, 'label', label)
                if not os.path.exists(mv_dir):
                    os.mkdir(mv_dir)
                dst = mv_dir + '/' + os.path.basename(path)
                if DEBUG:
                    shutil.copyfile(path, dst)
                else:
                    shutil.move(path, dst)
        else:
            print('unlabeled images exist...')

    def __update_by_index(self):
        self.carousel.set_index(self.image_index)
        self.info.set_image_index(self.image_index)
        self.info.set_current_label(self.label_list[self.image_index])

    def __on_enter_youtube_id(self):
        youtube_id = self.youtube_id_form.get_text()
        self.__update_by_youtube_id(youtube_id)

    def __update_by_youtube_id(self, youtube_id):
        print('youtube id entered.', youtube_id)
        faces_dir = RESOURCES_ROOT + '/youtube_faces/' + youtube_id
        if os.path.isdir(faces_dir):
            print('dir exist')
            face_image_path_list = glob.glob(faces_dir + '/*.jpg')
            self.carousel.set_image_path_list(face_image_path_list)
            self.image_index = 0
            self.carousel.set_index(self.image_index)

            self.image_num = len(face_image_path_list)

            self.info.set_image_index(self.image_index)
            self.info.set_image_num(self.image_num)
            self.info.set_current_label(None)

            self.label_list = [None] * self.image_num
        else:
            print('There is no directory.', faces_dir)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    labeling_tool = LabelingTool()
    sys.exit(app.exec_())
