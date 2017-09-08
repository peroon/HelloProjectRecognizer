import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QLayout

IMAGE_BUTTON_SIZE = 200


class LabelButtons(QWidget):
    def __init__(self):
        super().__init__()

        vertical = QVBoxLayout()

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn1.resize(200, 200)
        btn1.setFixedSize(200, 200)
        btn1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.on_press_button)
        btn2.clicked.connect(self.on_press_button)

        #vertical.setSizeConstraint(QLayout.SetFixedSize)
        vertical.addWidget(btn1)
        vertical.addWidget(btn2)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(vertical)

    def on_press_button(self):
        sender = self.sender()
        print(sender.text())


def test():
    app = QApplication(sys.argv)
    t = LabelButtons()
    t.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()
