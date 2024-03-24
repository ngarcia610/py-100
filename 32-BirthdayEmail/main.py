import pandas
import random
import smtplib
from datetime import datetime
from dotenv import dotenv_values

# Import Secrets
secrets = dotenv_values(".env")
my_email = secrets["EMAIL"]
my_appkey = secrets["APPKEY"]


# Check if today matches a birthday from birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
  birthday_person = birthdays_dict[today_tuple]
  file_path = f"letter_templates/letter{random.randint(1,3)}.txt"
  with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", birthday_person["name"])
    message = f"Subject: Happy Birthday!\n\n{contents}".encode("utf-8")
    # encode() has some weird output. I need to research this bug.

  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_appkey)
    connection.sendmail(
      from_addr=my_email,
      to_addrs=birthday_person["email"],
      msg=message
    )
    connection.close()
