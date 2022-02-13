import turtle

import pandas as pd


#creating screen with img
screen=turtle.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#reading the list of states
data=pd.read_csv("50_states.csv")
list_of_states=data["state"].to_list()

screen.exitonclick()




