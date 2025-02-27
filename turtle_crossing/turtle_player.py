from turtle import Turtle
STARTING_POSITION = (0, -280)

class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.setheading(90)
        self.forward(20)

    def reset(self):
        self.goto(STARTING_POSITION)

    def move_back(self):
        self.setheading(270)
        self.forward(20)

    def move_left(self):
        self.setheading(180)
        self.forward(20)

    def move_right(self):
        self.setheading(0)
        self.forward(20)