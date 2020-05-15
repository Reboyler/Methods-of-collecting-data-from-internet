#Основы клиент-серверного взаимодействия. Парсинг API
#Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
import requests
import json
from pprint import pprint
url = 'https://api.github.com'
user = 'Reboyler'
r = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(r.json(), f)
for i in r.json():
    pprint(i['name'])
    #print(i['name'])

