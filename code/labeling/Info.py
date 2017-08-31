import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QHBoxLayout


class Info(QWidget):
    def __init__(self):
        super().__init__()

    def test(self):
        self.show()

def test():
    app = QApplication(sys.argv)
    info = Info()
    info.test()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()