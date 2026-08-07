from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os

#TO CONSERVE REQUESTS#
# requests_cache.install_cache('flight_cache', expire_after=3600)
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

tomorrow = datetime.now() + timedelta(days=1)
today_date = tomorrow.strftime("%Y-%m-%d")
six_months_from_today= (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

data_sheety = DataManager()
sheet_data = data_sheety.destination_data()
# pprint(sheet_data, indent=1)

notification_manager = NotificationManager()

for value in sheet_data:
    destination_code = value["iataCode"]
    city = value["city"]
    lowest_price = value["lowestPrice"]
    id_ = value["id"]

    # print(destination_code, city, lowest_price, id_)
    flights = FlightSearch().flight_search("LHR", destination_code, today_date, six_months_from_today)
    cheapest_flight = FlightData.find_cheapest_flight(flights, six_months_from_today)
    pprint(f"{destination_code} -> {cheapest_flight.price}")


    if cheapest_flight.price == "N/A":
        print("No direct flight available")
        stopover_flights = FlightSearch().flight_search("LHR", destination_code, today_date, six_months_from_today, is_direct=False)
        cheapest_flight = FlightData.find_cheapest_flight(stopover_flights,six_months_from_today)
        print(f"Cheapest indirect flight price is: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < lowest_price:
        pprint(f"Lower price flight found to {city}!")
        data_sheety.update_price(id_, cheapest_flight.price)
        # notification_manager.send_message(cheapest_flight)
        user_data = data_sheety.get_emails()
        email_list = [row["enterYourEmailAddress:"] for row in user_data]
        notification_manager.send_emails(email_list, cheapest_flight)



