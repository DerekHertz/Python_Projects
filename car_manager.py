from turtle import Turtle, colormode
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=280, y=random.randint(-250, 250))
        self.setheading(180)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def drive(self):
        self.forward(self.car_speed)

