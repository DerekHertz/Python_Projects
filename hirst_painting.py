import colorgram
import random
from turtle import *

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156),
              (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120),
              (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239),
              (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241),(5, 68, 42)]

create_dot = Turtle()
screen = Screen()

directions = [0, 90, 180, 270]
colormode(255)
create_dot.speed(0)
create_dot.up()
create_dot.setx(-200)
create_dot.sety(-200)
switch = 0


def make_row(num_dots):

    for i in range(num_dots):

        create_dot.dot(20, random.choice(color_list))
        create_dot.up()
        create_dot.forward(40)
        create_dot.down()
        create_dot.dot(20, random.choice(color_list))


def move_up():

    if switch == 0:
        create_dot.setheading(90)
        create_dot.up()
        create_dot.forward(40)
        create_dot.down()
        create_dot.setheading(180)
    else:
        create_dot.setheading(90)
        create_dot.up()
        create_dot.forward(40)
        create_dot.down()
        create_dot.setheading(0)


num_dots = int(input("How many dots would you like in a row?"))

num_rows = int(input("How many rows would you like?"))


for i in range(num_rows):

    make_row(num_dots - 1)

    if i % 2 == 0:

        switch = 0

    else:

        switch = 1

    move_up()

screen.exitonclick()

