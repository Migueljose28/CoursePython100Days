import os

import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWN_API_KEY")

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


weather_params = {
    "lat": -5.187690,
    "lon": -37.344421,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=owm_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for interval in weather_data["list"]:
    condition_code = interval["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️.",
        from_="+15017122661",
        to="+15558675310",
    )
    print(message.status)
