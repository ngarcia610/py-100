# Day 10 Calculator
# Demonstrates passing function output to other functions

from art import logo

# Addition
def add(n1, n2):
  return n1 + n2

# Subtraction
def subtract(n1, n2):
  return n1 - n2

# Multiplication
def multiply(n1, n2):
  return n1 * n2

# Division
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Gather user choices
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  should_continue = True

  # Allow the user to continue calculating with the result of the first calculation
  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Select an option: \n 'y' Continue calculating with {answer} \n 'n' Start a new calculation \n 'q' Quit \n :")
    if choice == 'y':
      num1 = answer
    elif choice == 'n':
      calculator()
      should_continue = False
    else:
      should_continue = False

calculator()