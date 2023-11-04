"""Three Views of Cubes

Some Useful Information:
1. The program randomly generates and draws an object made of cubes. Press spacebar to display
   the three views of the object at the bottom of the window. From left to right, they are the
   left view, front view, and top view. Press spacebar again to generate a new object.
2. The spatial position (column, row, layer) of each cube is stored in a list, and all cubes
   are contained in the object. So, the object is represented by a two-dimensional list.
3. What is drawn on the canvas will cover the previous drawings at the same position. So the
   cubes only need to be drawn in the order from left to right, back to front, and bottom to
   top to achieve an occlusion effect.
4. The object is flattened to a view by ignoring one of the three dimensions of the object.
   E.g., a top view can be drawn by ignoring the layer dimension (z coordinate).
"""

from tkinter import Tk, Canvas
from random import randint
from time import sleep


# Window size.
WIDTH = 800
HEIGHT = 800

# Constants for drawing.
# Edge length of a cube.
EDGE = 100
# The offset of the back edge upward and to the right relative to the front edge.
OFFSET = 35
# The color group used to draw a cube. The first color in the list is for the border,
# the second is for the front and right faces, and the third is for the top face.
BLUE = ['blue', 'lightblue', 'lightcyan']
# Side length of a square in three views.
SIDE = 25

# Constants for generating cubes.
MAX_COLUMN_COUNT = 3
MAX_ROW_COUNT = 3
MAX_LAYER_COUNT = 3
MIN_CUBE_COUNT = 4
# MAX_CUBE_COUNT should not exceed (MAX_ROW_COUNT * MAX_COLUMN_COUNT * MAX_LAYER_COUNT).
MAX_CUBE_COUNT = 12


class Cubes():
    """Cubes class representing a three-dimensional object made of cubes.

    Attributes
    ----------
    cubes: a list of cubes.
    max_x, max_y, max_z: max number of cubes in each direction.
    drawing: whether cubes are being drawn.
    show_cubes: whether to draw cubes or views next time controller() is called.

    Methods
    -------
    generate_cubes(): generate cubes randomly.
    """
    def __init__(self):
        """Constructor."""
        self.cubes = []
        self.max_x = self.max_y = self.max_z = 0
        self.drawing = False
        self.show_cubes = True

    def generate_cubes(self):
        """Generate cubes."""
        cubes = []
        cube_count = randint(MIN_CUBE_COUNT, MAX_CUBE_COUNT)
        num = 0
        while num < cube_count:
            x = randint(0, MAX_COLUMN_COUNT - 1)
            y = randint(0, MAX_ROW_COUNT - 1)
            z = randint(0, MAX_LAYER_COUNT - 1)
            # The generated cube must be on top of another cube, unless it is at the bottom.
            if [x, y, z] not in cubes and (z == 0 or [x, y, z - 1] in cubes):
                cubes.append([x, y, z])
                num += 1
        # Sort all cubes from bottom to top, back to front, and left to right.
        self.cubes = sorted(cubes, key=lambda x: (x[2], x[1], x[0]))
        # Get max number of cubes in each direction.
        self.max_x = max(cube[0] for cube in cubes) + 1
        self.max_y = max(cube[1] for cube in cubes) + 1
        self.max_z = max(cube[2] for cube in cubes) + 1


def draw_cube(x, y, color):
    """Draw a cube at the given position.
    
    x, y: cube's position coordinates.
    color: a color group list used to draw a cube.
    """
    canvas.create_rectangle(x, y, x + EDGE, y - EDGE, fill=color[1], outline=color[0])
    canvas.create_polygon(x, y - EDGE, x + OFFSET, y - EDGE - OFFSET,
                            x + EDGE + OFFSET, y - EDGE - OFFSET, x + EDGE, y - EDGE,
                            fill=color[2], outline=color[0])
    canvas.create_polygon(x + EDGE, y - EDGE, x + EDGE + OFFSET, y - EDGE - OFFSET,
                            x + EDGE + OFFSET, y - OFFSET, x + EDGE, y,
                            fill=color[1], outline=color[0])


def draw_square(x, y, color):
    """Draw a single square at the given position in three views.
    
    x, y: square's position coordinates.
    color: a color group list used to draw a square.
    """
    canvas.create_rectangle(x, y, x + SIDE, y - SIDE, fill=color[1], outline=color[0])


def draw_cubes():
    """Draw cubes."""
    # Based on generated cubes, dynamically assign heights to upper and lower parts of the window
    # for displaying cubes and views respectively.
    LOWER_HEIGHT = SIDE * (max(cubes.max_y, cubes.max_z) + 2)  # Use SIDE * 2 as padding.
    UPPER_HEIGHT = HEIGHT - LOWER_HEIGHT
    # Based on generated cubes, dynamically adjust the origin's position to center the displayed
    # cubes.
    CUBES_WIDTH = EDGE * cubes.max_x + OFFSET * cubes.max_y
    CUBES_HEIGHT = EDGE * cubes.max_z + OFFSET * cubes.max_y
    ORIGIN_X = (WIDTH - CUBES_WIDTH) / 2 + OFFSET * (cubes.max_y - 1)
    ORIGIN_Y = UPPER_HEIGHT - (UPPER_HEIGHT - CUBES_HEIGHT) / 2 - OFFSET * (cubes.max_y - 1)

    cubes.drawing = True
    for cube in cubes.cubes:
        x = ORIGIN_X + EDGE * cube[0] - OFFSET * cube[1]
        y = ORIGIN_Y - EDGE * cube[2] + OFFSET * cube[1]
        draw_cube(x, y, BLUE)
        root.update()
        sleep(0.2)
    cubes.drawing = False


def draw_views():
    """Draw front view, left view, and top view of the cubes."""
    FRONT_VIEW_X = WIDTH / 2 - SIDE * cubes.max_x / 2
    LEFT_VIEW_X = WIDTH / 4 - SIDE * cubes.max_y / 2
    TOP_VIEW_X = WIDTH * 3 / 4 - SIDE * cubes.max_x / 2
    # The bottoms of the three views are aligned, which means the starting y coordinates are
    # the same.
    VIEW_Y = HEIGHT - SIDE * 2

    for cube in cubes.cubes:
        x = FRONT_VIEW_X + SIDE * cube[0]
        y = VIEW_Y - SIDE * cube[2]
        draw_square(x, y, BLUE)
        x = LEFT_VIEW_X + SIDE * cube[1]
        y = VIEW_Y - SIDE * cube[2]
        draw_square(x, y, BLUE)
        x = TOP_VIEW_X + SIDE * cube[0]
        y = VIEW_Y - SIDE * (cubes.max_y - 1 - cube[1])
        draw_square(x, y, BLUE)


def controller():
    """Control generating cubes, drawing cubes, and drawing views."""
    # Do not respond to keyboard events if cubes are being drawn.
    if cubes.drawing:
        return
    if cubes.show_cubes:
        cubes.generate_cubes()
        canvas.delete('all')
        draw_cubes()
    else:
        draw_views()
    cubes.show_cubes = not cubes.show_cubes


root = Tk()
root.title('Three Views of Cubes')
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

cubes = Cubes()
controller()
root.bind('<space>', lambda e: controller())
root.mainloop()
