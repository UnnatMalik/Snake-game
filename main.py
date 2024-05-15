from turtle import Screen
from snake_body import Snake
from Food import Food
from Score import Score
import time

# window setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=700,height=700)
screen.title("Snake game")
screen.tracer(0)

#snake class
nigga = Snake()
food = Food()
score = Score()
#controls for the snake
screen.onkey(fun=nigga.up, key="w")
screen.onkey(fun=nigga.down, key="s")
screen.onkey(fun=nigga.left, key="a")
screen.onkey(fun=nigga.right, key="d")
screen.listen()

check = True
i = 0
#keeps moving the snake
while check :
    i += 1
    screen.update()
    time.sleep(0.1)
    nigga.move()
    if nigga.head.distance(food) < 15:
        food.new_food()
        nigga.extend()
        score.score_update()
    if nigga.head.xcor() > 340 or nigga.head.xcor() < -340 :
        score.game_over()
        check = False

    if nigga.head.ycor() > 340 or nigga.head.ycor() < -340 :
        score.game_over()
        check = False
    
    for segment in nigga.snakes[1:]:
        if nigga.head.distance(segment) < 10 :
            score.game_over()
            check = False
            break

screen.exitonclick()