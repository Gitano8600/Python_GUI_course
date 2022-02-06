import logging
import time
import os
import typing

import requests

import urllib.parse
import hashlib
import hmac
import base64

from models import Balance

logger = logging.getLogger()


class KrakenClient:
    def __init__(self, public_key: str, secret_key: str):
        self.name = "Kraken"
        self._base_url = "https://api.kraken.com"

        self._public_key = public_key
        self._secret_key = secret_key

        self.balances = self.get_balances()

    def _generate_signature(self, endpoint: str, data: typing.Dict, secret: str) -> str:

        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = endpoint.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    def _make_request(self, method: str, endpoint: str):

        headers = dict()
        data = {"nonce": str(int(1000*time.time()))}
        headers['API-Key'] = self._public_key
        headers['API-Sign'] = self._generate_signature(endpoint, data, self._secret_key)

        if method == "GET":
            try:
                response = requests.get(self._base_url + endpoint, headers=headers, data=data)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None

        if method == "POST":
            try:
                response = requests.post(self._base_url + endpoint, headers=headers, data=data)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)",
                         method, endpoint, response.json(), response.status_code)
            return None

    def get_balances(self) -> typing.Dict[str, Balance]:

        account_data = self._make_request("POST", "/0/private/Balance")

        balances = dict()

        print(account_data['result'])

        if account_data is not None:
            for key, value in account_data['result'].items():
                if float(value) > 0.0001:
                    balances[key.upper()] = Balance([key.upper(), value], "kraken")

        return balances
