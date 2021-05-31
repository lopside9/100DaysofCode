# import colorgram
#
# colours = colorgram.extract('image.jpg', 30)
#
# rgb_colours = []
# # first_colour = colours[0]
# # rgb = first_colour.rgb
# # print(rgb)
# #
# # red = rgb.r
# # print(red)
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

# Start Code here
import random
import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("green")
screen = t.Screen()
t.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

# Colour list from the Damien Hirst image, and using the Colorgram module
colour_list = [
    (1, 12, 31), (53, 25, 17),
    (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24),
    (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
    (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85),
    (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)
]

# Code to check what the height of the canvas was to help set starting position
# print(screen.window_width())
# print(screen.window_height())

starting_x = -460
starting_y = -370
start_position = (starting_x, starting_y)
timmy.setpos(start_position)


def line_of_dots(rows, columns, initial_start_position):
    # Setting the new starting position for the drawing object
    new_start_position = initial_start_position
    # For each row do this
    for n in range(rows):
        # For each column do this
        for i in range(columns):
            timmy.forward(50)
            timmy.dot(20, random.choice(colour_list))
        # Setting a new starting position after each row is completed
        new_start_position = (new_start_position[0], new_start_position[1] + 50)
        timmy.setpos(new_start_position)


line_of_dots(10, 10, start_position)
screen.exitonclick()
