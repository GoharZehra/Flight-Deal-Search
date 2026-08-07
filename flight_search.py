import requests
from dotenv import load_dotenv
import os

load_dotenv()
class FlightSearch:
    def __init__(self):
        self.serpAPI = os.environ["SERPAPI_API_KEY"]
        self.serpURL = os.environ["SERPAPI_URL"]

    def flight_search(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        provide = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.serpAPI,
        }

        if is_direct:
            provide["stops"] = "1"
        response = requests.get(url=self.serpURL, params=provide)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None
        result = response.json()
        if "error" in result:
            print(f"API error: {result['error']}")
            return None
        return result