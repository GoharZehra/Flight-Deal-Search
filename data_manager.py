import requests
import requests_cache
from dotenv import load_dotenv
import os

requests_cache.install_cache('flight_cache', expire_after=3600)

load_dotenv()

class DataManager:
    def __init__(self):
        self.SHEETY_AUTHORIZATION = os.environ["SHEETY_AUTHORIZATION"]
        self.SHEETY_URL = os.environ["SHEETY_URL"]
        self.SHEETY_URL_USERS = os.environ["SHEETY_URL_USERS"]
        self.headers = {"Authorization" : self.SHEETY_AUTHORIZATION}
    def destination_data(self):
        response = requests.get(url=self.SHEETY_URL, headers=self.headers)
        result = response.json()["prices"]
        return result

    def update_price(self, row_id, price):
        price_update = {
            "price": {
                "lowestPrice": price,
            }
        }
        response = requests.put(url=f"{self.SHEETY_URL}/{row_id}", headers=self.headers, json=price_update)
        if response.status_code != 200:
            print("Data not updated")

    def get_emails(self):
            response = requests.get(url=self.SHEETY_URL_USERS, headers=self.headers)
            result = response.json()["users"]
            return result