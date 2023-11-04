"""Rotation around a point"""

import turtle
from random import randint


# Angle of counterclockwise rotation.
ROTATION = 75
# Coordinates of the center of rotation.
POINT = (100, -200)
# Sides with different colors can help distinguish between sides before and after rotation.
COLORS = ['black', 'red', 'orange', 'gold', 'green', 'turquoise', 'blue', 'violet']
THICKNESS = 5
DOTSIZE = 15
MIN_SIDE_COUNT = 3
MAX_SIDE_COUNT = len(COLORS)
MIN_SIDE_LENGTH = 100
MAX_SIDE_LENGTH = 200


def draw_regular_polygon():
    """Draw a regular polygon."""
    pen.pensize(THICKNESS)
    pen.dot(DOTSIZE)
    for i in range(n):
        pen.color(COLORS[i])
        pen.forward(side)
        pen.left(360/n)


screen = turtle.Screen()
pen = turtle.Turtle()
# Generate the number and length of sides of a regular polygon randomly.
n = randint(MIN_SIDE_COUNT, MAX_SIDE_COUNT)
side = randint(MIN_SIDE_LENGTH, MAX_SIDE_LENGTH)

# Draw a regular polygon before rotation.
draw_regular_polygon()

# Draw the center of rotation and the marking lines.
pen.pencolor('lightgray')
pen.pensize(1)
pen.goto(POINT)
pen.dot(DOTSIZE, 'red')
# Find the starting point after rotation.
pen.setheading(pen.towards(0, 0))
pen.left(ROTATION)
pen.forward(pen.distance(0, 0))
# Set the angle of the starting side after rotation.
pen.setheading(ROTATION)

# Draw a regular polygon after rotation.
draw_regular_polygon()
pen.hideturtle()

screen.exitonclick()
