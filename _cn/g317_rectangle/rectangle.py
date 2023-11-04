"""创建长方形类 Rectangle

关于程序的几点说明：
1. 用 get_perimeter() 方法计算长方形对象的周长。
2. 用 is_square() 方法判断长方形对象是否是一个正方形。
"""

class Rectangle():
    """长方形类

    属性
    ----
    length: 长方形的长。
    width: 长方形的宽。

    方法
    ----
    get_perimeter(): 返回长方形的周长。
    is_square(): 正方形返回 True, 否则返回 False。
    """
    def __init__(self, length=1, width=None):
        """构造函数
        
        length: 长方形的长。
        width: 长方形的宽。

        Rectangle(m, n): 实例化一个长是 m 宽是 n 的长方形对象。
        Rectangle(m): 实例化一个长方形对象，代表边长是 m 的正方形。
        Rectangle(): 实例化一个长方形对象，代表边长是 1 的正方形。
        """
        if not width:
            width = length
        self.length = length
        self.width = width

    def get_perimeter(self):
        """返回长方形的周长。"""
        return (self.length + self.width) * 2

    def is_square(self):
        """正方形返回 True, 否则返回 False。"""
        return self.length == self.width

    def __repr__(self):
        """使用 print() 函数输出长方形对象时的显示内容。"""
        string = ''
        if self.is_square():
            string += ('正方形\n'
                     + f'边长: {self.length}\n')
        else:
            string += ('长方形\n'
                     + f'长: {self.length}\n'
                     + f'宽: {self.width}\n')
        string += f'周长: {self.get_perimeter()}\n'

        return string


rect1 = Rectangle(5, 2)  # rect1 是一个长方形。
print(rect1)

rect2 = Rectangle(3)  # rect2 是一个正方形。
print(rect2)

rect2.length = 4  # 长改变后和宽不再相等，现在 rect2 是一个长方形。
print(rect2)
