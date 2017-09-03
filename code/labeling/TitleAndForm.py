import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QHBoxLayout


class TitleAndForm(QWidget):
    def __init__(self, title, on_enter_text):
        super().__init__()
        w = QWidget()
        h = QHBoxLayout()
        self.qle = QLineEdit(self)
        self.qle.returnPressed.connect(on_enter_text)
        label = QLabel(title)
        h.addWidget(self.qle)
        h.addWidget(label)
        w.setLayout(h)
        w.setParent(self)

    def get_text(self):
        t = self.qle.text()
        #self.clear_text()
        return t

    def set_text(self, s):
        self.qle.setText(s)

    def clear_text(self):
        self.set_text('')


def on_enter_text_sample():
    print('sample')


def test():
    app = QApplication(sys.argv)
    t = TitleAndForm('title', on_enter_text_sample)
    t.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()