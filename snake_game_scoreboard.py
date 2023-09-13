from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", False, align="center")
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", False, align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center")
