import pandas as pd
import requests

from task_one import parse

URL_TEMPLATE = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html"
FILE_NAME = "purchases.csv"

# Task 1
if requests.get(URL_TEMPLATE).status_code == 200:
    df = pd.DataFrame(data=parse(URL_TEMPLATE))
    df.to_csv(FILE_NAME)
else:
    print("Status code is not equal 200 — problem in loading site")
