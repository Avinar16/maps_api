import requests
import json


def geocoder_request(geocode):
    apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
    format = "json"
    url = f"http://geocode-maps.yandex.ru/1.x/?apikey=%7Bapikey%7D&geocode=%7Bgeocode%7D&format=%7Bformat%7D"
    response = requests.get(url)
    if response:
        json_response = response.json()
        return json_response
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
    return False


def save_to_file(obj, filename="test.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)


response = geocoder_request("Петровка, 38")
save_to_file(response)
toponym = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]
print("Почтовый индекс:", address["postal_code"])