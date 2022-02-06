import tkinter as tk
import logging

from connectors.binance import BinanceClient
from connectors.kraken import KrakenClient
from connectors.celsius import CelsiusClient

from portfolio import *

from interface.root_component import Root


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from config import cmc_api_key
from portfolio import portfolio


if __name__ == '__main__':
    binance = BinanceClient(binance_keys['pub'], binance_keys['sec'])
    kraken = KrakenClient(kraken_keys['pub'], kraken_keys['sec'])
    celsius = CelsiusClient(celsius_keys['pub'], celsius_keys['sec'])

    available_exchanges = [binance, kraken, celsius]

    for exchange in available_exchanges:
        for asset in exchange.balances.values():
            print(f"{exchange.name} / {asset.asset}: {asset.balance}")

    root = Root(binance, kraken, celsius)
    root.mainloop()


