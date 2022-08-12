from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.write(f"Score = {self.score} ", False, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()


    def get_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.color('white')
        self.write("GAME OVER", align="center", font = ("Arial", 32, "normal"))
