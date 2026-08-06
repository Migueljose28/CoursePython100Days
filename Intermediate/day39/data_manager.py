import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

sheety_endpoint = (
    "https://api.sheety.co/3243dcf47c17c4d3928a03ebd9a188ed/flightDeals/prices"
)


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._authorization = (
            HTTPBasicAuth("Authorization", os.environ["SHEETY_TOKEN"]),
        )
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            sheety_endpoint,
            auth=self._authorization,
        )
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {"price": {"lowestPrice": new_price}}
        requests.put(
            url=f"{sheety_endpoint}/{row_id}",
            json=new_data,
            auth=self._authorization,
        )
