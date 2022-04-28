import requests
from datetime import datetime


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    list_rates = content.split('<Valute ')
    code = code.upper()
    valute = []
    value = 'Value'
    if code == '':
        return None
    for exchange_rate in list_rates:
        e_r = exchange_rate.split('><')
        for val in e_r:
            if val[9:12] == code:
                valute = val[9:12]
            if val[0:5] == value and valute == code:
                value = val.lstrip('Value>')
                value = value.rsplit('</Value')
    if code != valute:
        return None
    value = value[0].split(',')
    value = '.'.join(value)
    result_value = f'{value}'
    return result_value


def currency_rates_adv(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    list_rates = content.split('<Valute ')
    code = code.upper()
    valute = []
    curs_date = 'ValCurs Date'
    value = 'Value'
    for exchange_rate in list_rates:
        e_r = exchange_rate.split('><')
        for val in e_r:
            if val[:12] == curs_date:
                curs_date = val[14:24]
            if val[9:12] == code:
                valute = val[9:12]
            if val[0:5] == value and valute == code:
                value = val.lstrip('Value>')
                value = value.rsplit('</Value')
    if code != valute:
        return None
    value = value[0].split(',')
    value = '.'.join(value)
    curs_date = curs_date.split('.')
    curs_date = datetime(year=int(curs_date[2]), month=int(curs_date[1]), day=int(curs_date[0]))
    result_value = f'{value}, {curs_date}'
    return result_value


if __name__ == '__main__':
    currency_rates(None)
