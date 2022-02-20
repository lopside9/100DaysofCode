import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

scoreboard = Scoreboard()
player_1 = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player_1.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_left()

    for car in car_manager.all_cars:
        if player_1.distance(car.position()) < 20:
            print("Oh no you got squished!")
            scoreboard.game_over()
            game_is_on = False

    if player_1.ycor() > 280:
        player_1.score += 1
        # print("You've reached the end!")
        # print(f"Your score is {player_1.score}")
        scoreboard.update_scoreboard()
        player_1.reset_position()
        car_manager.increase_car_speed()

screen.exitonclick()
