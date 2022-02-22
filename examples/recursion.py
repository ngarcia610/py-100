# Example of using recursion, a type of loop
# Recursion is when a function calls itself until it reaches a base case
# In the irl example of russian dolls, the base case is the smallest doll
def factorial(n):
  if n < 2: # this is the base case
    return 1
  return n * factorial(n-1) # this is the recursive case


# Example 2
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15