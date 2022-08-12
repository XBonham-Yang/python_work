from turtle import Turtle
MOVESPEED = 5
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITION = [(0,0), (-20, 0), (-40,0)]
class Snake:
    def __init__(self):
        self.snakebody = []
        self.create_snake()
        self.head = self.snakebody[0]

    def create_snake(self):
        for i in POSITION:
            tim = Turtle()
            tim.shape('square')
            tim.color('white')
            tim.penup()
            tim.goto(i)
            self.snakebody.append(tim)

# this range thing(from len-1 ie the last block to 0 ie the head) goes backwards
    def move(self):
        for i in range(len(self.snakebody) - 1, 0, -1):
            new_x = self.snakebody[i - 1].xcor()
            new_y = self.snakebody[i - 1].ycor()
            self.snakebody[i].goto(new_x, new_y)
            self.snakebody[0].forward(MOVESPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_body(self, location):
        tim = Turtle()
        tim.shape('square')
        tim.color('white')
        tim.penup()
        tim.goto(location)
        self.snakebody.append(tim)

    def extend(self):
        self.add_body(self.snakebody[-1].position())