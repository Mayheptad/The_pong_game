

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self, pos):
        self.position = pos
        super().__init__()
        self.scores = 0
        self.penup()
        self.pensize(20)
        self.hideturtle()
        self.color('white')
        self.write_scores(position=pos)

    def write_scores(self, position):
        self.goto(position)
        self.write(self.scores, align=ALIGNMENT, font=FONT)

    def increase_scores(self):
        self.clear()
        self.scores += 1
        self.write_scores(position=self.pos())

