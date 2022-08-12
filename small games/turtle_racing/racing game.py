from turtle import Turtle, Screen
import random

start = False
screen = Screen()
screen.setup(width = 500, height = 400)
player_bet = screen.textinput(title = "Make your bet", prompt = "Which coloured turtle will win: ")
colour = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

for i in range(6):
    tim = Turtle(shape='turtle')
    tim.color(colour[i])
    tim.penup()
    tim.goto(-230, -125+50*i)
    turtles.append(tim)

if player_bet:
    start = True


while start:
    for t in turtles:
        if t.xcor() > 230:
            start = False
            winning = t.pencolor()
            if winning == player_bet:
                print(f"You won! the {winning} turtle is the winner!")
            else:
                print(f"You lost! the {winning} turtle is the winner!")
        ran_speed = random.randint(0, 10)
        t.forward(ran_speed)



screen.exitonclick()

# This code is not perfect, when more than one turtle win, it won't cope.