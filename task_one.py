import requests
from bs4 import BeautifulSoup as bs


def parse(url):
    result_list = {'Номер': [], 'Начальная цена': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")

    purchases_nums = soup.find_all('div', class_='registry-entry__header-mid__number')
    purchases_prices = soup.find_all('div', class_='price-block__value')

    for num in purchases_nums:
        result_list['Номер'].append(num.text)
    for price in purchases_prices:
        result_list['Начальная цена'].append(price.text)

    return result_list
