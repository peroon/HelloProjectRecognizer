import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


import constant
import idol

IMAGE_BUTTON_SIZE = 200


class LabelButtons(QWidget):
    def __init__(self, on_click_button):
        super().__init__()

        horizontal = QHBoxLayout()

        groups = idol.get_idols_by_group()
        for group in groups:
            print('group', group)
            vertical = QVBoxLayout()
            for an_idol in group:
                btn = self.__get_image_button(an_idol.idol_id)
                btn.setToolTip(an_idol.name)
                btn.clicked.connect(lambda state, ii=an_idol.idol_id: on_click_button(ii))
                vertical.addWidget(btn)
            horizontal.addLayout(vertical)

        # other label button
        vertical = QVBoxLayout()
        btn = self.__get_image_button(-1)
        btn.clicked.connect(lambda state, ii=-1: on_click_button(ii))
        vertical.addWidget(btn)
        horizontal.addLayout(vertical)

        self.setLayout(horizontal)

    def __get_image_button(self, idol_id):
        btn = QPushButton('', self)
        btn.setFixedSize(80, 80)
        icon_path = constant.PROJECT_ROOT + '/docs/images/face_icon/' + '{0:04d}'.format(idol_id) + '.jpg'
        btn.setIcon(QIcon(icon_path))
        btn.setIconSize(QSize(75, 75))
        return btn


def on_click_button_sample(idol_id):
    print('sample', idol_id)


def test():
    app = QApplication(sys.argv)
    t = LabelButtons(on_click_button_sample)
    t.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test()
