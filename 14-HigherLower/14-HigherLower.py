from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
  """Format the account data into a printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def clear_console():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)

print(logo)
score = 0
game_continue = True
account_b = random.choice(data)


while game_continue:
  # Pull the accounts from data
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  # Format the data
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")

  # Get the guess and check if correct
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear_console()
  print(logo)

  # Provide feedback
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")

  else:
    game_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")