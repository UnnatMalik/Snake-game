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
snake = Snake()
food = Food()
score = Score()
#controls for the snake
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")
screen.listen()

check = True
i = 0
#keeps moving the snake
while check :
    i += 1
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score.score_update()
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 :
        score.High_score()
        time.sleep(2)
        snake.reset()
    
    if snake.head.ycor() > 340 or snake.head.ycor() < -340 :
        score.High_score()
        time.sleep(2)
        
        snake.reset()
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10 :
            score.High_score()
            time.sleep(2)
            
            snake.reset()

screen.exitonclick()