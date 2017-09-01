import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QHBoxLayout


class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.__get_youtube_id_form()
        self.show()

    def __get_youtube_id_form(self):
        w = QWidget()
        h = QHBoxLayout()
        self.youtube_id_form = QLineEdit(self)
        self.youtube_id_form.returnPressed.connect(self.__on_enter_youtube_id)
        label = QLabel('youtube id')
        h.addWidget(self.youtube_id_form)
        h.addWidget(label)
        w.setLayout(h)
        w.setParent(self)

    def __on_enter_youtube_id(self):
        youtube_id = self.youtube_id_form.text()
        print('entered', youtube_id)

    def test(self):
        self.show()


def test():
    app = QApplication(sys.argv)
    info = Info()
    info.test()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()