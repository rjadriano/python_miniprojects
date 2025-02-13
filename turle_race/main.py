import random
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make a Bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','blue','purple','green','orange','pink','black']

turtles = {}
y_position = -80
for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].penup()
    turtles[color].color(color)
    turtles[color].goto(-230,y_position)
    y_position += 30

game_over = False
while not game_over:
    for color in turtles:
        turtles[color].forward(random.randint(0,25))
        """Check Winning turtle"""
        if round(turtles[color].xcor(), 0) >= 220:
            if user_bet == color:
                print(f"You Win! {color} Turtle wins the race ")
            else:
                print(f"You Lose! {color} Turtle wins the race ")
            game_over = True

screen.exitonclick()
