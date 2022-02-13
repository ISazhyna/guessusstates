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
    answer_state = screen.textinput(title=f"{correct_quess}/50 States Correct", prompt="What's another state's name?").title()

screen.exitonclick()




