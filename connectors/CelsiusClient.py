import logging
import typing

from models import Balance

import requests

logger = logging.getLogger()


class CelsiusClient:
    def __init__(self, public_key: str, secret_key: str):
        self._base_url = "https://wallet-api.celsius.network/wallet/balance/"

        self._public_key = public_key
        self._secret_key = secret_key

        self.balances = self.get_balances()

    def _make_request(self, method: str):
        payload = {}
        headers = {'X-Cel-Partner-Token': self._secret_key,
                   'X-Cel-Api-Key': self._public_key
                   }
        endpoint = self._base_url

        if method == "GET":
            try:
                response = requests.get(self._base_url, headers=headers, data=payload)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)",
                         method, endpoint, response.json(), response.status_code)

    def get_balances(self) -> typing.Dict[str, Balance]:

        account_data = self._make_request("GET")
        balances = dict()

        if account_data is not None:
            for key, value in account_data['balance'].items():
                if float(value) > 0.0001:
                    balances[key.upper()] = Balance([key.upper(), value], "celsius")

        return balances
