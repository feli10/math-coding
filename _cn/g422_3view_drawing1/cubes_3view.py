"""几何体三视图

关于程序的几点说明：
1. 程序随机生成由立方体积木块拼成的三维几何体，并在窗口正中显示该几何体，按空格键在窗口下方显示该几何体的
   三视图，从左至右依次为：左视图、正视图、俯视图。再按一次空格键重新生成新的几何体。
2. 在程序中，每个立方体的空间位置（列、行、层）存储在一个列表中，几何体中包含的所有立方体也存储在一个列表中。
   所以实际上几何体是由一个二维列表所表示。
3. 使用 Tk Canvas 画图时，在同一位置上新画的图形会覆盖先前的图形。所以只需遵循从左向右、从后向前、从下向上
   的顺序绘制立方体，就可以实现几何体各立方体积木块之间的遮挡效果。
4. 画几何体三视图时，只需在列、行、层三个维度中忽略一个维度即可把立体图 “压扁” 为平面图。例如如果忽略 “层”
   这个维度，就可以画出俯视图。
"""

from tkinter import Tk, Canvas
from random import randint
from time import sleep


# 窗口大小。
WIDTH = 800
HEIGHT = 800

# 绘图时使用的常数。
# 立方体棱长。
EDGE = 100
# 为表现立体感，立方体的前、后两面在横向和纵向上的偏移量。
OFFSET = 35
# 颜色列表中的第一个颜色用于画边框，第二个颜色用于画立方体的正面和右面以及三视图中的正方形，
# 第三个颜色用于画正方体的顶面。
BLUE = ['blue', 'lightblue', 'lightcyan']
# 三视图中正方形的边长。
SIDE = 25

# 生成几何体时使用的常数。
MAX_COLUMN_COUNT = 3
MAX_ROW_COUNT = 3
MAX_LAYER_COUNT = 3
MIN_CUBE_COUNT = 4
# MAX_CUBE_COUNT 不应该超过总块数 (MAX_ROW_COUNT * MAX_COLUMN_COUNT * MAX_LAYER_COUNT)。
MAX_CUBE_COUNT = 12


class Cubes():
    """Cubes类代表由立方体积木块拼成的三维几何体。

    属性
    ----
    cubes: 立方体列表。
    max_x, max_y, max_z: 每个方向上立方体的最大块数。
    drawing: 是否正在绘制几何体。
    show_cubes: 下次调用 controller() 函数时，是绘制几何体还是三视图。

    方法
    ----
    generate_cubes(): 随机生成由立方体拼成的三维几何体。
    """
    def __init__(self):
        """构造函数。"""
        self.cubes = []
        self.max_x = self.max_y = self.max_z = 0
        self.drawing = False
        self.show_cubes = True

    def generate_cubes(self):
        """随机生成由立方体拼成的三维几何体。"""
        cubes = []
        cube_count = randint(MIN_CUBE_COUNT, MAX_CUBE_COUNT)
        num = 0
        while num < cube_count:
            x = randint(0, MAX_COLUMN_COUNT - 1)
            y = randint(0, MAX_ROW_COUNT - 1)
            z = randint(0, MAX_LAYER_COUNT - 1)
            # 立方体的下面必须有另一个立方体，除非该立方体在最底层。
            if [x, y, z] not in cubes and (z == 0 or [x, y, z - 1] in cubes):
                cubes.append([x, y, z])
                num += 1
        # 按照从下到上、从后到前、从左到右的顺序对所有立方体进行排序。
        self.cubes = sorted(cubes, key=lambda x: (x[2], x[1], x[0]))
        # 获取每个方向上立方体的最大块数。
        self.max_x = max(cube[0] for cube in cubes) + 1
        self.max_y = max(cube[1] for cube in cubes) + 1
        self.max_z = max(cube[2] for cube in cubes) + 1


def draw_cube(x, y, color):
    """在指定位置绘制一个立方体。
    
    x, y: 立方体的位置坐标。
    color: 绘制立方体所需的颜色列表。
    """
    canvas.create_rectangle(x, y, x + EDGE, y - EDGE, fill=color[1], outline=color[0])
    canvas.create_polygon(x, y - EDGE, x + OFFSET, y - EDGE - OFFSET,
                            x + EDGE + OFFSET, y - EDGE - OFFSET, x + EDGE, y - EDGE,
                            fill=color[2], outline=color[0])
    canvas.create_polygon(x + EDGE, y - EDGE, x + EDGE + OFFSET, y - EDGE - OFFSET,
                            x + EDGE + OFFSET, y - OFFSET, x + EDGE, y,
                            fill=color[1], outline=color[0])


def draw_square(x, y, color):
    """在指定位置绘制三视图中的一个小正方形。
    
    x, y: 正方形的位置坐标。
    color: 绘制正方形所需的颜色列表。
    """
    canvas.create_rectangle(x, y, x + SIDE, y - SIDE, fill=color[1], outline=color[0])


def draw_cubes():
    """绘制几何体。"""
    # 根据随机生成的几何体，动态分配窗口上、下两部分的高度，上面部分绘制几何体，下面部分绘制三视图。
    LOWER_HEIGHT = SIDE * (max(cubes.max_y, cubes.max_z) + 2)  # 三视图距窗口下边框留白 SIDE * 2。
    UPPER_HEIGHT = HEIGHT - LOWER_HEIGHT
    # 根据随机生成的几何体，动态调整立方体位置原点的坐标，以居中显示几何体。
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
    """绘制几何体的三视图。"""
    FRONT_VIEW_X = WIDTH / 2 - SIDE * cubes.max_x / 2
    LEFT_VIEW_X = WIDTH / 4 - SIDE * cubes.max_y / 2
    TOP_VIEW_X = WIDTH * 3 / 4 - SIDE * cubes.max_x / 2
    # 三个视图下对齐，所以起始纵坐标是相同的。
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
    """控制生成几何体、绘制几何体、绘制三视图。"""
    # 如果正在绘制几何体，不响应按键。
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
root.title('几何体三视图')
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

cubes = Cubes()
controller()
root.bind('<space>', lambda e: controller())
root.mainloop()
