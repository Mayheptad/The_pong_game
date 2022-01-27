
from random import randint
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed('fastest')
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    # def move_paddle(self):
    #     self.speed('slowest')
    #     rand_y = randint(-300, 300)
    #     self.goto(self.xcor(), self.ycor() + 20)
    
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
