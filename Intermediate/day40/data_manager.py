import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()


SHEETY_PRICE_ENDPOINT = os.environ["SHEETY_PRICE_ENDPOINT"]
SHEETY_CUSTOMER_ENDPOINT = os.environ["SHEETY_CUSTOMER_ENDPOINT"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_PRICE_ENDPOINT, auth=self._authorization
        )
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        requests.put(
            url=f"{SHEETY_PRICE_ENDPOINT}/{row_id}",
            json={"price": {"lowestPrice": new_price}},
            auth=self._authorization,
        )

    def get_customer_emails(self):
        response = requests.get(
            SHEETY_CUSTOMER_ENDPOINT, auth=self._authorization
        )
        data = response.json()
        print(data)
        self.customer_data = data["users"]
        return self.customer_data
