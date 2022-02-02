import logging

from models import Balance

import requests

logger = logging.getLogger()


class CelsiusClient:
    def __init__(self, public_key: str):
        self._base_url = "https://wallet-api.staging.celsius.network/wallet/balance/"

        self._public_key = public_key

        #self.balances = self.get_balances()

    def _make_request(self, method: str):
        payload = {}
        headers = {'X-Cel-Partner-Token': 'MISSING',
                   'X-Cel-User-Token': self._public_key
                   }
        endpoint = self._base_url

        print(str(headers))

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

    def get_balances(self): # -> typing.Dict[str, Balance]:

        account_data = self._make_request("GET")

        print(account_data)