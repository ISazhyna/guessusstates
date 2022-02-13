import turtle

import pandas as pd
from state import State

correct_quess=0

#creating screen with img
screen=turtle.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#reading the list of states
data=pd.read_csv("50_states.csv")
list_of_states=data["state"].to_list()

#
while len(list_of_states)>0:
    answer_state = screen.textinput(title=f"{correct_quess}/50 States Correct", prompt="What's another state's name?",)
    if answer_state:
        answer_state.title()
        if answer_state == "Exit":
            new_data = pd.DataFrame(list_of_states)
            new_data.to_csv("states_to_learn.csv")
            break
        elif answer_state in list_of_states:
            correct_quess += 1
            list_of_states.remove(answer_state)
            state_data = data[data["state"] == answer_state]
            x_coor = int(state_data.x)
            y_coor = int(state_data.y)
            write_state = State(state_data.state.item(), [x_coor, y_coor])
    else:
        list_of_states=[]
        print("exit")

screen.exitonclick()




