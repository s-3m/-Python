from requests import get, utils
from datetime import date

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


# qwertyejkjekjwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww



def currency_rates(currency):
    currency_in_content = content[content.find(currency):content.find(currency)+3]
    date_lst  = content[content.find('Date')+6:content.find('Date')+16].split('.')
    date_now  = date(int(date_lst[2]), int(date_lst[1]), int(date_lst[0]))
    if currency == currency_in_content:
        currency_str = content[content.find(currency)+40:content.find(currency)+90]
        value_str = ''
        for i in currency_str:
            if i.isdigit():
                value_str = value_str + i
        print(f'{currency} по курсу ЦБ на {date_now} -  {float(value_str) / 10000} руб.')
    else:
        print('Введите верный код валюты.')

user_value = input('Введите код валюты: ')
currency_rates(user_value.upper())