from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        """Create a three segment snake"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        snake_body = Turtle()
        snake_body.color("white")
        snake_body.shape("square")
        snake_body.penup()
        snake_body.goto(position)
        self.snake.append(snake_body)

    def extend_snake(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) -1,0,-1):
            new_x = self.snake[seg_num -1].xcor()
            new_y = self.snake[seg_num -1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
