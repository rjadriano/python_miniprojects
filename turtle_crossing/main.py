import time
from turtle import Screen
from turtle_player import TurtlePlayer
from car import Car
from levelboard import Level

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Turtle")
screen.tracer(0)

turtle_player = TurtlePlayer()

screen.listen()
screen.onkeypress(turtle_player.move,'w')
screen.onkeypress(turtle_player.move_back,'s')
screen.onkeypress(turtle_player.move_left,'a')
screen.onkeypress(turtle_player.move_right,'d')


def stop_listening():
    screen.onkeypress(None, "w")
    screen.onkeypress(None, "s")
    screen.onkeypress(None, "a")
    screen.onkeypress(None, "d")

level_score = Level()

is_game_over = False
new_car_ctr = 6
cars = []
while not is_game_over:
    time.sleep(0.07)
    screen.update()

    #Deploy Car
    if new_car_ctr == 6:
        new_car_ctr = 0
        cars.append(Car(level_score.speed_level))
    new_car_ctr += 1

    #Car Movement and Detect Collision
    for car in cars:
        car.move()
        if turtle_player.distance(car) < 30:
            #GAME OVER
            level_score.game_over()
            car.color('black')
            stop_listening()

    # Detect Level Clear
    if turtle_player.ycor() > 280:
        level_score.add_level()
        turtle_player.reset()
