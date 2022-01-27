
from turtle import Screen
from paddle import Paddle
from ball import Ball
from middledash import MiddleDash
from scoreboard import ScoreBoard
import time


Screen().setup(width=800, height=600)
Screen().bgcolor('black')
Screen().title('THE PONG GAME')
Screen().tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball((0, 0))

sb_left = ScoreBoard((-50, 200))
sb_right = ScoreBoard((50, 200))

middle_dash_arr = []
middle_dash_pos = [(0, 0), (0, 20), (0, 40), (0, 60), (0, 80), (0, 100), (0, 120), (0, 140), (0, 160), (0, 180),
                   (0, 200), (0, 220), (0, 240), (0, 260), (0, 280), (0, 300), (0, 320), (0, 340), (0, -20), (0, -40),
                   (0, -60), (0, -80), (0, -100), (0, -120), (0, -140), (0, -160), (0, -180), (0, -200), (0, -220),
                   (0, -240), (0, -260), (0, -280), (0, -300), (0, -320), (0, -340)]


for nums in range(len(middle_dash_pos)):
    md = MiddleDash()
    middle_dash_arr.append(md)

for num in range(len(middle_dash_pos)):
    middle_dash_arr[num].goto(middle_dash_pos[num])

Screen().listen()
Screen().onkey(fun=r_paddle.go_up, key='Up')
Screen().onkey(fun=r_paddle.go_down, key='Down')

Screen().onkey(fun=l_paddle.go_up, key='w')
Screen().onkey(fun=l_paddle.go_down, key='s')


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    Screen().update()
    ball.move()

    # detect ball collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect ball collision with left and right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if ball pass through the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        sb_left.increase_scores()

    # detect if ball pass through the right paddle
    if ball.xcor() < -380:
        ball.reset_position()
        sb_right.increase_scores()


Screen().exitonclick()


