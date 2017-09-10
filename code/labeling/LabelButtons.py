import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QSizePolicy, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


import constant

IMAGE_BUTTON_SIZE = 200


class LabelButtons(QWidget):
    def __init__(self):
        super().__init__()

        vertical = QVBoxLayout()
        btn0 = self.__get_image_button(0)
        btn1 = self.__get_image_button(1)

        btn0.clicked.connect(lambda: self.on_press_button(0))
        btn1.clicked.connect(lambda: self.on_press_button(1))

        vertical.addWidget(btn0)
        vertical.addWidget(btn1)

        self.setLayout(vertical)

    def __get_image_button(self, idol_id):
        btn1 = QPushButton('', self)
        btn1.setFixedSize(200, 200)
        icon_path = constant.PROJECT_ROOT + '/docs/images/face_icon/' + '{0:04d}'.format(idol_id) + '.jpg'
        btn1.setIcon(QIcon(icon_path))
        btn1.setIconSize(QSize(180, 180))
        return btn1

    def on_press_button(self, idol_id):
        print(idol_id)


def test():
    app = QApplication(sys.argv)
    t = LabelButtons()
    t.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()
