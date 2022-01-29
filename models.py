class Balance:
    def __init__(self, info, exchange):
        print(info)
        if exchange == "binance":
            self.asset = info['asset']
            self.balance = float(info['free'])
