import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
import glob

from constant import RESOURCES_ROOT
SHOW_IMAGE_NUM = 5
FACE_IMAGE_SIZE = 224


class Carousel(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path_list = None
        self.label_list = []
        for i in range(SHOW_IMAGE_NUM):
            self.label_list.append(QLabel(self))
            self.label_list[i].setGeometry(i * FACE_IMAGE_SIZE, 0, FACE_IMAGE_SIZE, FACE_IMAGE_SIZE)

    def set_image_path_list(self, lst):
        self.image_path_list = lst

    def set_index(self, index):
        for i in range(SHOW_IMAGE_NUM):
            idx = index + i
            if idx >= len(self.image_path_list):
                idx -= len(self.image_path_list)
            pixmap = QPixmap(self.image_path_list[idx])
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