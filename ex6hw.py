import json
import re
import requests
import pandas as pd


api_key='24354461118e1e1008052182d218efd2b1d18e751c3e9faaf7db1cf96faa45b236fd01120c67fb7cfbb84'
response = requests.get("https://api.vk.com/method/friends.get?count=125&fields=city&access_token=24354461118e1e1008052182d218efd2b1d18e751c3e9faaf7db1cf96faa45b236fd01120c67fb7cfbb84&v=5.131")
print('Part 1')
print()
print(response)
print(response.text)
print(response.headers)
print(response.url)
print(response.status_code)
print(response.headers.get('Content-Type'))
print(response.json()['response']['items'][1]['id'])
try:
    for i in range(1, 5):
        r = requests.get(f'https://api.vk.com/method/friends.get?fields=city&access_token=24354461118e1e1008052182d218efd2b1d18e751c3e9faaf7db1cf96faa45b236fd01120c67fb7cfbb84&v=5.131')
        print(i, r.json()['response']['items'][i]['id'], r.json()['response']['items'][i]['first_name'],  r.json()['response']['items'][i]['last_name'])
except:
    print('Нет больше друзей')

