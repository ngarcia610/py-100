# Use a get request to fetch 10 T/F questions
# Parse the JSON response and replace the value of question_data
# Create a py dictionary for the amount and type parameters
import requests

parameters = {
  "amount": 10,
  "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
