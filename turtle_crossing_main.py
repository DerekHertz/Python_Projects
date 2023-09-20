import time
from turtle import Screen
from player import Player
from car_manager import CarManager, COLORS
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []
num_cars = 10
for i in range(num_cars):
    car = CarManager()
    cars.append(car)


screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_back, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if len(cars) < num_cars and random.randint(1, 6) == 1:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.drive()
        if car.xcor() < -320:
            cars.remove(car)
            car.goto(x=320, y=random.randint(-250, 250))
            car.color(random.choice(COLORS))
            car.increase_speed()
            num_cars += 5

        if player.ycor() == 270 and car.distance(player) > 50:
            scoreboard.next_level()
            car.increase_speed()
            player.goto(0, -280)

        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
