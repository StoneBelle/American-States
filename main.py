from turtle import Screen, Turtle
import pandas as pd
from check_anwers import Answers
from scoreboard import Scoreboard

# Screen Setup to be an image of a blank American map
wn = Screen()
wn.title("Name the American States")
wn.setup(width=800, height=600)
image = "blank_states_img.gif"
wn.addshape(image)
states_map = Turtle(image)

# State Data from CSV file
state_data = pd.read_csv("50_states.csv")
all_states = state_data["state"].to_list()
score = Scoreboard()
user_prompt = "Enter a State"
check_answer = Answers()

while len(score.valid_answers) < 50:
    answer = wn.textinput(title="Guess the States", prompt=user_prompt).title()
    # If user exits from game early, store all the states that have not been named in a new CSV file.
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in score.valid_answers:
                missing_states.append(state)
        df = pd.DataFrame(missing_states)  # Converts "missing_states" list into a data frame called "df"
        df.to_csv("missing_states.csv")  # Converts and save "df" into a csv file within directory
        break  # Exits program early (i.e. closes pop up window). Thus, program does not need "wn.mainloop"

    # If answer is in CSV file, show the state's name on correct position on map.
    if answer in all_states:
        state_pos = state_data[state_data.state == answer]
        check_answer.show_state(int(state_pos.x), int(state_pos.y), answer)
        score.update_score(answer)
        user_prompt = "Enter another State"
    elif answer not in all_states:
        user_prompt = "Incorrect. Enter another State"


