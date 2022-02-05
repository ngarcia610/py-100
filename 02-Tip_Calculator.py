# Day 2 - Tip Calculator

print("Welcome to the tip calculator.")

# Collect data
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?  "))
people = int(input("How many people to split the bill? "))

# Calculate
bill_with_tip = tip / 100 * bill + bill
print("The total bill is ${:.2f}".format(bill_with_tip))

bill_per_person = bill_with_tip / people
print("Each person should pay ${:.2f}".format(bill_per_person))
