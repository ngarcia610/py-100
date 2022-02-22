# Program that prints the solution to the FizzBuzz game.
# Prints each number starting at 1 and ending at 100
# If the number is divisible by 3, print "Fizz"
# If the number is divisible by 5, print "Buzz"
# If the number is divisible by 3 and 5, print "FizzBuzz"

for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
