
from turtle import Turtle


class MiddleDash(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=0.2, stretch_wid=0.5)
