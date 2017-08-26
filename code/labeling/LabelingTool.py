import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
import glob

from constant import RESOURCES_ROOT
import Carousel

W = 1000
H = 800


class LabelingTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.resize(W, H)
        self.center()
        self.youtube_id_form()
        self.setWindowTitle('Labeling Tool')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def youtube_id_form(self):
        self.qle = QLineEdit(self)
        self.qle.returnPressed.connect(self.on_enter_youtube_id)

    def on_enter_youtube_id(self):
        youtube_id = self.qle.text()
        print('entered', youtube_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    labeling_tool = LabelingTool()

    carousel = Carousel.Carousel()
    carousel.setParent(labeling_tool)
    carousel.test()

    sys.exit(app.exec_())