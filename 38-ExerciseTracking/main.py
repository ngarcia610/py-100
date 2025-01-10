import creds
import requests

API_KEY = creds.API_KEY
APP_ID = creds.APP_ID
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = 90.7
HEIGHT = 173.7
AGE = 39

exercise_text = input("Tell me which exercises you did: ")

headers = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY
}

params = {
  "query": exercise_text,
  "gender": GENDER,
  "weight_kg": WEIGHT,
  "height_cm": HEIGHT,
  "age": AGE
}

response = requests.post(URL, json=params, headers=headers)
result = response.json()
print(result)
