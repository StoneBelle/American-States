from turtle import Screen, Turtle
import pandas as pd
from scoreboard import Scoreboard

# TODO 1: SetUp Screen to be an image of a blank American map
wn = Screen()
wn.title("Name the American States")
wn.setup(width=800, height=600)
image = "blank_states_img.gif"
wn.addshape(image)
states_map = Turtle(image)


def show_state(x_pos, y_pos, state):
    make_text = Turtle()
    make_text.penup()
    make_text.hideturtle()
    make_text.setpos(x_pos, y_pos)
    make_text.write(state, align="center", font=("Arial", 8, "normal"))


# TODO 2: Ask user to name any state on the map.
answer = wn.textinput(title="Guess the States", prompt="Enter a State").title()
state_data = pd.read_csv("50_states.csv")
state_list = state_data["state"].to_list()
print(state_list)
score = Scoreboard()
# TODO 5:
while True:
    # TODO 4: If answer is in file, write the state's name on correct position on map.
    if answer in state_list:
        state_pos = state_data[state_data.state == answer]
        state_x = int(state_pos.x)
        state_y = int(state_pos.y)
        show_state(state_x, state_y, answer)
        score.show_score(answer)
        print(score.valid_answers)
        answer = wn.textinput(title="Guess the States", prompt="Enter another State").title()
    else:
        answer = wn.textinput(title="Guess the States", prompt="Incorrect. Enter another State").title()

wn.mainloop()
