import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QHBoxLayout, QPushButton


class LabelButtons(QWidget):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
        btn1.clicked.connect(self.on_press_button)
        btn2.clicked.connect(self.on_press_button)

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
