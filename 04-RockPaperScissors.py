from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = True

while game is True:
  # User's choice
  user_choice = input("What do you choose? rock/paper/scissors\n").lower()

  # Computer's choice
  computer_choice = randint(1,3)
  if computer_choice == 1:
    computer_choice = 'rock'
  elif computer_choice == 2:
    computer_choice = 'scissors'
  else:
    computer_choice = 'paper'

  # Outcomes
  if user_choice == "rock":
    print(f"You chose: {rock}.")
    if computer_choice == "scissors":
      print(f"The computer chose: {scissors}")
      print("Rock crushes scissors. You win.")
      game = False
    elif computer_choice == "paper":
      print(f"The computer chose: {paper}")
      print("Paper suffocates rock. You lose.")
      game = False
    else:
      print(f"The computer chose: {rock}")
      print("Tie game. Try again.")

  elif user_choice == "scissors":
    print(f"You chose: {scissors}.")
    if computer_choice == "paper":
      print(f"The computer chose: {paper}")
      print("Scissors cuts paper. You win.")
      game = False
    elif computer_choice == "rock":
      print(f"The computer chose: {rock}")
      print("Scissors is crushed by rock. You lose.")
      game = False
    else:
      print(f"The computer chose: {scissors}")
      print("Tie game. Try again.")

  elif user_choice == "paper":
    print(f"You chose: {paper}.")
    if computer_choice == "rock":
      print(f"The computer chose: {rock}")
      print("Paper suffocates rock. You win.")
      game = False
    elif computer_choice == "scissors":
      print(f"The computer chose: {scissors}")
      print("Scissors cuts paper. You lose.")
      game = False
    else:
      print(f"The computer chose: {paper}")
      print("Tie game. Try again.")

  else:
    print("Invalid choice!\nPlease enter rock, paper, or scissors.")
