from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

#etch_a-sketh
def forward():
    tim.forward(10)


def back():
    tim.backward(10)


def left():
    tim.setheading(tim.heading() + 10)


def right():
    tim.setheading(tim.heading() - 10)


def clean():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()


screen.onkey(key = "w", fun = forward)
screen.onkey(key = "s", fun = back)
screen.onkey(key = "a", fun = left)
screen.onkey(key = "d", fun = right)
screen.onkey(key = "c", fun = clean)
screen.exitonclick()
#etch_a-sketh