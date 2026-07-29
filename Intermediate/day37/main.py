from datetime import datetime
import os
import requests

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("USERNAME")

GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers
# )
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages have you read today?"),
}

# response = requests.post(
#    url=pixel_creation_endpoint, json=pixel_data, headers=headers
# )
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_update_data = {"quantity": "1"}

# response = requests.put(
#    url=update_endpoint, json=pixel_update_data, headers=headers
# )
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response)
