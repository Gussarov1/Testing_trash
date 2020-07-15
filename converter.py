import json

import requests

currencies = ['USD', 'EUR', 'GBP']


def get_course(currency):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = json.loads(response.text)['Valute']
    return data[currency]['Value']


def convert(currencies, value):
    print('\nРезультат: {0}'.format(int(value * float(get_course(currencies)))))


def start():
    result = 'Выбери ID валюты\n'
    for i in range(len(currencies)):
        result += ('ID: {0}  Валюта:{1}\n'.format(i, currencies[i]))
    print(result)
    id_currencies = int(input())
    print('\nВведи число:\n')
    value = int(input())
    convert(currencies[id_currencies], value)
