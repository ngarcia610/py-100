def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result

# Should return {'a':5}
print(count_letters('aaaaa'))
