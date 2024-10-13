# Objectives:
# Pull in the stock prices of the stocks we're interested in
# Find the difference between two days and the direction
# Calculate the percentage difference
# Fetch the relevant news data
# Send an SMS with the percentage and news
import requests
from dotenv import dotenv_values

secrets = dotenv_values(".env")

STOCK_NAME = secrets["STOCK_NAME"]
COMPANY_NAME = secrets["COMPANY_NAME"]
STOCK_ENDPOINT = secrets["STOCK_ENDPOINT"]
STOCK_API_KEY = secrets["STOCK_API_KEY"]
NEWS_ENDPOINT = secrets["NEWS_ENDPOINT"]
NEWS_API_KEY = secrets["NEWS_API_KEY"]

# Get yesterday's closing stock price
# https://www.alphavantage.co/documentation/
stock_params = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
# Use a list comprehension to get the daily close data
# [new_item for item in list]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = data_list["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2
# Convert to float and use abs()
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

# Find the percentage difference between the closing prices
diff_percent = (difference / float(yesterday_closing_price)) * 100

# If the percentage is greater than 5, get news
if diff_percent > 5:  # Change to > 1 for testing
  news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
  }

  news_response = requests.get(NEWS_ENDPOINT, params=news_params)
  articles = news_response.json()["articles"]

  # Using articles create a list that contains the first 3 articles
  three_articles = articles[:3]

  # Use Twilio to send a message with each article's title and description to your phone