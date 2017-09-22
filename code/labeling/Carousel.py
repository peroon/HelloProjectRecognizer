"""Show images in a row"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
import glob

from constant import RESOURCES_ROOT
SHOW_IMAGE_NUM = 7
FACE_IMAGE_SIZE = 224


class Carousel(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path_list = None
        self.label_list = []
        horizontal = QHBoxLayout()
        for i in range(SHOW_IMAGE_NUM):
            label = QLabel(self)
            size = FACE_IMAGE_SIZE + 100
            label.resize(size, size)
            self.label_list.append(label)
            horizontal.addWidget(label)
        self.setLayout(horizontal)

    def set_image_path_list(self, lst):
        self.image_path_list = lst

    def set_index(self, index):
        for i in range(SHOW_IMAGE_NUM):
            image_index = index + i
            while image_index >= len(self.image_path_list):
                image_index -= len(self.image_path_list)
            print(len(self.image_path_list), image_index)
            path = self.image_path_list[image_index]
            pixmap = QPixmap(path)
            pixmap = pixmap.scaledToWidth(FACE_IMAGE_SIZE)

            # center image size
            if i == SHOW_IMAGE_NUM // 2:
                pixmap = pixmap.scaledToWidth(FACE_IMAGE_SIZE * 2)
            self.label_list[i].setPixmap(pixmap)

    def test(self):
        image_path_list = glob.glob(RESOURCES_ROOT + '/face_224x224/airi-suzuki/ok/*.jpg')
        self.set_image_path_list(image_path_list)
        self.set_index(0)
        self.show()


def test():
    app = QApplication(sys.argv)
    carousel = Carousel()
    carousel.test()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()
