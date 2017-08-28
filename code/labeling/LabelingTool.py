import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap
import glob

from constant import RESOURCES_ROOT
import Carousel

W = 224 * 5
H = 800
WINDOW_NAME = 'Labeling Tool'

class LabelingTool(QWidget):
    def __init__(self):
        super().__init__()
        self.image_index = 0
        self.initialize_ui()

        # add carousel
        self.carousel = Carousel.Carousel()
        self.carousel.setParent(self)
        self.carousel.move(0, 25)
        self.carousel.test()

        # info
        self.w = QWidget()
        index_title = QLabel('image index:')
        self.index_label = QLabel('0')
        hbox = QHBoxLayout()
        hbox.addWidget(index_title)
        hbox.addWidget(self.index_label)
        self.w.setLayout(hbox)
        self.w.move(0, 275)
        self.w.setParent(self)

        self.show()

    def initialize_ui(self):
        self.resize(W, H)
        self.center()
        self.youtube_id_form()
        self.tag_input_form()
        self.setWindowTitle(WINDOW_NAME)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def youtube_id_form(self):
        self.qle = QLineEdit(self)
        self.qle.returnPressed.connect(self.__on_enter_youtube_id)

    def __on_enter_youtube_id(self):
        youtube_id = self.qle.text()
        print('entered', youtube_id)

    def tag_input_form(self):
        w = QWidget()
        horizontal = QHBoxLayout()
        self.tag_form = QLineEdit()
        self.tag_form.returnPressed.connect(self.__on_enter_tag)
        title = QLabel('tag input')
        horizontal.addWidget(self.tag_form)
        horizontal.addWidget(title)
        w.setLayout(horizontal)
        w.move(0, 24 + 224)
        w.setParent(self)

    def __get_idol_tag_list(self):
        return ['ym', 'ns']  # temporary

    def __on_enter_tag(self):
        tag = self.tag_form.text()
        self.tag_form.setText('')
        tag_list = self.__get_idol_tag_list()
        if tag in tag_list:
            tag_index = tag_list.index(tag)
            print(tag_index)
            # TODO labeling
            self.image_index += 1
            # update carousel
            self.carousel.set_index(self.image_index)
            self.index_label.setText(str(self.image_index))
        else:
            print('no tag')
        print('tag is', tag)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    labeling_tool = LabelingTool()
    sys.exit(app.exec_())