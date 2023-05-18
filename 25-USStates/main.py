import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Guess the name of a U.S. State.").title()

    # If you enter 'Exit' as your choice, generate a list of states you missed
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the answer is equal to one of the states in the csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # If correct, create a turtle that writes the name of the state at the coordinates
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # This takes the entire row
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # Using 'answer_state' to write the state is easier and makes sense
        # But if you want to use the data, try this instead
        # state_data.state.item()

'''
Find the coordinates of each state
This is how 50_states.csv data was collected
def get_mouse_click_coor(x, y):
 print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
'''