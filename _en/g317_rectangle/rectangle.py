"""Create Rectangle class to represent a rectangle.

Some Useful Information:
1. get_perimeter() method is used to calculate the perimeter of the rectangle.
2. is_square() method is used to tell if the rectangle is a square.
"""

class Rectangle():
    """Rectangle

    Attributes
    ----------
    length: length of the rectangle.
    width: width of the rectangle.

    Methods
    -------
    get_perimeter(): return the perimeter of the rectangle.
    is_square(): return True if the rectangle is a square and False if not.
    """
    def __init__(self, length=1, width=None):
        """Constructor
        
        length: length of the rectangle.
        width: width of the rectangle.

        Rectangle(m, n): instantiate a rectangle object length m and width n.
        Rectangle(m): instantiate a rectangle object representing a square with side length m.
        Rectangle(): instantiate a rectangle object representing a square with side length 1.
        """
        if not width:
            width = length
        self.length = length
        self.width = width

    def get_perimeter(self):
        """Return the perimeter of the rectangle."""
        return (self.length + self.width) * 2

    def is_square(self):
        """Return True if the rectangle is a square and False if not."""
        return self.length == self.width

    def __repr__(self):
        """Return a string representation of this rectangle."""
        string = ''
        if self.is_square():
            string += ('Square\n'
                       + f'side: {self.length}\n')
        else:
            string += ('Rectangle\n'
                       + f'length: {self.length}\n'
                       + f'width: {self.width}\n')
        string += f'perimeter: {self.get_perimeter()}\n'

        return string


rect1 = Rectangle(5, 2)  # rect1 is a rectangle.
print(rect1)

rect2 = Rectangle(3)  # rect2 is a square.
print(rect2)

rect2.length = 4  # Since length and width are no longer equal, rect2 becomes a rectangle.
print(rect2)
