"""The relation between number of trees and number of gaps between trees."""

import turtle
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


ROAD = 800
RADIUS = 300
TRUNK_HEIGHT = 40
LEAVES_SIZE = 50
TREE_FONT_SIZE = 24
GAP_FONT_SIZE = 32
# Turtle speed can be an integer between 0 and 10 or a string mapped to speed values as follows:
# 'fastest': 0; 'fast': 10; 'normal': 6; 'slow': 3 (default); 'slowest': 1.
SPEED = 'fast'


def draw_a_tree(num, closed=False):
    """Draw a tree and write the tree number.
    
    num: the tree number.
    closed: whether to draw the tree in a closed shape road?
    """
    if not closed:
        pen.left(90)
    pen.down()
    # Draw a trunk.
    pen.pensize(15)
    pen.color('brown')
    pen.forward(TRUNK_HEIGHT)

    # Draw leaves.
    pen.right(90)
    pen.pensize(5)
    pen.color('green')
    pen.begin_fill()
    pen.forward(LEAVES_SIZE / 2)
    for _ in range(2):
        pen.left(120)
        pen.forward(LEAVES_SIZE)
    pen.left(120)
    pen.forward(LEAVES_SIZE / 2)
    pen.end_fill()
    pen.left(90)

    # Write the tree number.
    pen.up()
    pen.forward(LEAVES_SIZE + TREE_FONT_SIZE)
    pen.color('black')
    pen.write(num, align='center', font=('Arial', TREE_FONT_SIZE, 'normal'))
    pen.backward(LEAVES_SIZE + TREE_FONT_SIZE)

    # Reset pen to the state before drawing this tree.
    pen.backward(TRUNK_HEIGHT)
    if not closed:
        pen.right(90)


def draw_trees(count=4):
    """Draw trees on a straight road and count the number of gaps between the trees.
    
    count: number of trees to draw.
    """
    # Draw a line representing an open shape road.
    pen.pensize(5)
    pen.up()
    pen.backward(ROAD / 2)
    pen.down()
    pen.forward(ROAD)
    pen.up()
    pen.backward(ROAD)

    # Draw trees and write tree numbers.
    distance = ROAD / (count - 1)
    draw_a_tree(1)
    for i in range(count - 1):
        pen.forward(distance)
        draw_a_tree(i + 2)

    # Write gap numbers.
    pen.backward(ROAD - distance / 2)
    pen.speed('slow')
    pen.color('red')
    for i in range(count - 1):
        pen.right(90)
        pen.forward(GAP_FONT_SIZE * 2)
        pen.write(i + 1, align='center', font=('Arial', GAP_FONT_SIZE, 'normal'))
        pen.backward(GAP_FONT_SIZE * 2)
        pen.left(90)
        pen.forward(distance)

    pen.hideturtle()


def draw_trees_closed(count=4):
    """Draw trees on a circular road and count the number of gaps between the trees.
    
    count: number of trees to draw.
    """
    # Draw a circle representing a closed shape road.
    pen.speed('fastest')
    pen.pensize(5)
    pen.up()
    pen.goto(0, -RADIUS)
    pen.down()
    pen.circle(RADIUS)
    pen.up()
    pen.goto(0, 0)
    pen.speed(SPEED)

    # Draw trees and write tree numbers.
    angle = 360 / count
    pen.left(90)
    for i in range(count):
        pen.forward(RADIUS)
        draw_a_tree(i + 1, True)
        pen.backward(RADIUS)
        pen.right(angle)

    # Write gap numbers.
    pen.speed('slow')
    pen.color('red')
    pen.right(angle / 2)
    for i in range(count):
        pen.forward(RADIUS + GAP_FONT_SIZE * 2)
        pen.write(i + 1, align='center', font=('Arial', GAP_FONT_SIZE, 'normal'))
        pen.backward(RADIUS + GAP_FONT_SIZE * 2)
        pen.right(angle)

    pen.hideturtle()


tree_count = int(input_natural_number('Number of trees (2-20): ', 2, 20))
closed = input('Is the road a closed shape (y/n)? ')

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(SPEED)

if closed not in ('y', 'Y', 'yes', 'Yes'):
    draw_trees(tree_count)
else:
    draw_trees_closed(tree_count)

screen.exitonclick()
