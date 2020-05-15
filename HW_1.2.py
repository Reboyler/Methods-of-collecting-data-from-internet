# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию через curl, Postman, Python.Ответ сервера записать в файл (приложить скриншот для Postman и curl)

# Выбрал https://plant.id/api - идентификатор растений
import requests
import json
from pprint import pprint
import base64

# преобразовываем изображение в base64
with open("unknown_plant.jpg", "rb") as file: # загрузил фотографию которую сделал сам (подснежник)
    images = [base64.b64encode(file.read()).decode("ascii")]
# получил API ключ после регистрации на сайте
your_api_key = "ugmp6mZtYlycw0tLGGtSf2FLdOzeMCATO3dp8vS7NwdhXVxJDU"
json_data = {
    "images": images,
    "modifiers": ["similar_images"],
    "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
}
# отправляю на сайт свое изображение
response = requests.post(
    "https://api.plant.id/v2/identify",
    json=json_data,
    headers={
        "Content-Type": "application/json",
        "Api-Key": your_api_key
    }).json()


for suggestion in response["suggestions"]:
    pprint(suggestion["plant_name"])    # Название растения
    pprint(suggestion["plant_details"]["common_names"])    # Общее название
    pprint(suggestion["plant_details"]["url"])    # ссылка на wikipedia

with open('answer.json','w', encoding='utf-8') as f:
    json_r = json.dump(response, f)
