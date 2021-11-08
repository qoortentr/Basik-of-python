import requests
from requests import get


def currency_rates(coin):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    for el in content.split(f'{coin}')[1:]:
        return f'1 {coin} = ' + el.split('</Value>')[0][-7:] + ' RUB' + ' на момент ' + response.headers['date']


currency_u = currency_rates('USD')
currency_e = currency_rates('EUR')

if __name__ == '__main__':
    print(currency_e)
    print(currency_u)
