# Problem: You want to print the temperature data in weather_data.csv


# This is the dumb way to do it.
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)


# This is the cool way to do it.
import pandas


data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# A dataframe is an entire sheet. In this example 'data'.
# A series is a column or row of data. In this example 'data["temp"]'

# To find the average temperature rounded to 2 decimal places
print(data["temp"].mean())

# Find the max value
print(data["temp"].max())

# Print a row
print(data[data.day == "Monday"])

# Find the highest value row
print(data[data.temp == data.temp.max()])

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Nate"],
    "scores": [76, 56, 65]
}
data2 = pandas.DataFrame(data_dict)
print(data2)

# Convert it to a csv
data2.to_csv("new_data.csv")