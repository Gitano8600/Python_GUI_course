from portfolio import bc_data
from connectors.bc import BcConnector
import requests
import logging
logger = logging.getLogger()


bc_instance = BcConnector(bc_data)

for asset in bc_instance.balances.values():
    print(f"{asset.asset}: {asset.balance}")

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