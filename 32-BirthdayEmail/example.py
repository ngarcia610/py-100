import smtplib
import random
import datetime as dt
from dotenv import dotenv_values

# Import Secrets
secrets = dotenv_values(".env")
my_email = secrets["EMAIL"]
my_appkey = secrets["APPKEY"]
to_email = secrets["TO"]

# Create Time Vars
now = dt.datetime.now()
weekday = now.weekday()

# If today is Tuesday,
# Open the quotes file and save a random quote
# Send an email with that quote using Gmail
if weekday == 1:
  with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_appkey)
    connection.sendmail(
      from_addr=my_email,
      to_addrs=to_email,
      msg=f"Subject: Monday Motivation\n\n{quote}"
    )
    connection.close()
