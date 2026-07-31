import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

GENDER = os.environ["GENDER"]
WEIGHT_KG = int(os.environ["WEIGHT_KG"])
HEIGHT_CM = int(os.environ["HEIGHT_CM"])
AGE = int(os.environ["AGE"])

SHEETY_AUTH = os.environ["SHEETY_AUTH"]
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

nutrition_endpoint = os.environ["NUTRITION_ENDPOINT"]
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]

user_input = input("Tell me which exercises you did:")

sheety_headers = {"Authorization": f"Basic {SHEETY_AUTH}"}

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

config_nutrition = {
    "query": user_input,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(
    nutrition_endpoint, json=config_nutrition, headers=headers
)
response.raise_for_status()
result = response.json()


today = datetime.now()
for workout in result["exercises"]:
    config_sheety = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }
    response_sheety = requests.post(
        sheety_endpoint, json=config_sheety, headers=sheety_headers
    )
    print(response_sheety.text)
