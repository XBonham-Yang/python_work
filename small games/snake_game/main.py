import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.get_point()
    # detect wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    # detect tail
    # for s in snake.snakebody:
    #     if s == snake.head:
    #         pass
    #     elif snake.head.distance(s) < 10:
    #         game_on = False
    #         scoreboard.game_over()
# It didn't work, head is always <10 to part 2...
for s in snake.snakebody[1:]:
    if snake.head.distance(s) <10:
        game_on = False
        scoreboard.game_over()
# this works but same logic.... don't know why this works

screen.exitonclick()
