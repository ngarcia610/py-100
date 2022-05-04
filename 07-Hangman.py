# Day 7 - Hangman Game

from random_word import RandomWords
r = RandomWords()

chosen_word = str(r.get_random_word())
display = []
lives = 6
gameover = False

# Create the display
for _ in range(len(chosen_word)):
  display += "_"
print("".join(display))

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(chosen_word)

# Game Logic
while gameover == False:
  guess = input("Guess a letter: ").lower()

  # Guess is correct or hyphen
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == '-':
      display[position] = '-'
    elif letter == guess:
      display[position] = letter

  # Guess is incorrect
  if guess not in chosen_word:
    lives -= 1
    print(f"Lives remaining: {lives}")
    if lives == 0:
      gameover = True
      print("No lives remaining. You lose.")

  print("".join(display))

  # Win Condition
  if "_" not in display:
    gameover = True
    print("You win!")

  print(stages[lives])

print(f"The word was: {chosen_word}")