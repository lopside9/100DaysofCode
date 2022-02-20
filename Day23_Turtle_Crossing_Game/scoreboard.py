from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-270, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setposition(POSITION)
        self.write("Score: ", align="left", font=FONT)
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
