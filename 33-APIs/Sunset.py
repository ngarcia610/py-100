import requests

# latlong.net results for Philadelphia, PA
MY_LAT = 39.952583
MY_LNG = -75.165222

parameters = {
  "lat": MY_LAT,
  "lng": MY_LNG,
  # return 24 hour UTC unformatted
  "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Return the hour
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# Convert UTC to EST
sunrise = int(sunrise) - 4
sunset = int(sunset) - 4

print(f'The sunrise for today is {sunrise}.')
print(f'The sunset for today is {sunset}.')