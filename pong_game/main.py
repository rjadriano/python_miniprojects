from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
"""PONG GAME"""
# Create board
screen = Screen()
screen.bgcolor('black')
screen.setup(width=1000, height=600)
screen.title("Pong Game")

screen.tracer(0)

board_dash = Turtle()
board_dash.pencolor('white')
board_dash.pensize(5)
# draw dashed
board_height = 300
board_dash.teleport(0,board_height)
while board_height > -300:
    board_height -= 20
    board_dash.goto(0, board_height)
    board_dash.penup()
    board_height -= 20
    board_dash.goto(0, board_height)
    board_dash.pendown()

# Create Paddle
r_paddle = Paddle((-450,0))
l_paddle = Paddle((450,0))

screen.listen()
screen.onkeypress(r_paddle.up,'w')
screen.onkeypress(r_paddle.down,'s')
screen.onkeypress(l_paddle.up,'Up')
screen.onkeypress(l_paddle.down,'Down')

#Create Ball
ball = Ball()
#Create Score
l_score = Scoreboard((-40,240))
r_score = Scoreboard((40,240))


is_game_over = False
while not is_game_over:
    time.sleep(ball.move_speed)

    screen.update()
    ball.move()

    # Detect Wall Collision
    if ball.ycor() > 280  or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.xcor() == l_paddle.xcor() and ball.distance(l_paddle) < 50 ) or (ball.xcor() == r_paddle.xcor() and ball.distance(r_paddle) < 50):
        ball.bounce_x()

    #Detect score
    if ball.xcor() > 500 :
        l_score.add_score()
        ball.reset()
    if ball.xcor() < -500:
        r_score.add_score()
        ball.reset()
