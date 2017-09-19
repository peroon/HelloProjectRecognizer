import sys
import glob
import os

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QShortcut
from PyQt5.QtGui import QPixmap, QKeyEvent, QKeySequence, QCursor
from PyQt5.QtCore import Qt, QCoreApplication

from constant import RESOURCES_ROOT, PROJECT_ROOT
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
        self.youtube_id_form.set_text('0EwG_EJ7Aaw')

        # info
        self.info = Info.Info()
        self.info.setParent(self)
        self.info.move(W / 2 - 75, 450)

        self.label_buttons = LabelButtons.LabelButtons(self.__on_click_idol_button)
        self.label_buttons.setParent(self)
        self.label_buttons.move(600, 600)

        self.label_list = []

        self.show()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __on_click_idol_button(self, idol_id):
        print('idol id', idol_id)
        self.label_list[self.image_index] = idol_id

        self.image_index += 1
        self.carousel.set_index(self.image_index)
        self.info.set_image_index(self.image_index)
        self.info.set_current_label(idol_id)

    def __on_enter_youtube_id(self):
        youtube_id = self.youtube_id_form.get_text()
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
            print('no directory')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    labeling_tool = LabelingTool()
    sys.exit(app.exec_())
