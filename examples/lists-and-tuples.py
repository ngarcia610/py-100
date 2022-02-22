animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0

for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# Returns a list of items in the list, with the index
for index, animal in enumerate(animals):
  print("{} - {}".format(index + 1, animal))