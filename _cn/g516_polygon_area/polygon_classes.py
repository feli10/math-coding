"""多边形类的面积属性

关于程序的几点说明：
1. 程序分别定义了平行四边形、三角形和梯形类，在每个类中都有一个面积属性 (area)。与一般的属性不同，
   area 的取值是由底和高等其它属性值决定的，其它属性值改变, area 的值也要随之改变，而且 area 也不允许
   被直接改写。像 area 这种特殊的属性，在 Python 中被称为 Property。
2. 在类中定义 Property 时，是在同名函数前加 “@property” 装饰符。访问 Property 同访问其它属性一样，
   但对 Property 的访问在内部实际上是对函数的调用，所以可以对读、写进行更多控制。
"""


class Parallelogram:
    """平行四边形类
    
    属性
    ----
    base: 平行四边形的底。
    height: 平行四边形的高。

    Property 属性
    -------------
    area: 平行四边形的面积。
    """
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    @property
    def area(self):
        return self.base * self.height

    def __repr__(self):
        return ('平行四边形\n'
                + f'底: {self.base}\n'
                + f'高: {self.height}\n'
                + f'面积: {self.area}\n')


class Triangle:
    """三角形类
    
    属性
    ----
    base: 三角形的底。
    height: 三角形的高。

    Property 属性
    -------------
    area: 三角形的面积。
    """
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height

    @property
    def area(self):
        result = self.base * self.height / 2
        return int(result) if int(result) == result else result

    def __repr__(self):
        return ('三角形\n'
                + f'底: {self.base}\n'
                + f'高: {self.height}\n'
                + f'面积: {self.area}\n')


class Trapezoid:
    """梯形类
    
    属性
    ----
    base1/base2: 梯形的上、下底。
    height: 梯形的高。

    Property 属性
    -------------
    area: 梯形的面积。
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
        shape = '梯形'
        # 一组对边平行且相等的四边形是平行四边形。
        if self.base1 == self.base2:
            shape = '平行四边形'
        return (f'{shape}\n'
                + f'上底: {self.base1}\n'
                + f'下底: {self.base2}\n'
                + f'高: {self.height}\n'
                + f'面积: {self.area}\n')


parallelogram = Parallelogram(4, 3)
print(parallelogram.area)
# 如果取消下面语句的注释，给 area 赋值，运行时会报错。
# parallelogram.area = 10  # AttributeError: can't set attribute 'area'
parallelogram.base = 5
print(parallelogram)

# triangle = Triangle(4, 3)
# print(triangle)

# trapezoid = Trapezoid(3, 5, 4)
# print(trapezoid)
