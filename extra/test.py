import  pygame
import  requests
import  os
import sys

def geocoder_request(geocode):
    apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
    format = "json"
    url = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={geocode}&format={format}"
    response = requests.get(url)
    if response:
        json_response = response.json()
        return json_response
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
    return False


def get_cords(json_response):
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coodrinates = toponym["Point"]["pos"]
    return ",".join(toponym_coodrinates.split(' '))


def get_pt(cords):
    return f"{cords},flag"


def print_map(ll="37.615486%2C55.740755", l="map", spn="0.2,0.2", pt=False):
    if pt:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&l={l}&spn={spn}&pt={pt}"
    else:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&l={l}&spn={spn}"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_file)


stadiums = ["Лужники", "Спартак", "Динамо"]
pt = []
for i in range(3):
    pt.append(get_pt(get_cords(geocoder_request(stadiums[i]))))

pt[1] = get_pt('37.440336%2C55.817803')

print_map(pt='~'.join(pt))