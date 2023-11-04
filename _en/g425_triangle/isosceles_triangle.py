"""Draw Isosceles Triangles

Some Useful Information:
1. Given vertex angle and length of legs, the program draws the isosceles triangle and
   displays its base angle and base length.
"""

import turtle


MAX_LEG_LENGTH = 500
VERTEX_Y = 200

# Input vertex angle and calculate base angle.
vertex_angle = float(input('Enter the vertex angle: '))
while True:
    if 0 < vertex_angle < 180:
        break
    print('An angle of a triangle must be in the range (0, 180).')
    vertex_angle = float(input('Enter again: '))
base_angle = (180 - vertex_angle) / 2
if int(vertex_angle) == vertex_angle:
    vertex_angle = int(vertex_angle)
if int(base_angle) == base_angle:
    base_angle = int(base_angle)

# Input length of legs.
leg = float(input(f'Enter the length of legs (0 - {MAX_LEG_LENGTH}): '))
while True:
    if 0 < leg <= MAX_LEG_LENGTH:
        break
    print(f'The length of legs must be in the range (0, {MAX_LEG_LENGTH}].')
    leg = float(input('Enter again: '))
if int(leg) == leg:
    leg = int(leg)

# Draw the isosceles triangle.
screen = turtle.Screen()
pen = turtle.Turtle()
pen.up()
pen.goto(0, VERTEX_Y)
pen.down()
pen.right(90 - vertex_angle / 2)
pen.forward(leg)
point = pen.position()
pen.backward(leg)
pen.right(vertex_angle)
pen.forward(leg)
pen.left(180 - base_angle)
# Get the distance between the two ends of the base which is the length of the base.
base = pen.distance(point)
pen.forward(base)

print(f'\nVertex Angle: {vertex_angle}  Base Angle: {base_angle}  Legs: {leg}  Base: {round(base)}')

screen.exitonclick()
