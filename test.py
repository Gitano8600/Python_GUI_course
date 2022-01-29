from connectors.BinanceClient import BinanceClient
from connectors.KrakenClient import KrakenClient
from portfolio import binance_keys, kraken_keys

'''
binance = BinanceClient(binance_keys['pub'], binance_keys['sec'])

print(binance.balances)

for asset in binance.balances.values():
    print(f"{asset.asset}: {asset.balance}")
'''

kraken = KrakenClient(kraken_keys['pub'], kraken_keys['sec'])

kraken.get_balances()
