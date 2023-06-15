# Create a tool that uses the phonetic alphabet
# Create a dictionary using nato_phonetic_alphabet.csv
# Accept a word the user inputs
# Print a list of phonetic words for each letter

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Use a dictionary comprehension to format the data
# {new_key:new_value for (index, row) in data_frame.iterrows()}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
# List comprehension [new_item for item in list]
output = [phonetic_dict[letter] for letter in word]
print(output)