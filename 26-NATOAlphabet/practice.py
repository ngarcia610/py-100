# List Comprehensions
new_list = [new_item for item in list]
new_list = [new_item for item in list if test]

# Example
# Opens 2 files, and returns a list of shared values
with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]

print(result)

# Dictionary Comprehension
new_dict = {new_key:new_value for item in list}
