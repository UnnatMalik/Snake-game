from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 18, "normal")



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 320)
        with open("data.txt",mode="r") as data :
            self.high_score = int(data.read())
        self.point = 0
        self.shapesize(0.1, 0.1)
        self.color("White")
        self.speed(0)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.color("Green")
        self.write(arg=f"Score : {self.point} | High score = {self.high_score}", align=ALIGNMENT, move=False, font=FONT)

    def score_update(self):
        self.point += 1
        self.score_board()

    def High_score(self):
        if self.point > self.high_score:
            self.high_score = self.point
            with open("data.txt",mode="w") as data :
                data.write(str(self.high_score))
        self.point = 0
        self.score_board()
        
    def game_exit():
        return False