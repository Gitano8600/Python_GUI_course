import logging
import requests
import time
import typing

from urllib.parse import urlencode

import hmac
import hashlib

from models import Balance

logger = logging.getLogger()


class BinanceClient:
    def __init__(self, public_key: str, secret_key: str):
        self._base_url = "https://api.binance.com"

        self._public_key = public_key
        self._secret_key = secret_key

        self._headers = {'X-MBX-APIKEY': self._public_key}

        self.balances = self.get_balances()

        self.prices = dict()

        self.logs = []

        self._ws_id = 1
        self._ws = None

    def _add_log(self, msg: str):
        logger.info("%s", msg)
        self.logs.append({"log": msg, "displayed": False})

    def _generate_signature(self, data: typing.Dict) -> str:
        return hmac.new(self._secret_key.encode(), urlencode(data).encode(), hashlib.sha256).hexdigest()

    def _make_request(self, method: str, endpoint: str, data: typing.Dict):
        if method == "GET":
            try:
                response = requests.get(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None

        elif method == "POST":
            try:
                response = requests.post(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None

        elif method == "DELETE":
            try:
                response = requests.delete(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None
        else:
            raise ValueError()

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)",
                         method, endpoint, response.json(), response.status_code)
            return None

    def get_balances(self) -> typing.Dict[str, Balance]:
        data = dict()
        data['type'] = "SPOT"
        data['timestamp'] = int(time.time() * 1000)
        data['signature'] = self._generate_signature(data)

        balances = dict()

        account_data = self._make_request("GET", "/sapi/v1/accountSnapshot", data)
        print(account_data)

        if account_data is not None:
            for a in account_data['snapshotVos'][0]['data']['balances']:
                if a['free'] != '0':
                    balances[a['asset']] = Balance(a, "binance")

        return balances
