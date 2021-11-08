import sys
import main


def term(argv):
    print(main.currency_rates(argv))


coin = input('Введите валюту: ')

term(coin)
