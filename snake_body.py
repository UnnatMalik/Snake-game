from turtle import Screen, Turtle
import time

# constants
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


# snake class
class Snake:

    def __init__(self):
        self.snakes = []
        self.create()
        self.move()
        self.head = self.snakes[0]
    # snake creation
    def create(self):
        for i in POSITION:
            self.create_new(i)

    def create_new(self,i):
            snake = Turtle(shape="square")
            snake.color("Green")
            snake.penup()
            snake.goto(i)
            self.snakes.append(snake)
    # to elongate the snake
    def extend(self):
        self.create_new(self.snakes[-1].position())
    # to keep moving the snake
    def move(self):
        for num in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[num - 1].xcor()
            y = self.snakes[num - 1].ycor()
            self.snakes[num].goto(x, y)
        self.snakes[0].fd(MOVE)
    
    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create()
        self.head = self.snakes[0]
    
    # to control snake direction
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
