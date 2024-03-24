import requests
import smtplib
import time
from datetime import datetime
from dotenv import dotenv_values

# latlong.net results for Philadelphia, PA
MY_LAT = 39.952583
MY_LONG = -75.165222

# Import Secrets for Email
secrets = dotenv_values(".env")
my_email = secrets["EMAIL"]
my_appkey = secrets["APPKEY"]

# Compare ISS position with yours
# Allow + or - 5 degrees
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_latitude <= MY_LONG + 5):
        return True

# Check if it's dark outside
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# Send an email to look up
while True:
    # Checks every 60 seconds
    time.sleep(60)

    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_appkey)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject: Look Up\n\nThe ISS is above you in the sky."
            )
            connection.close()