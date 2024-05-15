import random as rnd
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Yellow")
        self.speed(10)
        a = rnd.randint(-320, 320)
        b = rnd.randint(-320, 310)
        self.goto(x=a, y=b)

    def new_food(self):
        a = rnd.randint(-320, 320)
        b = rnd.randint(-320, 320)
        self.goto(x=a, y=b)
