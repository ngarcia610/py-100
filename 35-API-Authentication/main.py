# Create a program that will take a location,
# and check the weather report for that location.
# If rain is in the forecast, it will send an sms notification

# Openweather is used for forecast
# Twilio is used for SMS
# Get the secrets and add them to .env
# Import the secrets with dotenv
import requests
from twilio.rest import Client
from dotenv import dotenv_values


# Import Secrets for Email
# secrets = dotenv_values(".env")
# my_email = secrets["EMAIL"]
# my_appkey = secrets["APPKEY"]

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""  # Openweather API key
account_sid = ""  # Twilio Account ID
auth_token = ""  # Twilio Auth Token

weather_params = {
    "lat": 39.952583,
    "lon": -75.165222,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="",  # Twilio virtual num
        to=""  # Twilio verified real num
    )
    print(message.status)
