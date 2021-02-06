import sys
import os
from PIL.ImageQt import ImageQt
from extra.mapapi import map_request
from PyQt5.QtGui import QPixmap


def get_map_pixmap(ll='36.15,51.72', l="map", **kwargs):
    # Запишем полученное изображение в файл.
    response_image = map_request(ll, l, **kwargs)
    map_file = "map.png"
    error_file = "extra\error.png"
    try:
        with open(map_file, "wb") as file:
            if response_image:
                file.write(response_image)
            else:
                error = open(error_file, 'rb')
                file.write(error.read())
                error.close()
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file
