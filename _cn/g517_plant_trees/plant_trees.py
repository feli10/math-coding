"""植树问题"""

import turtle
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


ROAD = 800
RADIUS = 300
TRUNK_HEIGHT = 40
LEAVES_SIZE = 50
TREE_FONT_SIZE = 24
GAP_FONT_SIZE = 32
# Turtle 的速度可以是 0 到 10 之间的整数，或速度字符串。速度字符串与速度值的对应关系如下：
# 'fastest': 0; 'fast': 10; 'normal': 6; 'slow': 3 (默认值); 'slowest': 1.
SPEED = 'fast'


def draw_a_tree(num, closed=False):
    """画一棵树并标出树的编号。
    
    num: 树的编号。
    closed: 所画的树是否在闭合的环路上。
    """
    if not closed:
        pen.left(90)
    pen.down()
    # 画树干。
    pen.pensize(15)
    pen.color('brown')
    pen.forward(TRUNK_HEIGHT)

    # 画树叶。
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

    # 标出树的编号。
    pen.up()
    pen.forward(LEAVES_SIZE + TREE_FONT_SIZE)
    pen.color('black')
    pen.write(num, align='center', font=('Arial', TREE_FONT_SIZE, 'normal'))
    pen.backward(LEAVES_SIZE + TREE_FONT_SIZE)

    # 把 pen 复原到画这棵树之前的状态。
    pen.backward(TRUNK_HEIGHT)
    if not closed:
        pen.right(90)


def draw_trees(count=4):
    """在直路上植树，并标出树的棵树和间隔数。

    count: 树的数量。
    """
    # 画一条直路。
    pen.pensize(5)
    pen.up()
    pen.backward(ROAD / 2)
    pen.down()
    pen.forward(ROAD)
    pen.up()
    pen.backward(ROAD)

    # 画出所有树并给树编号。
    distance = ROAD / (count - 1)
    draw_a_tree(1)
    for i in range(count - 1):
        pen.forward(distance)
        draw_a_tree(i + 2)

    # 数出间隔数。
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
    """在环路上植树，并标出树的棵树和间隔数。

    count: 树的数量。
    """
    # 画一条环路。
    pen.speed('fastest')
    pen.pensize(5)
    pen.up()
    pen.goto(0, -RADIUS)
    pen.down()
    pen.circle(RADIUS)
    pen.up()
    pen.goto(0, 0)
    pen.speed(SPEED)

    # 画出所有树并给树编号。
    angle = 360 / count
    pen.left(90)
    for i in range(count):
        pen.forward(RADIUS)
        draw_a_tree(i + 1, True)
        pen.backward(RADIUS)
        pen.right(angle)

    # 数出间隔数。
    pen.speed('slow')
    pen.color('red')
    pen.right(angle / 2)
    for i in range(count):
        pen.forward(RADIUS + GAP_FONT_SIZE * 2)
        pen.write(i + 1, align='center', font=('Arial', GAP_FONT_SIZE, 'normal'))
        pen.backward(RADIUS + GAP_FONT_SIZE * 2)
        pen.right(angle)

    pen.hideturtle()


tree_count = int(input_natural_number('植多少棵树 (2-20)? ', 2, 20))
closed = input('是否是闭合的环路 (y/n)? ')

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(SPEED)

if closed not in ('y', 'Y', '是', '对'):
    draw_trees(tree_count)
else:
    draw_trees_closed(tree_count)

screen.exitonclick()
