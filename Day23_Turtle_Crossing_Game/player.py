from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        self.score = 0

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
