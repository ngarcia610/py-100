# Damien Hirst inspired dot drawing using Turtle

import random
import turtle

# Use this to create the list of RGB values
# ---
# import colorgram

# Pull the colors from image.jpg
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# Test the colors using https://www.w3schools.com/colors/colors_rgb.asp
# Removed the shades of white
# ---
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)

nate = turtle.Turtle()
nate.speed("fastest")
nate.penup()
nate.hideturtle()
# Move the turtle to the starting point
nate.setheading(225)
nate.forward(300)
nate.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    nate.dot(20, random.choice(color_list))
    nate.forward(50)

    # Reset the turtle on a new line
    if dot_count % 10 == 0:
        nate.setheading(90)
        nate.forward(50)
        nate.setheading(180)
        nate.forward(500)
        nate.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
