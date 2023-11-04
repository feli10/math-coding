"""画等腰三角形

关于程序的几点说明： 
1. 用户输入等腰三角形的顶角和腰长，程序画出等腰三角形，并给出底角和底边长。
"""

import turtle


MAX_LEG_LENGTH = 500
VERTEX_Y = 200

# 输入顶角，计算底角。
vertex_angle = float(input('请输入等腰三角形的顶角: '))
while True:
    if 0 < vertex_angle < 180:
        break
    print('三角形的内角必须大于 0 度且小于 180 度。')
    vertex_angle = float(input('请重新输入: '))
base_angle = (180 - vertex_angle) / 2
if int(vertex_angle) == vertex_angle:
    vertex_angle = int(vertex_angle)
if int(base_angle) == base_angle:
    base_angle = int(base_angle)

# 输入腰长。
leg = float(input(f'请输入腰长 (0 - {MAX_LEG_LENGTH}): '))
while True:
    if 0 < leg <= MAX_LEG_LENGTH:
        break
    print(f'腰长必须在 (0, {MAX_LEG_LENGTH}] 范围内。')
    leg = float(input('请重新输入: '))
if int(leg) == leg:
    leg = int(leg)

# 画等腰三角形。
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
# 获取底边两端点之间的距离，也就是底边长。
base = pen.distance(point)
pen.forward(base)

print(f'\n顶角: {vertex_angle}  底角: {base_angle}  腰长: {leg}  底长: {round(base)}')

screen.exitonclick()
