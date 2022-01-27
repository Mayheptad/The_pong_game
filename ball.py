
from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.speed('fastest')
        self.color('yellow')
        self.penup()
        self.shapesize(stretch_len=1.0, stretch_wid=1.0)
        self.goto(position)
        self.y_axis = 10
        self.x_axis = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_axis, self.ycor() + self.y_axis)

    def bounce_y(self):
        self.y_axis *= -1

    def bounce_x(self):
        self.x_axis *= -1
        # increase ball movement speed very time it hit a paddle
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto((0, 0))
        self.move_speed = 0.1
        self.bounce_x()


