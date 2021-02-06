import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
from extra.api_image import get_map_pixmap
from PyQt5.QtGui import QImage, QPixmap


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_map()
        self.set_connections()

    def set_connections(self):
        self.LL.textChanged.connect(self.update_map)
        self.Spn.textChanged.connect(self.update_map)

    def update_map(self):
        ll = self.LL.text()
        spn = self.Spn.text()
        filename = get_map_pixmap(ll=ll, spn=spn)
        tmp_img = QImage(filename)
        pixmap = QPixmap.fromImage(tmp_img)
        self.Image.setPixmap(pixmap)
        os.remove('map.png')

    def keyPressEvent(self, event):
        print("pressed key " + str(event.key()))
        if event.key == 16777235:
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
