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

        btn1 = QPushButton('', self)
        btn1.move(30, 50)
        btn1.setFixedSize(200, 200)
        btn1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        icon_path = constant.PROJECT_ROOT + '/docs/images/face_icon/0000.jpg'
        btn1.setIcon(QIcon(icon_path))
        btn1.setIconSize(QSize(180, 180))

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(lambda: self.on_press_button(1))
        btn2.clicked.connect(self.on_press_button)

        vertical.addWidget(btn1)
        vertical.addWidget(btn2)

        self.setLayout(vertical)

    def on_press_button(self, idol_id):
        sender = self.sender()
        print(idol_id)


def test():
    app = QApplication(sys.argv)
    t = LabelButtons()
    t.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()
