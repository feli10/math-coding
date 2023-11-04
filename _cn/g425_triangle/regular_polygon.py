"""画正多边形

关于程序的几点说明： 
1. 程序使用了两种方法画正多边形，可每次选择一种方法运行。
"""

import turtle

# 正多边形中心到顶点的距离。
RADIUS = 400


def draw_regular_polygon1(n):
    """首先获取边长，再根据边长画正多边形。
    
    n: 正多边形的边数。
    """
    ANGLE = 360 / n
    # 获取边长。
    pen.pencolor('lightgray')
    pen.left(90 - ANGLE / 2)
    pen.forward(RADIUS)
    point = pen.position()
    pen.backward(RADIUS)
    pen.left(ANGLE)
    pen.forward(RADIUS)
    # 正多边形相邻两个顶点的距离就是边长。
    side = pen.distance(point)
    # 根据边长画正多边形。
    pen.setheading(0)
    pen.pencolor('black')
    for _ in range(n):
        pen.forward(side)
        pen.right(ANGLE)


def draw_regular_polygon2(n):
    """使用一个辅助 turtle (lead) 协助画图 turtle (pen) 画出正多边形。lead 每次到达下一个顶点，
    pen 就从前一个顶点跟随过来画出一条边。

    n: 正多边形的边数。
    """
    ANGLE = 360 / n
    lead = turtle.Turtle()
    lead.shape('turtle')
    lead.pencolor('lightgrey')
    # lead 每次到达下一个顶点，pen 就从前一个顶点跟随过来画出一条边。
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
# 以下两行每次选一行执行，注销另一行。
draw_regular_polygon1(8)
# draw_regular_polygon2(8)

screen.exitonclick()
