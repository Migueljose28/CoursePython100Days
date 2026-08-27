# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from datetime import date, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
from pprint import pprint


requests_cache.install_cache(
    "flight_cache.sqlite",
    urls_xpire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    },
)


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
customer_data = data_manager.get_customer_emails()
emails = [customer["whatIsYourEmail?"] for customer in customer_data]

now = date.today()
tomorrow = now + timedelta(days=1)
six_month_from_today = now + timedelta(days=(6 * 30))

flight_search = FlightSearch()

notification_manager = NotificationManager()

ORIGIN_CITY_CODE = "LHR"

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_CODE,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )

    cheapest_flight = find_cheapest_flight(
        flights, return_date=six_month_from_today.strftime("%Y-%m-%d")
    )
    pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")

    if (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < destination["lowestPrice"]
    ):
        pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
        data_manager.update_lowest_price(
            sheet_data[0]["id"], cheapest_flight.price
        )
        if cheapest_flight.stops == 0:
            message = (
                f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
        else:
            message = (
                f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"with {cheapest_flight.stops} stop(s) "
                f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."
            )

        print(
            f"Check your email. Lower price flight found to {destination['city']}!"
        )

        # notification_manager.send_whatsapp(
        #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
        #     f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #     f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
        #     f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #     f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )

        notification_manager.send_emails(emails, message_body=message)
