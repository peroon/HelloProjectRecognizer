import sys
import glob
import os

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton

from constant import RESOURCES_ROOT
import Carousel
import TitleAndForm
import Info
import LabelButtons

W = 1900
H = 1900
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
        youtube_id_sample = '0EwG_EJ7Aaw'
        self.youtube_id_form.set_text(youtube_id_sample)

        # info
        self.info = Info.Info()
        self.info.setParent(self)
        self.info.move(W / 2 - 75, 450)

        # next and prev button
        next_button = QPushButton('next', self)
        next_button.setFixedSize(80, 80)
        next_button.clicked.connect(self.__next)
        next_button.move(500, 500)

        self.label_buttons = LabelButtons.LabelButtons(self.__on_click_idol_button)
        self.label_buttons.setParent(self)
        self.label_buttons.move(600, 600)

        self.label_list = []

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
        self.__next()

    def __next(self):
        self.image_index += 1
        self.__update_by_index()

    def __prev(self):
        self.image_index -= 1
        self.__update_by_index()

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

            self.info.set_image_index(self.image_index)
            self.info.set_image_num(len(face_image_path_list))
            self.info.set_current_label(str(None))

            self.label_list = [None] * len(face_image_path_list)
        else:
            print('There is no directory.', faces_dir)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    labeling_tool = LabelingTool()
    sys.exit(app.exec_())
