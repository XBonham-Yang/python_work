import colorgram
import turtle as t
import random
#get all the colours out
colors = colorgram.extract('hi.jpg', 30)

# c_list = []
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb = (r,g,b)
#     c_list.append(rgb)
#
# print(c_list)
# Now I got all the colours
colour_list = [(225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
 (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
 (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79),
 (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177),
 (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

timmy = t.Turtle()
screen = t.Screen()
timmy.speed('fastest')
timmy.penup()
timmy.goto(-300,-300)
t.colormode(255)


def line(dot_num):
    for i in range(dot_num):
        timmy.dot(20, random.choice(colour_list))
        timmy.penup()
        timmy.forward(50)


def go_up(turn):
    timmy.backward(50)
    timmy.setheading(90)
    timmy.penup()
    timmy.forward(50)
    timmy.setheading(turn)



for i in range(5):
    line(10)
    go_up(180)
    line(10)
    go_up(0)

screen.exitonclick()
