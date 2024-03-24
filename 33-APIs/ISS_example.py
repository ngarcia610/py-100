# pip install normalizer
# pip install requests
import requests

# Create a response from the API endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# <Response [200]> expected
print(response)

# Use the requests module's method for all responses NOT 200
response.raise_for_status()

# Format the response into a tuple with the lat and long coordinates
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
position = (longitude, latitude)
print(position)