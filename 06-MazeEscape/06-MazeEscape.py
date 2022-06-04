# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json 

# Write a program using an if/elif/else statement so Reeborg can find the exit.
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, 
# going straight ahead if it can’t turn right, or turning left as a last resort.
# What you need to know:
# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(),
# right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).

# Clear VScode errors------------------
def turn_left():
  pass
def front_is_clear():
  pass
def at_goal():
  pass
def move():
  pass
def right_is_clear():
  pass
# -------------------------------------

# Define a turn right function:
def turn_right():
  turn_left()
  turn_left()
  turn_left()

# Make sure you start at a wall
while front_is_clear():
  move()
turn_left()

# Check if at goal:
while not at_goal():
  # Turn right if you can
  if right_is_clear():
    turn_right()
    move()
  # Go straight if you can't turn right
  elif front_is_clear():
    move()
  # Turn left as a last resort
  else:
    turn_left()