import tkinter as tk
import logging

from connectors.binance import BinanceClient
from connectors.kraken import KrakenClient
from connectors.celsius import CelsiusClient

from interface.styling import *

logger = logging.getLogger()


class Root(tk.Tk):
    def __init__(self, binance: BinanceClient, kraken: KrakenClient, celsius: CelsiusClient):
        super().__init__()

        self.binance = binance
        self.kraken = kraken
        self.celsius = celsius

        self.title("Portfolio App by Gitano v.0.1")

        name = tk.Label(self, text="Coin Name", bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
        name.grid(row=0, column=0, sticky="nsew")

        price = tk.Label(self, text="Price", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
        price.grid(row=0, column=1, sticky="nsew")

        no_coins = tk.Label(self, text="Coin Owned", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
        no_coins.grid(row=0, column=2, sticky="nsew")

        amount_paid = tk.Label(self, text="Total Amount Paid", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
        amount_paid.grid(row=0, column=3, sticky="nsew")

        current_val = tk.Label(self, text="Current Value", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
        current_val.grid(row=0, column=4, sticky="nsew")

        pl_coin = tk.Label(self, text="P/L per coin", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT)
        pl_coin.grid(row=0, column=5, sticky="nsew")

        totalpl = tk.Label(self, text="Total P/L With Coin", bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT, )
        totalpl.grid(row=0, column=6, sticky="nsew")

