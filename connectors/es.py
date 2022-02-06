from models import Balance

import requests
import typing
import logging

logger = logging.getLogger()


class EsConnector:
    def __init__(self, acct_data: typing.Dict):
        self.name = "ES"

        self._endpoint = acct_data['endpoint']
        self._api_key = acct_data['api-key']
        self._account_data = acct_data['indexes']
        self._parameters = self._get_param_data()

        self.balances = self.get_balances()

    def _get_param_data(self):
        param_string = ''

        for i in self._account_data:
            param_string += i[0]
            if i[0] != self._account_data[-1][0]:
                param_string += ","

        return param_string

    def _make_request(self):
        method = "GET"
        query_string = f"?module=account&action=balancemulti&address={self._parameters}&tag=latest&apikey={self._api_key}"

        try:
            response = requests.get(self._endpoint + query_string, headers={"User-Agent": ""})
        except Exception as e:
            logger.error("Connection error while making %s request to %s: %s", method, self._endpoint, e)
            return None

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)",
                         method, self._endpoint, response.json(), response.status_code)

    def get_balances(self):
        response = self._make_request()
        wallets = self._account_data
        temp_balance = 0.0
        balances = dict()

        for count, value in enumerate(response['result']):
            temp_balance += float(value['balance']) * 0.000000000000000001 * wallets[count][1]

        balances['ETH'] = Balance(['ETH', temp_balance], "other")

        return balances
