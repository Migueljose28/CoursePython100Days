# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from datetime import datetime, timedelta
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

today = datetime.today()

# Calculate tomorrow
tomorrow = today + timedelta(days=1)
six_month_from_today = today + timedelta(day=6 * 30)

# Conserve Requests
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    },
)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)


flight_search = FlightSearch()

flights = flight_search.check_flights(
    origin_city_code="LHR",
    destination_city_code="CDG",
    from_time=tomorrow,
    to_time=six_month_from_today,
)

pprint(flights)
