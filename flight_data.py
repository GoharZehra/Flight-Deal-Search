from dotenv import load_dotenv
import requests_cache

requests_cache.install_cache('flight_cache', expire_after=3600)
load_dotenv()

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops
    @classmethod
    def find_cheapest_flight(cls, data,  return_date):
       if not data:
           print("There is no data")
           return cls("N/A", "N/A", "N/A", "N/A", return_date, "N/A")
       flight_list = data.get("best_flights", []) + data.get("other_flights", [])
       if not flight_list:
           print("There is no data")
           return cls("N/A", "N/A", "N/A", "N/A", return_date, "N/A")

       cheapest_raw_flight = None
       lowest_price = float("inf")

       for flight in flight_list:
           try:
            price = flight["price"]
           except KeyError:
               print("There is no price for flight")
               continue

           if price < lowest_price:
               lowest_price = price
               cheapest_raw_flight = flight

       if cheapest_raw_flight is not None:
            origin = cheapest_raw_flight["flights"][0]["departure_airport"]["id"]
            destination = cheapest_raw_flight["flights"][-1]["arrival_airport"]["id"]
            out_date = cheapest_raw_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            stops = len(cheapest_raw_flight["flights"]) - 1
            # cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)
            return cls(lowest_price, origin, destination, out_date, return_date, stops)
       else:
            return cls("N/A", "N/A", "N/A", "N/A", return_date, "N/A")







# first_flight = flight_list[0]
       # lowest_price = first_flight["price"]
       # origin = first_flight["flights"][0]["departure_airport"]["id"]
       # destination = first_flight["flights"][-1]["arrival_airport"]["id"]
       # out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
       #
       # cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)





