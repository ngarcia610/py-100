import random
import os
from logo import logo

def clear_console():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)

def playGame():
  game = False
  while not game:
    # Introduction, Generate answer
    clear_console()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)

    # Determine attempts
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
      attempts = 10
    else:
      attempts = 5

    # Check attempts
    while attempts > 0:
      print(f"You have {attempts} guesses remaining.")
      guess = int(input("Make a guess: "))
      if guess == answer:
        print("You Win.")
        attempts = 0
        game = True
      elif guess > answer:
        print("Too high.")
        attempts -= 1
      elif guess < answer:
        print("Too low.")
        attempts -= 1
    if attempts == 0 and guess != answer:
      print("Out of attempts. Game Over.")
      game = True

    if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
      game = False
    else:
      game = True

playGame()