"""Cuboid class with unit property.

Some Useful Information:
1. In Cuboid class, surface_area and volume are two properties with only a getter, and unit is
   a property with both a getter and setter. Getter and setter are functions with the same name
   as their property. There is a "@property" decorator before the getter and "@unit.setter"
   decorator before the setter of unit. If unit changes, all attributes will also be changed
   accordingly in the setter of unit.
2. length/width/height are also properties with both a getter and setter. This is mainly because
   int or float values need to be converted to Decimal in their setters to obtain accurate values
   of surface area and volume in decimal calculations.
3. When instantiating a Cuboid object, 0, 1, or 3 edge arguments can be given. If other numbers
   of edge arguments are given, or if any edge value is not valid, the program can still pass the
   syntax test, but errors will occur at runtime - such errors are called exceptions. Exceptions
   can be handled in programs. Exceptions that are not handled will result in error messages.
   In addition to built-in exceptions, there are also user-defined exceptions which can be raised
   manually with the "raise" keyword.
4. The program defines a custom exception for the wrong number of edge arguments. If there are any
   problems on instantiating a Cuboid object or setting a property, a corresponding built-in or
   user_defined exception will be raised and the error message will be displayed.
"""

from decimal import Decimal


UNITS = ['mm', 'cm', 'dm', 'm']


class NumberOfArgumentsError(TypeError):
    """Define a custom exception class NumberOfArgumentsError derived from the built-in
    exception class TypeError."""
    def __init__(self, num):
        super().__init__('The number of edge arguments can only be 0, 1, or 3. '
                         + f'You have {num} edge arguments.')


def check_positive_number(value):
    """Check if value is a positive number."""
    if not isinstance(value, (int, float, Decimal)):
        raise TypeError('The edges must be integers or floats.')
    if value <= 0:
        raise ValueError('The edges must be larger than zero.')


class Cuboid:
    """Cuboid Class

    Properties
    ----------
    length/width/height: length/width/height of the cuboid
    surface_area: surface area of the cuboid
    volume: volume of the cuboid
    unit: unit of length/width/height of the cuboid

    Methods
    --------
    is_cube(): check if the cuboid is a cube.
    """
    def __init__(self, *edges, unit='cm'):
        """Constructor
        
        edges: the number of edge arguments can only be 0, 1, or 3.
            Cuboid(): instantiate a new cube with edge length 1.
            Cuboid(a): instantiate a new cube with edge length a.
            Cuboid(a, b, h): instantiate a new cuboid with length a, width b, and height h.
        unit: length unit string, 'mm', 'cm', 'dm', or 'm'
        """
        if len(edges) == 0:
            self.length = self.width = self.height = 1
        elif len(edges) == 1:
            self.length = self.width = self.height = edges[0]
        elif len(edges) == 3:
            self.length = edges[0]
            self.width = edges[1]
            self.height = edges[2]
        else:
            # Raise an user-defined exception if the number of edge arguments is not 0, 1, or 3.
            raise NumberOfArgumentsError(len(edges))

        # Raise an exception if the unit value is not valid.
        if unit not in UNITS:
            raise ValueError(f'Unit must be one of {UNITS}.')
        # _unit is an internal instance variable used for the unit property.
        self._unit = unit

        # Display feedback of successfully creating an object.
        if self.is_cube():
            print('Successfully created a cube.\n'
                  + f'Edge: {self.length}{self.unit}\n')
        else:
            print('Successfully created a cuboid.\n'
                  + f'Length: {self.length}{self.unit}\n'
                  + f'Width: {self.width}{self.unit}\n'
                  + f'Height: {self.height}{self.unit}\n')

    def is_cube(self):
        """Check if the cuboid is a cube."""
        if self.length == self.width == self.height:
            return True
        return False

    @property
    def length(self):
        """Getter of the length property."""
        return self._length

    @length.setter
    def length(self, value):
        """Setter of the length property."""
        check_positive_number(value)
        self._length = Decimal(str(value))

    @property
    def width(self):
        """Getter of the width property."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter of the width property."""
        check_positive_number(value)
        self._width = Decimal(str(value))

    @property
    def height(self):
        """Getter of the height property."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter of the height property."""
        check_positive_number(value)
        self._height = Decimal(str(value))

    @property
    def surface_area(self):
        """Getter of the surface_ara property."""
        return (self.length * self.width + self.length * self.height + self.width * self.height) * 2

    @property
    def volume(self):
        """Getter of the volume property."""
        return self.length * self.width * self.height

    @property
    def unit(self):
        """Getter of the unit property."""
        return self._unit

    @unit.setter
    def unit(self, value):
        """Setter of the unit property."""
        # Raise an exception if the unit value is not valid.
        if value not in UNITS:
            raise ValueError(f'Unit must be one of {UNITS}')

        # Change the length/width/height values according to the new unit value.
        old = UNITS.index(self.unit)
        new = UNITS.index(value)
        change = Decimal(str(10 ** (old - new)))
        self.length *= change
        self.width *= change
        self.height *= change

        self._unit = value

    def __repr__(self):
        """Return a string representation of the cuboid."""
        if self.is_cube():
            message = ('Cube\n'
                       + f'Edge: {self.length}{self.unit}\n')
        else:
            message = ('Cuboid\n'
                       + f'Length: {self.length}{self.unit}\n'
                       + f'Width: {self.width}{self.unit}\n'
                       + f'Height: {self.height}{self.unit}\n')

        return (message
                + f'Surface Area: {self.surface_area}{self.unit}²\n'
                + f'Volume: {self.volume}{self.unit}³\n')


# cuboid = Cuboid(3, 2, unit = 'dm')  # NumberOfArgumentsError will be raised.
cuboid = Cuboid(3, unit='dm')
cuboid.height = 5
print(cuboid)
cuboid.unit = 'm'
print(cuboid)
