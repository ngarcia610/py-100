# Day 5 - Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = []

l_length = len(letters) # 52
s_length = len(symbols) # 9
n_length = len(numbers) # 10

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generate letters, symbols, and numbers
# random.choice() also works
for _ in range(nr_letters):
  password.append(letters[random.randint(0,l_length - 1)])

for _ in range(nr_symbols):
  password.append(symbols[random.randint(0,s_length - 1)])

for _ in range(nr_numbers):
  password.append(numbers[random.randint(0,n_length - 1)])

# Shuffle the list
# You could also use a for loop to do this
password = ''.join(random.sample(password, len(password)))
print(password)
