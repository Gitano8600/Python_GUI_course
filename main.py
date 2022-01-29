import tkinter as tk
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from config import cmc_api_key
from portfolio import portfolio

portfolio_tracker = tk.Tk()
portfolio_tracker.title("Portfolio Tracker by Gitano")

name = tk.Label(portfolio_tracker, text="Bitcoin", bg="brown",fg="white")
name.grid(row=0, column=0)
portfolio_tracker.mainloop()


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1000',
  'convert':'CHF'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': cmc_api_key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

total_value = 0
for i in data['data']:
    for coin in portfolio:
        if i['symbol'] == coin['symbol']:
            print(i['symbol'])
            print('{0:.2f}'.format(i['quote']['CHF']['price']))
            cur_pos_value = round(coin["amount_owned"] * float(i["quote"]["CHF"]["price"]), 2)
            total_value += cur_pos_value
            print(f'TOTAL CHF VALUE = {cur_pos_value}')
            print('-----------------------')

print(f'FINAL VALUE = {total_value}')