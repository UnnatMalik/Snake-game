from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 18, "normal")



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 320)
        self.point = 0
        self.shapesize(0.1, 0.1)
        self.color("White")
        self.speed(0)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.color("Green")
        self.write(arg=f"Score : {self.point}", align=ALIGNMENT, move=False, font=FONT)

    def score_update(self):
        self.clear()
        self.point += 1
        self.score_board()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("Yellow")
        self.write(arg="Game Over", align=ALIGNMENT, move=False, font=FONT)
