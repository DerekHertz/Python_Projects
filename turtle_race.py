from turtle import *
from random import *

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = []
y_cord = -175

for i in range(len(colors)):

    j = Turtle(shape='turtle')
    j.color(colors[i])

    j.up()
    j.goto(x=-225, y=y_cord)
    y_cord += 66

    turtles.append(j)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

