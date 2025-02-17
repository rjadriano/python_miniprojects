from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position)

    def up(self):
        x = self.xcor()
        new_y = self.ycor()
        self.goto(x,new_y + 20)

    def down(self):
        x = self.xcor()
        new_y = self.ycor()
        self.goto(x, new_y - 20)
