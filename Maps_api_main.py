import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
from extra.api_image import get_map_pixmap


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
        print('map updated')
        ll = self.LL.text()
        spn = self.Spn.text()
        self.Image.setPixmap(get_map_pixmap(ll=ll, spn=spn))

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
