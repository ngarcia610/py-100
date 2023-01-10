import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# By setting the colormode to 255, you can generate rgb colors using the randint function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Draw as fast as possible, also can take an int 0-10
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

# The window stays until you click on it
screen = t.Screen()
screen.exitonclick()