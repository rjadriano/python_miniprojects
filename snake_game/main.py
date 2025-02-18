"""Snake Game"""
"""
4. creating the food / eating the food / adding length to the snake
5. score tracking
6.wall collision - game over
7.tail/self collision - game over
"""
import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create Snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(.1)

    snake.move()

    # Detect food collision
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.add_score()

    # Detect wall collision
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
