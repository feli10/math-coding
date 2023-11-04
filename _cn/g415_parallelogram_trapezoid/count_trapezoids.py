"""数梯形

关于程序的几点说明：
1. 随机生成的所有线段互不平行，以确保数梯形时不会出现平行四边形。
2. 调整常数值时需确保 LENGTH / STEP > 50, 否则程序可能由于无法生成 n 条互不平行的线段而陷入死循环。
3. 数梯形本质上是一个组合问题，所以程序中数梯形时采用了与 combination.py (G328) 类似的二重循环。
"""

import tkinter as tk
from random import randrange
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number, answer_check


WIDTH = 800
HEIGHT = 300
MARGIN_H = 100
MARGIN_V = 100
LEFT = MARGIN_H
RIGHT = WIDTH - MARGIN_H
TOP = MARGIN_V
BOTTOM = HEIGHT - MARGIN_V
LENGTH = RIGHT - LEFT

STEP = 10
DOT_SIZE = 2


def get_line(range_min, range_max):
    """随机生成两个在 [range_min, range_max] 范围内的值，分别代表了线段两端点在两条平行线上的位置。"""
    # 确保新生成的线段和已经生成的所有线段全都不平行。
    parallel = True
    while parallel:
        parallel = False
        value0 = randrange(range_min, range_max, STEP)
        value1 = randrange(range_min, range_max, STEP)
        for line in lines:
            if value0 - line[0] == value1 - line[1]:
                parallel = True
                break
    return value0, value1


def is_intersecting(line1, line2):
    """如果 line1 和 line2 相交，返回 True, 否则返回 False。
    
    line1, line2: 代表两条线段的两个 tuple。
    """
    return (line1[0] - line2[0]) * (line1[1] - line2[1]) <= 0


root = tk.Tk()
root.title('数梯形')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
# Draw two parallel lines.
canvas.create_line(LEFT, TOP, RIGHT, TOP)
canvas.create_line(LEFT, BOTTOM, RIGHT, BOTTOM)

n = int(input_natural_number('生成线段的数量 (2 < n < 10): ',
                             2, 10))
intersect = input('线段能相交吗? (y/n) ')

# 生成并画出 n 条线段，每条线段的两个端点分别位于两条平行线上。
lines = []
range_min = LEFT
range_max = RIGHT
for i in range(n):
    if intersect not in ('y', 'Y', '能', '可以', '是'):
        range_min = LEFT + int(LENGTH * i / n)
        range_max = LEFT + int(LENGTH * (i + 1) / n)
    line = get_line(range_min, range_max)
    lines.append(line)
    canvas.create_oval(line[0] - DOT_SIZE, TOP - DOT_SIZE,
                  line[0] + DOT_SIZE, TOP + DOT_SIZE, fill='black')
    canvas.create_oval(line[1] - DOT_SIZE, BOTTOM - DOT_SIZE,
                  line[1] + DOT_SIZE, BOTTOM + DOT_SIZE, fill='black')
    canvas.create_line(line[0], TOP, line[1], BOTTOM)

# 数梯形。
total = 0
for i in range(n):
    for j in range(i + 1, n):
        if not is_intersecting(lines[i], lines[j]):
            total += 1

if answer_check(total, '图中共有多少个梯形? '):
    print('正确!')
root.mainloop()
