# Example of unpacking lists within a dictionary
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
  for item in value:
    print("{} {}".format(item, key))

# Here is your output:
  # red shirt
  # blue shirt
  # white shirt
  # blue jeans
  # black jeans
