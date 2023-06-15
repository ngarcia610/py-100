# Use a dictionary comprehension to
# create a dictionary of students and scores
# then use that dictionary to create a new list of
# students that have a score greater than or equal to 60
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Nate', 'Willy']

students_scores = {student:random.randint(1,100) for student in names}

print(students_scores)

# new_dictionary = {new_key:new_value for (key, value) in dict.items() if test}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

print(passed_students)