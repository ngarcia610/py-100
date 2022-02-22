# Takes the year as input and checks if it is a leap year
# Returns True or False

def is_leap(year):
  return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(input("Enter a year: "))
print(is_leap(year))
