import random
from turtle import Turtle

COLORS = ["red","blue","violet","green","orange","pink","brown"]
CAR_NUMBER = 3
X_START = 280

class Car(Turtle):
    def __init__(self,speed_level):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.shape("square")
        self.penup()
        self.goto(X_START,random.randint(-230,250))
        self.setheading(180)
        self.speed(1)
        self.speed_level = speed_level


    def move(self):
        self.forward(self.speed_level)

