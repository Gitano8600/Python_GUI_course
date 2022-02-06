class Balance:
    def __init__(self, info, exchange):
        if exchange == "binance":
            self.asset = info['asset']
            self.balance = float(info['free'])

        elif exchange == "kraken":
            self.asset = info[0]
            self.balance = info[1]

        elif exchange == "celsius":
            self.asset = info[0]
            self.balance = info[1]

        elif exchange == "other":
            self.asset = info[0]
            self.balance = info[1]
