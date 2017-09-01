import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout


class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout()

        self.image_index_label = self.__create_title_and_label('image index')
        self.current_tag_label = self.__create_title_and_label('current tag')

        self.setLayout(self.vertical_layout)

    def set_image_index(self, index):
        self.image_index_label.setText(str(index))

    def set_current_tag(self, tag_name):
        self.current_tag_label.setText(tag_name)

    def __create_title_and_label(self, title):
        w = QWidget()
        h = QHBoxLayout()
        label = QLabel(self)
        title = QLabel(title)
        h.addWidget(title)
        h.addWidget(label)
        w.setLayout(h)
        w.setParent(self)
        self.vertical_layout.addWidget(w)
        return label


def test():
    app = QApplication(sys.argv)
    info = Info()
    info.set_image_index(123)
    info.set_current_tag('tag')
    info.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()