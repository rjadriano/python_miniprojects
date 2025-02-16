import random
from turtle import Turtle

BORDER = 280
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(.5,.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-BORDER, BORDER)
        ran_y = random.randint(-BORDER, BORDER)
        self.goto(ran_x, ran_y)