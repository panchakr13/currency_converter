import requests
from bs4 import BeautifulSoup


def html():
    url = 'https://minfin.com.ua/currency/banks/'
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, 'html.parser')
    table = soup.findAll('td', {'class': 'mfm-text-nowrap'})
    return table


def USD(operation):
    table = html()
    usd = list(table)[0].text.split()
    buy_usd = float(usd[0])
    sell_usd = float(usd[-1])

    if operation == 'buy':
        return buy_usd
    elif operation == 'sell':
        return sell_usd
    elif operation == 'currency':
        print(f'Купить: {buy_usd}', f'Продать: {sell_usd}', sep='\n')


def EUR(operation):
    table = html()
    eur = list(table)[2].text.split()
    buy_eur = float(eur[0])
    sell_eur = float(eur[-1])

    if operation == 'buy':
        return buy_eur
    elif operation == 'sell':
        return sell_eur
    elif operation == 'currency':
        print(f'Купить: {buy_eur}', f'Продать: {sell_eur}', sep='\n')



def PLN(operation):
    table = html()
    pln = list(table)[4].text.split()
    buy_pln = float(pln[0])
    sell_pln = float(pln[-1])

    if operation == 'buy':
        return buy_pln
    elif operation == 'sell':
        return sell_pln
    elif operation == 'currency':
        print(f'Купить: {buy_pln}', f'Продать: {sell_pln}', sep='\n')


def CZK(operation):
    table = html()
    czk = list(table)[18].text.split()
    buy_czk = float(czk[0])
    sell_czk = float(czk[-1])

    if operation == 'buy':
        return buy_czk
    elif operation == 'sell':
        return sell_czk
    elif operation == 'currency':
        print(f'Купить: {buy_czk}', f'Продать: {sell_czk}', sep='\n')


def converter():
    while True:
        amount = input('''Какую сумму денег желаете конвертировать?
>>> ''')
        if amount.isdigit() and int(amount) > 0:
            break
        print('Неверный ввод данных. Попробуйте ещё раз!')

    while True:
        currency = input('''Из какой валюты вы хотите выполнить конвертацию? 
(1 - USD / 2 - EUR / 3 - PLN / 4 - CZK)
>>> ''')
        if currency.isdigit() and 1 <= int(currency) <= 4:
            break
        print('Неверный ввод данных. Попробуйте ещё раз!')

    titles = {1: 'USD', 2: 'EUR', 3: 'PLN', 4: 'CZK'}

    currency_dict = {titles[1]: USD('buy'), titles[2]: EUR('buy'),
                     titles[3]: PLN('buy'), titles[4]: CZK('buy')}

    print(f'У вас есть {amount} {titles[int(currency)]}. '
          f'Вы получите {int(amount) * currency_dict[titles[int(currency)]]}'
          f' UAH')


def user():
    print('*' * 5 + ' Конвертер валют ' + '*' * 5)
    print()
    print('''Какую операцию желаете выполнить? 
1 - Конвертация валют
2 - Курс валют к гривне''')

    while True:
        user_operations = input('>>> ')
        if user_operations == '1' or user_operations == '2':
            break
        print('Неверный ввод данных. Попробуйте ещё раз!')

    if user_operations == '1':
        converter()
    elif user_operations == '2':
        print('Актуальный курс на сегодня:')
        print('USD to UAH:')
        USD('currency')
        print('EUR to UAH:')
        EUR('currency')
        print('PLN to UAH:')
        PLN('currency')
        print('CZK to UAH:')
        CZK('currency')


user()