"""Add methods for calculating area and drawing rectangle to Rectangle class.

Some Useful Information:
1. You can choose to draw a grid within a rectangle. Each small square in the grid is
   an area unit and the number of small squares is the area of the rectangle.
2. The program uses two tools, Turtle and Tk, to draw a rectangle. It should be noted
   that the origin of Turtle is in the center of screen and the origin of Tk is in the
   upper left corner.
3. The words "width" and "height" are genarlly used to represent the horizontal and vertical
   dimensions of the screen. For consistency, the Rectangle class's attributes "length" and
   "width" are changed to "width" and "height".
"""

import turtle
import tkinter as tk


UNIT = 50
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 900
CENTER_X = CANVAS_WIDTH / 2
CENTER_Y = CANVAS_HEIGHT / 2


class Rectangle():
    """Rectangle

    Attributes
    ----------
    width: horizontal length of rectangle.
    height: vertical length of rectangle.

    Methods
    -------
    get_perimeter(): return the perimeter of the rectangle.
    get_area(): return the area of the rectangle.
    is_square(): return True if the rectangle is a square and False if not.
    """
    def __init__(self, width=1, height=None):
        """Constructor
        
        width: horizontal length of rectangle.
        height: vertical length of rectangle.

        Rectangle(m, n): instantiate a rectangle object with width m and height n.
        Rectangle(m): instantiate a rectangle object representing a square with side length m.
        Rectangle(): instantiate a rectangle object representing a square with side length 1.
        """
        if not height:
            height = width
        self.width = width
        self.height = height

    def get_perimeter(self):
        """Return the perimeter of the rectangle."""
        return (self.width + self.height) * 2

    def get_area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def is_square(self):
        """Return True if the rectangle is a square and False if not."""
        return self.width == self.height

    def __repr__(self):
        """Return a string representation of this rectangle."""
        string = ''
        if self.is_square():
            string += ('Square\n'
                       + f'side: {self.width}\n')
        else:
            string += ('Rectangle\n'
                       + f'width: {self.width}\n'
                       + f'height: {self.height}\n')
        string += (f'perimeter: {self.get_perimeter()}\n'
                   + f'area: {self.get_area()}\n')

        return string

    def draw(self, fill=None, grid=False):
        """Draw a rectangle with Turtle according to the width and height of the rectangle object.
        
        fill: a string of standard 'color_name' or '#rrggbb' in hexadecimal digits or
              a color tuple (r,g,b) (r, g, and b must be within the range 0-255). 
        grid: whether to draw a grid within the rectangle. Each small square in the grid is
              an area unit and the number of small squares is the area of the rectangle.
        """
        turtle.setup(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)  # Setep screen size.
        turtle.colormode(255)  # r, g, b values of color tuple must be within the range 0-255.
        turtle.speed(0)  # Speed up the turtle.

        width = self.width * UNIT
        height = self.height * UNIT

        # Draw a rectangle.
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
        # Draw a grid.
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
        """Draw a rectangle with Tk according to the width and height of the rectangle object.
        
        fill: a string of standard 'color_name' or '#rrggbb' in hexadecimal digits.
        grid: whether to draw a grid within the rectangle. Each small square in the grid is
              an area unit and the number of small squares is the area of the rectangle.
        """
        root = tk.Tk()
        canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        canvas.pack()

        width = self.width * UNIT
        height = self.height * UNIT

        # Draw a rectangle.
        top_left_x = CENTER_X - width / 2
        top_left_y = CENTER_Y - height / 2
        bottom_right_x = CENTER_X + width / 2
        bottom_right_y = CENTER_Y + height / 2
        canvas.create_rectangle(top_left_x, top_left_y,
                                bottom_right_x, bottom_right_y, fill=fill)
        # Draw a grid.
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


rect = Rectangle(10)  # rect is a square.
print(rect)

rect.width = 15  # Since width and height are no longer equal, rect becomes a rectangle.
print(rect)

rect.draw(fill='lightblue', grid=True)
