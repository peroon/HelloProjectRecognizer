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
        self.initUI()

    def initUI(self):
        self.resize(W, H)
        self.center()
        self.youtube_id_form()

        self.pixmap = QPixmap(RESOURCES_ROOT + "/face_224x224/airi-suzuki/ok/0002.jpg")
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.setGeometry(100, 100, 224, 224)

        self.setWindowTitle('Center')
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
    image_path_list = glob.glob(RESOURCES_ROOT + '/face_224x224/airi-suzuki/ok/*.jpg')
    carousel.set_image_path_list(image_path_list)
    carousel.setParent(labeling_tool)

    sys.exit(app.exec_())