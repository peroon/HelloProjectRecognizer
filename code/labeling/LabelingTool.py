import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QShortcut
from PyQt5.QtGui import QPixmap, QKeyEvent, QKeySequence
from PyQt5.QtCore import Qt, QCoreApplication
import glob

from constant import RESOURCES_ROOT
import Carousel
import TitleAndForm
import Info

W = 1900
H = 1200
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

        # tag form
        self.tag_form = TitleAndForm.TitleAndForm('tag', self.__on_enter_tag)
        self.tag_form.setParent(self)
        self.tag_form.move(0, 450)

        # info
        self.info = Info.Info()
        self.info.setParent(self)
        self.info.move(0, 500)

        self.show()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            print('esc')
            QCoreApplication.quit()
        elif key == Qt.RightArroww:
            print('->')
        elif key == Qt.LeftArrow:
            print('<-')

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __on_enter_youtube_id(self):
        youtube_id = self.youtube_id_form.get_text()
        print('entered', youtube_id)

    def __get_idol_tag_list(self):
        return ['ym', 'ns']  # temporary

    def __on_enter_tag(self):
        tag = self.tag_form.get_text()
        tag_list = self.__get_idol_tag_list()
        if tag in tag_list:
            tag_index = tag_list.index(tag)
            print(tag_index)
            # TODO labeling
            self.image_index += 1
            self.carousel.set_index(self.image_index)
            self.info.set_image_index(self.image_index)
        else:
            print('no tag')
        print('tag is', tag)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    labeling_tool = LabelingTool()
    sys.exit(app.exec_())
