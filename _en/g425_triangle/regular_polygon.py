"""Draw Regular Polygons

Some Useful Information:
1. The program includes two methods to draw regular polygons, you can choose one to use at a time.
"""

import turtle

# Radius of the regular polygon (length between center and vertices).
RADIUS = 400


def draw_regular_polygon1(n):
    """Draw a regular polygon by first getting the length of sides.
    
    n: number of sides of the regular polygon.
    """
    ANGLE = 360 / n
    # Get the length of sides.
    pen.pencolor('lightgray')
    pen.left(90 - ANGLE / 2)
    pen.forward(RADIUS)
    point = pen.position()
    pen.backward(RADIUS)
    pen.left(ANGLE)
    pen.forward(RADIUS)
    # Length of sides is the distance between adjacent vertices.
    side = pen.distance(point)
    # Draw the regular polygon with the length of sides.
    pen.setheading(0)
    pen.pencolor('black')
    for _ in range(n):
        pen.forward(side)
        pen.right(ANGLE)


def draw_regular_polygon2(n):
    """Draw a regular polygon with a leading turtle as helper. The leading turtle is responsible for
    finding the next vertex of the regular polygon, and when it does, the pen goes to the leading
    turtle from the previous vertex.

    n: number of sides of the regular polygon.
    """
    ANGLE = 360 / n
    lead = turtle.Turtle()
    lead.shape('turtle')
    lead.pencolor('lightgrey')
    # Each time lead gets to the next vertex of the regular polygon, pen follows.
    lead.left(90 + ANGLE / 2)
    lead.forward(RADIUS)
    pen.up()
    pen.goto(lead.position())
    pen.down()
    for _ in range(n):
        lead.backward(RADIUS)
        lead.right(ANGLE)
        lead.forward(RADIUS)
        pen.goto(lead.position())


screen = turtle.Screen()
pen = turtle.Turtle()
# Select one of the following two lines to execute and comemnt out the other line.
draw_regular_polygon1(8)
# draw_regular_polygon2(8)

screen.exitonclick()
