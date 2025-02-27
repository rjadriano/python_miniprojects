from turtle import Turtle
FONT = ('Arial',15,'normal')

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280,260)
        self.level = 1
        self.update_level()
        self.hideturtle()
        self.speed_level = 5

    def update_level(self):
        self.write(f"Level : {self.level}",align='left', font=FONT)

    def add_level(self):
        self.level += 1
        self.speed_level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.color('red')
        self.goto(0,0)
        self.write(f"GAME OVER! You finished level {self.level}",align='center', font=('Arial',20,'bold'))

