"""随机生成轴对称图形"""

import turtle
from random import randint
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


MAX_Y = 400
MIN_X = 100
MAX_X = 300


def random_list(minimum, maximum, n):
    """随机生成一个随机数列表，列表中有位于 minimum 和 maximum 之间的 n 个随机数。
    
    minimum/maximum: 列表中随机数的取值范围。
    n: 列表中的元素数。
    """
    return [randint(minimum, maximum) for _ in range(n)]


n = int(input_natural_number('在对称轴一侧随机生成多少个点 (1-50)? ', 1, 50))
# 还有两个点位于对称轴上。
n += 2
# 生成 n 个点的 x 和 y 位置坐标。
points_y = sorted(random_list(-MAX_Y, MAX_Y, n))
points_x = [0] + random_list(MIN_X, MAX_X, n - 2) + [0]

screen = turtle.Screen()
pen = turtle.Turtle()

# 画对称轴。
pen.color('lightgray')
pen.up()
pen.goto(0, MAX_Y)
pen.down()
pen.goto(0, -MAX_Y)

# 画轴对称图形。
pen.color('black')
pen.up()
pen.goto(points_x[0], points_y[0])
pen.down()
# 画对称轴右侧的一半图形。
for i in range(1, n - 1):
    pen.goto(points_x[i], points_y[i])
# 画对称轴左侧的另一半图形。
for i in range(n - 1, -1, -1):
    pen.goto(-points_x[i], points_y[i])

screen.exitonclick()
