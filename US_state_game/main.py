import turtle
from turtle import Turtle

import pandas

"""Screen"""
screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
# states_list = states_data.tolist()
# print(states_list)
is_game_over = False
answer_title = "Guess the State"
answer_count = 0
answer_list = []
while len(answer_list) < 50:
    answer_state = screen.textinput(title=f"{answer_title}", prompt="What's another state name?").title()
    if answer_state == "Exit":
        # print csv
        # missing_state = list(set(states_data.state) - set(answer_list))
        missing_state = [state for state in states_data.state if state not in answer_list]
        missing_state_data = pandas.DataFrame(missing_state)
        missing_state_data.to_csv("missing_state_list.csv")
    answer_data = states_data[states_data.state == answer_state]
    if not answer_data.empty:
    # if answer_state in states_list:
        answer_list.append(answer_state)
        state = Turtle()
        state.penup()
        state.goto(int(answer_data.x.item()), int(answer_data.y.item()))
        state.hideturtle()
        state.write(f"{answer_state}", align="Center")

    answer_title = f"{len(answer_list)}/50 States Correct"

