# Pixela: Record and track your habits by API
# https://pixe.la/
# https://docs.pixe.la/

import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
  "token": "",
  "username": "nate100",
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)