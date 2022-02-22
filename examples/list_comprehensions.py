# List comprehensions let us create new lists based on sequences or ranges
# You want to make a list of multiples of 7, from 7 to 70.
multiples = []
for x in range(1, 11):
  multiples.append(x*7)
print(multiples)

# Same example as a list comprehension
multiples = [x*7 for x in range(1,11)]
print(multiples)

# List comprehension with a conditional
z = [x for x in range(0,101) if x % 3 == 0]
print(z)

# Modifying all values in a list using a comprehension
temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_adjusted = [temp + 20 for temp in temperatures]
print(temperatures_adjusted)

# Converting Celsius to Farenheit using a list comprehension
temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_F = [(9.0/5.0)*temp + 32 for temp in temperatures]
print(temperatures_F)
