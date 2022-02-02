import tkinter as tk
from interface.styling import *
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from config import cmc_api_key
from portfolio import portfolio

portfolio_tracker = tk.Tk()
portfolio_tracker.title("Portfolio Tracker by Gitano")

name = tk.Label(portfolio_tracker, text="Coin Name", bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
name.grid(row=0, column=0, sticky="nsew")

price = tk.Label(portfolio_tracker, text="Price", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
price.grid(row=0, column=1, sticky="nsew")

no_coins = tk.Label(portfolio_tracker, text="Coin Owned", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
no_coins.grid(row=0, column=2, sticky="nsew")

amount_paid= tk.Label(portfolio_tracker, text="Total Amount Paid", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
amount_paid.grid(row=0, column=3, sticky="nsew")

current_val = tk.Label(portfolio_tracker, text="Current Value", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
current_val.grid(row=0, column=4, sticky="nsew")

pl_coin = tk.Label(portfolio_tracker, text="P/L per coin", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
pl_coin.grid(row=0, column=5, sticky="nsew")

totalpl = tk.Label(portfolio_tracker, text="Total P/L With Coin", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT,)
totalpl.grid(row=0, column=6, sticky="nsew")


portfolio_tracker.mainloop()

'''
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
'''
