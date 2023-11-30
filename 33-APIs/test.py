import requests

# Create a response from the API endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

# Response codes
# https://www.webfx.com/web-development/glossary/http-status-codes/
# 100 - Informational
# 200 - Success
# 300 - Redirection
# 400 - Client Error
# 500 - Server Error

response.raise_for_status()

# Format the response into a tuple with the lat and long coordinates

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

position = (longitude, latitude)

print(position)