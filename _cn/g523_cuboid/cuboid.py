"""带有单位属性的长方体类

关于程序的几点说明：
1. Property 的定义可以包含两个函数，查询属性值的函数称为 Getter, 改写属性值的函数称为 Setter。长方体类的表面积
   和体积属性只有 Getter 没有 Setter, 所以只能查询不能改写。长方体类的单位属性 unit 存储棱长的单位 (例如 "m"),
   当 unit 改变时，长、宽、高也要做出相应的改变，这只能在 unit 的 Setter 函数中完成。unit 的 Getter 和 Setter
   的函数名同为 unit, 定义函数时，在 Getter 前面加 "@property" 装饰符，在 Setter 前面加 "@unit.setter" 装饰符。
2. 此程序中长方体类的长、宽、高也是 Property, 这主要是为了在它们的 Setter 中把用户输入的 int 或 float 类型数据
   转换为 Decimal 类型，以在小数计算中获得表面积和体积的精确值。
3. 如果给出的棱长参数数量不是 0、1 或 3, 或者参数值不是一个有效的数（例如字符串或负数），因为不是语法错误，程序可以通过
   语法检查，但会在运行阶段出现问题，这类问题被称为 Exception (异常)。Exception 可以被程序捕捉和处理，未经处理的
   Exception 会终止程序并在屏幕上显示错误信息。Python 中有很多内置的 Exception 类型，也可以在程序中自定义新的类型，
   并在需要时用 raise 语句人为抛出 Exception。
4. 程序中自定义了一个 “参数数量有误” 的 Exception。 当棱长参数或各属性设置出现问题时，会抛出相应的内置或自定义的
   Exception 终止程序并显示错误信息。
"""

from decimal import Decimal


UNITS = ['mm', 'cm', 'dm', 'm']


class NumberOfArgumentsError(TypeError):
    """自定义 Exception 类型 NumberOfArgumentsError 作为内置类型 TypeError 的子类型。"""
    def __init__(self, num):
        super().__init__(f'棱长参数只能有 0、1 或 3 个。你输入了 {num} 个。')


def check_positive_number(value):
    """检查 value 是否是一个 int, float 或 Decimal 类型的正数。"""
    if not isinstance(value, (int, float, Decimal)):
        raise TypeError('棱长必须是一个数。')
    if value <= 0:
        raise ValueError('棱长必须大于 0。')


class Cuboid:
    """长方体类

    Property 属性
    -------------
    length/width/height: 长方体的长、宽、高。
    surface_area: 长方体的表面积。
    volume: 长方体的体积。
    unit: 长、宽、高的长度单位。

    方法
    ----
    is_cube(): 检查长方体是否是正方体。
    """
    def __init__(self, *edges, unit='cm'):
        """构造函数
        
        edges: 棱长参数的数量只能是 0、1 或 3 个。
            Cuboid(): 创建一个棱长为 1 的正方体对象。
            Cuboid(a): 创建一个棱长为 a 的正方体对象。
            Cuboid(a, b, h): 创建一个长、宽、高分别为 a、b、h 的长方体对象。
        unit: 长度单位字符串, 'mm', 'cm', 'dm', 或 'm'
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
            # 如果棱长参数的数量不是 0、1 或 3 个，抛出一个自定义的 Exception。
            raise NumberOfArgumentsError(len(edges))

        # 如果长度单位不在指定范围内，抛出一个 Exception。
        if unit not in UNITS:
            raise ValueError(f'长度单位必须是 {UNITS} 中的一个。')
        # _unit 是单位属性使用的内部变量。
        self._unit = unit

        # 显示对象创建成功的信息。
        if self.is_cube():
            print('成功创建了一个正方体对象。\n'
                  + f'棱长: {self.length}{self.unit}\n')
        else:
            print('成功创建了一个长方体对象。\n'
                  + f'长: {self.length}{self.unit}\n'
                  + f'宽: {self.width}{self.unit}\n'
                  + f'高: {self.height}{self.unit}\n')

    def is_cube(self):
        """检查长方体是否是正方体。"""
        if self.length == self.width == self.height:
            return True
        return False

    @property
    def length(self):
        """长属性的 Getter。"""
        return self._length

    @length.setter
    def length(self, value):
        """长属性的 Setter。"""
        check_positive_number(value)
        self._length = Decimal(str(value))

    @property
    def width(self):
        """宽属性的 Getter。"""
        return self._width

    @width.setter
    def width(self, value):
        """宽属性的 Setter。"""
        check_positive_number(value)
        self._width = Decimal(str(value))

    @property
    def height(self):
        """高属性的 Getter。"""
        return self._height

    @height.setter
    def height(self, value):
        """高属性的 Setter。"""
        check_positive_number(value)
        self._height = Decimal(str(value))

    @property
    def surface_area(self):
        """表面积属性的 Getter。"""
        return (self.length * self.width + self.length * self.height + self.width * self.height) * 2

    @property
    def volume(self):
        """体积属性的 Getter。"""
        return self.length * self.width * self.height

    @property
    def unit(self):
        """单位属性的 Getter。"""
        return self._unit

    @unit.setter
    def unit(self, value):
        """单位属性的 Setter。"""
        # 如果长度单位不在指定范围内，抛出一个 Exception。
        if value not in UNITS:
            raise ValueError(f'长度单位必须是 {UNITS} 中的一个。')

        # 根据新的单位，改变长、宽、高的值。
        old = UNITS.index(self.unit)
        new = UNITS.index(value)
        change = Decimal(str(10 ** (old - new)))
        self.length *= change
        self.width *= change
        self.height *= change

        self._unit = value

    def __repr__(self):
        """使用 print() 函数输出长方形对象时的显示内容。"""
        if self.is_cube():
            message = ('正方体\n'
                       + f'棱长: {self.length}{self.unit}\n')
        else:
            message = ('长方体\n'
                       + f'长: {self.length}{self.unit}\n'
                       + f'宽: {self.width}{self.unit}\n'
                       + f'高: {self.height}{self.unit}\n')

        return (message
                + f'表面积: {self.surface_area}{self.unit}²\n'
                + f'体积: {self.volume}{self.unit}³\n')


# cuboid = Cuboid(3, 2, unit = 'dm')  # 会显示 NumberOfArgumentsError。
cuboid = Cuboid(3, unit='dm')
cuboid.height = 5
print(cuboid)
cuboid.unit = 'm'
print(cuboid)
