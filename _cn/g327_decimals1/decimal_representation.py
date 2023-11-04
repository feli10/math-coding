"""小数的形象化表示"""

import tkinter as tk
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 900
CENTER_X = CANVAS_WIDTH / 2
CENTER_Y = CANVAS_HEIGHT / 2

UNIT = 50
ROW = 10
COLUMN = 10
WIDTH = COLUMN * UNIT
HEIGHT = ROW * UNIT
FILL_COLOR = 'light blue'
GRID_COLOR = 'gray'


def draw_grid():
    """Draw a grid."""
    for i in range(ROW + 1):
        left_end_x = CENTER_X - WIDTH / 2
        left_end_y = CENTER_Y - HEIGHT / 2 + i * UNIT
        right_end_x = CENTER_X + WIDTH / 2
        right_end_y = left_end_y
        canvas.create_line(left_end_x, left_end_y, right_end_x, right_end_y, fill=GRID_COLOR)
    for i in range(COLUMN + 1):
        up_end_x = CENTER_X - WIDTH / 2 + i * UNIT
        up_end_y = CENTER_Y - HEIGHT / 2
        down_end_x = up_end_x
        down_end_y = CENTER_Y + HEIGHT / 2
        canvas.create_line(up_end_x, up_end_y, down_end_x, down_end_y, fill=GRID_COLOR)


def fill_cells(cell_count):
    """Fill cell_count cells in a grid."""
    # 十分位上的值，表示要涂色的列数。
    tenths = cell_count // ROW
    # 百分位上的值，表示一列中要涂色的格数。如果小数位数不止两位，实际上也包含着百分位后面数位的值。
    hundredths = cell_count % ROW

    # 根据十分位画一个涂色的长方形。
    top_left_x = CENTER_X - WIDTH / 2
    top_left_y = CENTER_Y - HEIGHT / 2
    bottom_right_x = top_left_x + tenths * UNIT
    bottom_right_y = CENTER_Y + HEIGHT / 2
    canvas.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y,
                            fill=FILL_COLOR, width=0)

    # 根据百分位（及后面数位）画一个涂色的长方形。
    top_left_x = bottom_right_x
    bottom_right_x = top_left_x + UNIT
    bottom_right_y = top_left_y + int(hundredths * UNIT)
    canvas.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y,
                            fill=FILL_COLOR, width=0)


decimal = input_decimal('输入一个 0 到 1 之间的小数或分数: ', 0, 1, fraction=True)
cell_count = float(decimal) * ROW * COLUMN

root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# 先调用 fill_cells() 涂色，再调用 draw_grid() 画网格，以确保网格线显示在颜色上面。
fill_cells(cell_count)
draw_grid()

root.mainloop()
