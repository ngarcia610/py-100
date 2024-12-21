'''
Objectives:
Pull in the stock prices of the stocks we're interested in
Find the difference between two days and the direction
Calculate the percentage difference
Fetch the relevant news data
Send an SMS with the percentage and news
https://www.alphavantage.co/documentation/
'''

import requests
from dotenv import dotenv_values
from twilio.rest import Client

secrets = dotenv_values(".env")

STOCK_NAME = secrets["STOCK_NAME"]
COMPANY_NAME = secrets["COMPANY_NAME"]
STOCK_ENDPOINT = secrets["STOCK_ENDPOINT"]
STOCK_API_KEY = secrets["STOCK_API_KEY"]
NEWS_ENDPOINT = secrets["NEWS_ENDPOINT"]
NEWS_API_KEY = secrets["NEWS_API_KEY"]
TWILIO_SID = secrets["TWILIO_SID"]
TWILIO_AUTH_TOKEN = secrets["TWILIO_AUTH_TOKEN"]

#1. Get yesterday's closing stock price
stock_params = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = data_list["4. close"]

#2. Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

#3. Find the positive difference between 1 and 2
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

#4. Find the percentage difference between the closing prices
diff_percent = (difference / float(yesterday_closing_price)) * 100

#5. If the percentage is greater than 5, print a string
#Change 5 to 1 for testing
if diff_percent > 5:
  news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
  }
  #6. Print a news article instead of a string
  news_response = requests.get(NEWS_ENDPOINT, params=news_params)
  articles = news_response.json()["articles"]

  #7. Using articles create a list that contains the first 3 articles
  three_articles = articles[:3]
  print(three_articles)

  #8. Create a new list of the first 3 article's headline and description
  formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

  #9. Send each article as a separate message via Twilio
  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  for article in formatted_articles:
    message = client.messages.create(
      body=article,
      from_="<Twilio virtual number>",
      to="<Your phone number>"
    )
