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
        self.L.currentTextChanged.connect(self.update_map)

    def update_map(self):
        print('updated')
        self.ll = self.LL.text()
        l = self.L.currentText()
        self.spn = self.Spn.text()
        filename = get_map_pixmap(ll=self.ll, spn=self.spn, l=l)
        tmp_img = QImage(filename)
        pixmap = QPixmap.fromImage(tmp_img)
        self.Image.setPixmap(pixmap)
        os.remove('map.png')

    def keyPressEvent(self, event):
        key = str(event.key())
        print(key)
        if key in ['16777238', '16777239']:
            self.spn_changer(key)
        elif key in ['16777234', '16777235', '16777236', '16777237']:
            self.coord_changer(key)
    # map movement
    def coord_changer(self, key):
        spn_split = self.spn.split(',')
        ll_split = self.ll.split(',')
        print(ll_split)
        new_x = float(ll_split[0])
        new_y = float(ll_split[1])
        # move left
        if key == '16777234':
            new_x = float(ll_split[0]) - float(spn_split[0]) * 2
        elif key == '16777236':
            new_x = float(ll_split[0]) + float(spn_split[0]) * 2
        elif key == '16777235':
            new_y = float(ll_split[1]) + float(spn_split[0]) * 0.9
        elif key == '16777237':
            new_y = float(ll_split[1]) - float(spn_split[0]) * 0.9
        coord = [str(new_x), str(new_y)]
        new_coord = ','.join(list(map(str, coord)))
        self.LL.setText(new_coord)


    def spn_changer(self, key, k=2):
        # pg up
        spn_split = self.spn.split(',')
        print(spn_split)
        if key == '16777238':
            spn_split = list((map(lambda x: float(x) / k, spn_split)))
        # pg down
        elif key == '16777239':
            spn_split = list((map(lambda x: float(x) * k, spn_split)))

        # spn limit
        if spn_split[0] > 85:
            spn_split[0] = 85
        if spn_split[1] > 85:
            spn_split[1] = 85
        # result
        self.spn = ','.join(list(map(str, spn_split)))

        self.Spn.setText(self.spn)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
