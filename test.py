from connectors.BinanceClient import BinanceClient
from connectors.KrakenClient import KrakenClient
from connectors.CelsiusClient import CelsiusClient
from portfolio import binance_keys, kraken_keys, celsius_keys, lykke_key
import requests
import logging
logger = logging.getLogger()

'''
binance = BinanceClient(binance_keys['pub'], binance_keys['sec'])

print(binance.balances)

for asset in binance.balances.values():
    print(f"{asset.asset}: {asset.balance}")


kraken = KrakenClient(kraken_keys['pub'], kraken_keys['sec'])

kraken.get_balances()
'''
celsius = CelsiusClient(celsius_keys['pub'], celsius_keys['sec'])
for asset in celsius.balances.values():
    print(f"{asset.asset}: {asset.balance}")
