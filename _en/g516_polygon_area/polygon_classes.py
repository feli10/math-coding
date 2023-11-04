"""Polygon classes with area property

Some Useful Information:
1. Each class has a property "area". The value of area is determined by other attributes such as
   base and height. If other attributes change, area will also change accordingly. And area is
   not allowed to be directly set to a value.
2. When a property is defined inside a class, the "@property" decorator is added before a function
   of the same name. Properties are accessed the same way as other attributes, but accessing a
   property is actually invoking a function internally. So, more can be done when accessing
   properties compared to attributes.
"""


class Parallelogram:
    """Parallelogram Class
    
    Attributes
    ----------
    base: base of parallelogram.
    height: height of parallelogram.

    Properties
    ----------
    area: area of parallelogram.
    """
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    @property
    def area(self):
        return self.base * self.height

    def __repr__(self):
        return ('Parallelogram\n'
                + f'base: {self.base}\n'
                + f'height: {self.height}\n'
                + f'area: {self.area}\n')


class Triangle:
    """Triangle Class
    
    Attributes
    ----------
    base: base of triangle.
    height: height of triangle.

    Properties
    ----------
    area: area of triangle.
    """
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    @property
    def area(self):
        result = self.base * self.height / 2
        return int(result) if int(result) == result else result

    def __repr__(self):
        return ('Triangle\n'
                + f'base: {self.base}\n'
                + f'height: {self.height}\n'
                + f'area: {self.area}\n')


class Trapezoid:
    """Trapezoid Class
    
    Attributes
    ----------
    base1/base2: two bases of trapezoid.
    height: height of trapezoid.

    Properties
    ----------
    area: area of trapezoid.
    """
    def __init__(self, base1=1, base2=2, height=1):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    @property
    def area(self):
        result = (self.base1 + self.base2) * self.height / 2
        return int(result) if int(result) == result else result

    def __repr__(self):
        shape = 'Trapezoid'
        if self.base1 == self.base2:
            shape = 'Parallelogram'
        return (f'{shape}\n'
                + f'base1: {self.base1}\n'
                + f'base2: {self.base2}\n'
                + f'height: {self.height}\n'
                + f'area: {self.area}\n')


parallelogram = Parallelogram(4, 3)
print(parallelogram.area)
# parallelogram.area = 10  # AttributeError: can't set attribute 'area'
parallelogram.base = 5
print(parallelogram)

# triangle = Triangle(4, 3)
# print(triangle)

# trapezoid = Trapezoid(3, 5, 4)
# print(trapezoid)
