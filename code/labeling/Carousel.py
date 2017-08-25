import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap

SHOW_IMAGE_NUM = 5


class Carousel(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path_list = None
        self.label_list = []
        for i in range(SHOW_IMAGE_NUM):
            self.label_list.append(QLabel(self))
            self.label_list[i].setGeometry(i * 224, 0, 224, 224)

    def show(self):
        self.resize(1000, 1000)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setWindowTitle('Center')
        self.show()

    def set_image_path_list(self, lst):
        self.image_path_list = lst

    def set_index(self, index):
        for i in range(SHOW_IMAGE_NUM):
            idx = index + i
            if idx >= len(self.image_path_list):
                idx -= len(self.image_path_list)
            pixmap = QPixmap(self.image_path_list[idx])
            self.label_list[i] = QLabel(self)
            self.lbl.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Carousel()
    sys.exit(app.exec_())