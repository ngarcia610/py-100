from turtle import Screen, Turtle
from snake import Snake
import time

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the Snake using a class
snake = Snake()

# Respond to arrow key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Run the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Move the snake using a class
    snake.move()

screen.exitonclick()
