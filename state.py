import turtle

class State:
    def __init__(self,state_name,position):
        state=turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(position)
        state.write(state_name)

