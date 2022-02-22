# Takes a sentence string and returns Pig Latin

def pig_latin(text):
  # Separate the text into words
  words = text.split(" ")
  say = []
  for word in words:
    # Create the pig latin word and add it to the list
    word = word[1:] + word[0] + "ay"
    # Turn the list back into a phrase
    say.append(word)
  say = " ".join(say)
  return say

# Should be "ellohay owhay reaay ouyay"
print(pig_latin("hello how are you"))
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))