"""Visual representation of decimals"""

import tkinter as tk
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
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
    # Value in tenths place, which represents the number of columns.
    tenths = cell_count // ROW
    # Value in hundredths place, which represents the number of cells in a column. If the deciaml
    # has more decimal places after hundredths, it actually includes those values as well.
    hundredths = cell_count % ROW

    # Draw a colored rectangle based on tenths.
    top_left_x = CENTER_X - WIDTH / 2
    top_left_y = CENTER_Y - HEIGHT / 2
    bottom_right_x = top_left_x + tenths * UNIT
    bottom_right_y = CENTER_Y + HEIGHT / 2
    canvas.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y,
                            fill=FILL_COLOR, width=0)

    # Draw a colored rectangle based on hundredths.
    top_left_x = bottom_right_x
    bottom_right_x = top_left_x + UNIT
    bottom_right_y = top_left_y + int(hundredths * UNIT)
    canvas.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y,
                            fill=FILL_COLOR, width=0)


decimal = input_decimal('Enter a decimal or fraction between 0 and 1: ', 0, 1, fraction=True)
cell_count = float(decimal) * ROW * COLUMN

root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# draw_grid() is called after fill_cells() to ensure that the grid is
# displayed over the colored cells.
fill_cells(cell_count)
draw_grid()

root.mainloop()
