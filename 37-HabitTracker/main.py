# Pixela: Record and track your habits by API
# https://pixe.la/
# https://docs.pixe.la/

import requests
from datetime import datetime

USERNAME = "nate100"
TOKEN = ""
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

#1. Create User
user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#2. Create Graph Config
graph_config = {
  "id": "graph1",
  "name": "Cycling Graph",
  "unit": "Km",
  "type": "float",
  "color": "shibafu"
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#3. Create pixel

today = datetime(year=2024, month=12, day=27)

pixel_config = {
  "date": today.strftime("%Y%m%d"),
  "quantity": "5",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)