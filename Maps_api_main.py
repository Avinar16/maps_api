import sys
import os
from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
from extra.api_image import get_map_pixmap
from PyQt5.QtGui import QImage, QPixmap
from extra.geocoder import get_coordinates, get_addres, find_businesses, get_post_code


class MyWidget(QMainWindow, Ui_MainWindow):
    left_click = QtCore.pyqtSignal()
    right_click = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.Left = False
        self.Right = False
        self.cliked = False
        self.map_size = (600, 450)
        self.result_search = None
        self.setupUi(self)
        self.Image.mousePressEvent = self.getPos
        # self.Image.mousePressEvent = self.mousePressEvent
        self.set_connections()
        self.update_map()

    def set_connections(self):
        self.LL.textChanged.connect(self.update_map)
        self.Spn.textChanged.connect(self.update_map)
        self.L.currentTextChanged.connect(self.update_map)
        self.Search_button.pressed.connect(self.Search_object)
        self.Search_button_cancel.pressed.connect(self.cancel_search)
        self.Index_check.stateChanged.connect(self.add_post_code)


    def update_map(self):
        #self.Image.mousePressEvent = self.getPos
        print('updated')
        self.ll = self.LL.text()
        l = self.L.currentText()
        self.spn = self.Spn.text()
        filename = get_map_pixmap(ll=self.ll, spn=self.spn, l=l, pt=self.get_pt(self.result_search))
        tmp_img = QImage(filename)
        self.pixmap = QPixmap.fromImage(tmp_img)
        self.Image.setPixmap(self.pixmap)
        os.remove('map.png')

    def on_click(self, pos):
        x, y = pos
        width, height = self.map_size
        # позиция клика относительно карты в пикселях
        # центр карты в пикселях
        center_x, center_y = width // 2, height // 2
        # ширина области карты в десятичных градусах
        width_spn = float(self.spn.split(',')[0])* 4
        # высота области карты в десятичных градусах
        height_spn = float(self.spn.split(',')[1])* 2
        # переводим пиксели в градусы
        one_px_x_degree = width_spn / width
        one_px_y_degree = height_spn / height
        # смещение в пикселях относительно центра
        offset_x, offset_y = center_x - x, center_y - y
        # смещение в градусах относительно центра
        offset_x_degree = offset_x * one_px_x_degree
        offset_y_degree = offset_y * one_px_y_degree
        # задаем новые координаты центра (старые -/+ смещение)
        lon = float(self.ll.split(',')[0])
        lat = float(self.ll.split(',')[1])
        new_lon, new_lat = lon - offset_x_degree, lat + offset_y_degree
        new_lon, new_lat = str(new_lon), str(new_lat)
        self.new_coords = new_lon + ',' + new_lat
        #self.LL.setText(str(self.new_coords))
        self.Search_object()


    def cancel_search(self):
        self.Search_text.setText('')
        self.result_search = None
        self.Search_result.clear()
        self.update_map()

    def get_pt(self, coords):
        if coords:
            return f"{coords},flag"

    def Search_object(self):
        if self.cliked and self.Left:
            self.Search_result.clear()
            object_coords = str(self.new_coords)
            self.result_search = object_coords
            self.adress = get_addres(object_coords)
            self.Search_result.addItem(self.adress[0])
            self.update_map()
            self.cliked = False
            self.Left = False
        elif self.cliked and self.Right:
            self.Search_result.clear()
            self.LL.setText(str(self.new_coords))
            object_coords = self.ll
            self.result_search = object_coords
            self.adress = find_businesses(object_coords, ' ',  self.Spn)
            print(self.adress)
            self.Search_result.addItem(self.adress[0])
            self.update_map()
            self.cliked = False
            self.Right = False
        else:
            self.Search_result.clear()
            self.search = self.Search_text.text()
            object_coords = get_coordinates(self.search)
            self.result_search = ','.join(map(str, object_coords))
            self.LL.setText(self.result_search)
            self.adress = get_addres(self.search)
            self.Search_result.addItem(self.adress[0])
            self.update_map()

    def add_post_code(self):
        self.Search_result.clear()
        self.Search_result.addItem(self.adress[0])
        if self.Index_check.isChecked():
            self.Search_result.addItem(get_post_code(self.adress[1]))



    def keyPressEvent(self, event):
        key = str(event.key())
        #print(key)
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



    def getPos(self, event):
        if event.button() == Qt.Qt.LeftButton:
            self.left_click.emit()
            self.Left = True
        elif event.button() == Qt.Qt.RightButton:
            self.right_click.emit()
            self.Right = True
        self.cliked = True
        x = event.pos().x()
        y = event.pos().y()
        pos_mouse = (x, y)
        self.on_click(pos_mouse)


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
