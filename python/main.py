from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
Scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.right , "Right")
screen.onkey(snake.left , "Left")

 
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if(snake.head.distance(food)<14):
        food.refresh()
        snake.create_segment()
        Scoreboard.increase()
        # snake.create_snake()

    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor()<-280:
        is_game_on = False
        Scoreboard.game_over()

    for segment in snake.segement[1:len(snake.segement)]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            Scoreboard.game_over()

        

screen.exitonclick() 