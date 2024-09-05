# Use a get request to fetch 10 T/F questions
# Parse the JSON response and replace the value of question_data
# Create a py dictionary for the amount and type parameters
import requests

parameters = {
<<<<<<< HEAD
  "amount": 10,
  "type": "boolean"
=======
   "amount": 10,
   "type": "boolean"
>>>>>>> 168b05f330c6f9434d4bfe092811f97301ccd290
}

response = requests.get(url="https://opentdb.com/api.php?amount=10", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
