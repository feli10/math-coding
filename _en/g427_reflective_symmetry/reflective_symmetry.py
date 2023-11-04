"""Genreate a mirror-symmetric shape."""

import turtle
from random import randint
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


MAX_Y = 400
MIN_X = 100
MAX_X = 300


def random_list(minimum, maximum, n):
    """Randomly generate a list of n random numbers between minimum and maximum.
    
    minimum/maximum: the range of the numbers in the list.
    n: number of elements in the list.
    """
    return [randint(minimum, maximum) for _ in range(n)]


n = int(input_natural_number('Generate how many points on one side (1-50)? ', 1, 50))
# There are two points on the line of symmetry.
n += 2
# Generate x and y positions for n points.
points_y = sorted(random_list(-MAX_Y, MAX_Y, n))
points_x = [0] + random_list(MIN_X, MAX_X, n - 2) + [0]

screen = turtle.Screen()
pen = turtle.Turtle()

# Draw line of symmetry.
pen.color('lightgray')
pen.up()
pen.goto(0, MAX_Y)
pen.down()
pen.goto(0, -MAX_Y)

# Draw a mirror-symmetric shape.
pen.color('black')
pen.up()
pen.goto(points_x[0], points_y[0])
pen.down()
# Draw half on right side of the ine of symmetry.
for i in range(1, n - 1):
    pen.goto(points_x[i], points_y[i])
# Draw another half on left side of the ine of symmetry.
for i in range(n - 1, -1, -1):
    pen.goto(-points_x[i], points_y[i])

screen.exitonclick()
