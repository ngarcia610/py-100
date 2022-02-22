# Create a formatted table after converting Farenheit to Celsius

def to_celsius(x):
  return (x-32)*5/9

# {:>3} means align the text 3 spaces
# {>6.2f} means align the text 6 spaces and include only 2 decimal points

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))