"""在长方形类中加入求面积和画长方形的方法

关于程序的几点说明：
1. 画长方形时可以选择在长方形中画出网格，每个正方形小格代表一个单位面积，网格的数量代表了
   长方形面积的大小。
2. 程序使用了 Turtle 和 Tk 两种方法画长方形。需要注意的是: Turlte 的坐标原点在屏幕中心，
   Tk 的坐标原点在屏幕的左上角（向下为正方向）。
3. 一般用“宽”和“高”表示屏幕的横向和纵向尺寸，为了使长方形类的属性名与之保持一致，将之前的
   length 和 width 属性，改为 width 和 height。
"""

import turtle
import tkinter as tk


UNIT = 50
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 900
CENTER_X = CANVAS_WIDTH / 2
CENTER_Y = CANVAS_HEIGHT / 2


class Rectangle():
    """长方形类

    属性
    ----
    width: 长方形的横向长度。
    height: 长方形的纵向长度。

    方法
    ----
    get_perimeter(): 返回长方形的周长。
    get_area(): 返回长方形的面积。
    is_square(): 正方形返回 True, 否则返回 False。
    """
    def __init__(self, width=1, height=None):
        """构造函数
        
        width: 长方形的横向长度。
        height: 长方形的纵向长度。

        Rectangle(m, n): 实例化一个宽是 m 高是 n 的长方形对象。
        Rectangle(m): 实例化一个长方形对象，代表边长是 m 的正方形。
        Rectangle(): 实例化一个长方形对象，代表边长是 1 的正方形。
        """
        if not height:
            height = width
        self.width = width
        self.height = height

    def get_perimeter(self):
        """返回长方形的周长。"""
        return (self.width + self.height) * 2

    def get_area(self):
        """返回长方形的面积。"""
        return self.width * self.height

    def is_square(self):
        """正方形返回 True, 否则返回 False。"""
        return self.width == self.height

    def __repr__(self):
        """使用 print() 函数输出长方形对象时的显示内容。"""
        string = ''
        if self.is_square():
            string += ('正方形\n'
                     + f'边长: {self.width}\n')
        else:
            string += ('长方形\n'
                     + f'宽: {self.width}\n'
                     + f'高: {self.height}\n')
        string += (f'周长: {self.get_perimeter()}\n'
                 + f'面积: {self.get_area()}\n')

        return string

    def draw(self, fill=None, grid=False):
        """按照长方形对象的宽和高，用 Turtle 画长方形。
        
        fill: 通用颜色名字符串 'color_name' 或 16进制 RGB 字符串 '#rrggbb'
              或颜色三元组 (r,g,b)，三元组中的 r,g,b 取值为 0-255。
        grid: 是否在长方形内画网格。每个正方形小格代表一个单位面积，网格的数量代表了长方形面积的大小。
        """
        turtle.setup(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)  # 设置窗口尺寸。
        turtle.colormode(255)  # 设置颜色三元组中的 r,g,b 取值为 0-255。
        turtle.speed(0)  # 加速 turtle 画图动画。

        width = self.width * UNIT
        height = self.height * UNIT

        # 画长方形。
        turtle.penup()
        turtle.goto(-width/2, -height/2)
        turtle.pendown()
        if fill:
            turtle.fillcolor(fill)
            turtle.begin_fill()
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        if fill:
            turtle.end_fill()
        # 画网格。
        if grid:
            for i in range(self.height + 1):
                turtle.penup()
                turtle.goto(-width/2, height/2 - i * UNIT)
                turtle.pendown()
                turtle.forward(width)
            turtle.right(90)
            for i in range(self.width + 1):
                turtle.penup()
                turtle.goto(-width/2 + i * UNIT, height/2)
                turtle.pendown()
                turtle.forward(height)

        turtle.mainloop()

    def draw_tk(self, fill=None, grid=False):
        """按照长方形对象的宽和高，用 Tk 画长方形。
        
        fill: 通用颜色名字符串 'color_name' 或 16进制 RGB 字符串 '#rrggbb'。
        grid: 是否在长方形内画网格。每个正方形小格代表一个单位面积，网格的数量代表了长方形面积的大小。
        """
        root = tk.Tk()
        canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        canvas.pack()

        width = self.width * UNIT
        height = self.height * UNIT

        # 画长方形。
        top_left_x = CENTER_X - width / 2
        top_left_y = CENTER_Y - height / 2
        bottom_right_x = CENTER_X + width / 2
        bottom_right_y = CENTER_Y + height / 2
        canvas.create_rectangle(top_left_x, top_left_y,
                                bottom_right_x, bottom_right_y, fill=fill)
        # 画网格。
        if grid:
            for i in range(self.height + 1):
                left_end_x = CENTER_X - width / 2
                left_end_y = CENTER_Y - height / 2 + i * UNIT
                right_end_x = CENTER_X + width / 2
                right_end_y = CENTER_Y - height / 2 + i * UNIT
                canvas.create_line(left_end_x, left_end_y, right_end_x, right_end_y)
            for i in range(self.width + 1):
                up_end_x = CENTER_X - width / 2 + i * UNIT
                up_end_y = CENTER_Y - height / 2
                down_end_x = CENTER_X - width / 2 + i * UNIT
                down_end_y = CENTER_Y + height / 2
                canvas.create_line(up_end_x, up_end_y, down_end_x, down_end_y)

        root.mainloop()


rect = Rectangle(10)  # rect 是一个正方形。
print(rect)

rect.width = 15  # 宽改变后和高不再相等，现在 rect 是一个长方形。
print(rect)

rect.draw(fill='lightblue', grid=True)
