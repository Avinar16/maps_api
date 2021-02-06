import sys
import os
from PIL.ImageQt import ImageQt
from extra.mapapi import map_request
from PyQt5.QtGui import QPixmap


def get_map_pixmap(ll='36.15,51.72', l="map", **kwargs):
    # Запишем полученное изображение в файл.
    response_image = map_request(ll, l, **kwargs)
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            if response_image:
                file.write(response_image)
            else:
                error = open('extra\error.png', 'rb')
                file.write(error.read())
                error.close()
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

    tmp_img = ImageQt(map_file)
    pixmap = QPixmap.fromImage(tmp_img)
    os.remove(map_file)
    return pixmap
