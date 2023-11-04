"""Counting Trapezoids

Some Useful Information:
1. All generated lines are non-parallel to ensure that no parallelograms appear when counting
   trapezoids.
2. When adjusting WIDTH and STEP, make sure that LENGTH / STEP > 50, otherwise the program
   may fall into an infinite loop due to the inability to generate n non-parallel lines.
3. Counting trapezoids is essentially a combination problem, so the program uses two nested loops
   similar to combination.py (G328).
"""

import tkinter as tk
from random import randrange
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
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
    """Randomly generate two values within [range_min, range_max] representing positions of
    a line's two endpoints.
    
    range_min/range_max: integers that determines the range of generated values.
    """
    # Make sure the generated line is not parallel to any previously generated lines.
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
    """Return True if line1 and line2 intersect, and False otherwise.
    
    line1, line2: two tuples representing two lines.
    """
    return (line1[0] - line2[0]) * (line1[1] - line2[1]) <= 0


root = tk.Tk()
root.title('Counting Trapezoids')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
# Draw two parallel lines.
canvas.create_line(LEFT, TOP, RIGHT, TOP)
canvas.create_line(LEFT, BOTTOM, RIGHT, BOTTOM)

n = int(input_natural_number('Number of generated line segments (2 < n < 10): ', 2, 10))
intersect = input('Are intersections allowed? (y/n) ')

# Generate and draw n line segments.
# Each endpoint of a line segment lies on one of the two parallel lines.
lines = []
range_min = LEFT
range_max = RIGHT
for i in range(n):
    if intersect not in ('y', 'Y', 'yes', 'Yes'):
        range_min = LEFT + int(LENGTH * i / n)
        range_max = LEFT + int(LENGTH * (i + 1) / n)
    line = get_line(range_min, range_max)
    lines.append(line)
    canvas.create_oval(line[0] - DOT_SIZE, TOP - DOT_SIZE,
                  line[0] + DOT_SIZE, TOP + DOT_SIZE, fill='black')
    canvas.create_oval(line[1] - DOT_SIZE, BOTTOM - DOT_SIZE,
                  line[1] + DOT_SIZE, BOTTOM + DOT_SIZE, fill='black')
    canvas.create_line(line[0], TOP, line[1], BOTTOM)

# Count trapezoids.
total = 0
for i in range(n):
    for j in range(i + 1, n):
        if not is_intersecting(lines[i], lines[j]):
            total += 1

if answer_check(total, 'How many trapezoids? '):
    print('Correct!')
root.mainloop()
