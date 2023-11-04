"""图形绕一点旋转"""

import turtle
from random import randint


# 图形逆时针旋转的旋转角度。
ROTATION = 75
# 旋转中心的坐标。
POINT = (100, -200)
# 图形的每一条边都具有不同的颜色，方便区分图形旋转前后的对应边。
COLORS = ['black', 'red', 'orange', 'gold', 'green', 'blue', 'purple', 'brown']
THICKNESS = 5
DOTSIZE = 15
MIN_SIDE_COUNT = 3
MAX_SIDE_COUNT = len(COLORS)
MIN_SIDE_LENGTH = 100
MAX_SIDE_LENGTH = 200


def draw_regular_polygon():
    """画一个正多边形。"""
    pen.pensize(THICKNESS)
    pen.dot(DOTSIZE)
    for i in range(n):
        pen.color(COLORS[i])
        pen.forward(side)
        pen.left(360/n)


screen = turtle.Screen()
pen = turtle.Turtle()
# 随机生成正多边形的边数和边长。
n = randint(MIN_SIDE_COUNT, MAX_SIDE_COUNT)
side = randint(MIN_SIDE_LENGTH, MAX_SIDE_LENGTH)

# 画旋转前的正多边形。
draw_regular_polygon()

# 画旋转中心和旋转标记线。
pen.pencolor('lightgray')
pen.pensize(1)
pen.goto(POINT)
pen.dot(DOTSIZE, 'red')
# 找到旋转后的起始点。
pen.setheading(pen.towards(0, 0))
pen.left(ROTATION)
pen.forward(pen.distance(0, 0))
# 设置旋转后起始边的角度。
pen.setheading(ROTATION)

# 画旋转后的正多边形。
draw_regular_polygon()
pen.hideturtle()

screen.exitonclick()
