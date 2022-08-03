import turtle
from turtle import *
from random import *

#import ... as t
timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
screen = Screen()
# a square
#for i in range(4):
#timmy.right(90)
#timmy.forward(100)
# a square

# dashed line
#for i in range(5):
    #timmy.forward(10)
    #timmy.penup()
    #timmy.forward(10)
    #timmy.pendown()
# dashed line

# maths shapes
colour = ["red", 'blue','green','dark green','pink', 'yellow','dark blue', 'dark red','deep pink', 'cyan']
#for n in (3,4,5,6,7,8,10,12):
    #timmy.color(choice(colour))
    #for i in range (n):
        #timmy.forward(100)
        #timmy.right(360/n)
#maths shapes
turtle.colormode(255)
def random_colour():
    r = randint(0,255)
    b = randint(0,255)
    g = randint(0,255)
    colour = (r,g,b)
    return colour
# draw a random walk
timmy.pensize(1)
angle = [90,180,270,360]
timmy.speed('fastest')
# for i in range (100):
#     timmy.color(random_colour())
#     timmy.forward(50)
#     timmy.setheading(choice(angle))
#draw a random walk

#draw a spirograph
# def draw_spiro(gap):
#     for i in range(int(360/gap)):
#         timmy.color(random_colour())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + gap)
#
# draw_spiro(5)
#draw a spirograph



screen.exitonclick()