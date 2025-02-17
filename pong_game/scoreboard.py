from turtle import Turtle
FONT = ('Arial',40,'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.goto(position)
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
