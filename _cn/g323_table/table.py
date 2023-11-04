"""创建表格类 Table 及在字符界面显示表格

关于程序的几点说明：
1. 程序创建了一个表格类，包含行标题、列标题、行数、列数、表格数据等属性，以及数据填充（指定或随机）、数据清除、
   删除某行或某列等方法。
2. 程序的一个主要功能是在字符界面中显示表格，包含行、列分割线。表格内容可以使用中西文字符，单元格的宽度会根据
   表格内容进行自动调整，行、列标题和数据会居中显示在单元格中。
3. 表格的数据存储在一个二维列表中，所以程序中涉及大量对 list 的操作，特别是多次使用 list comprehension 来
   创建列表，以使程序更加简洁。
"""

from random import randint


def get_width(text):
    """获取 text 的总宽度，由于中、西文字符的宽度比是 2:1, 所以一个中文字符算两个宽度单位。
    
    text: 包含不同宽度字符的字符串。
    """
    width = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff':  # 中文字符的 Unicode 范围。
            width += 2
        else:
            width += 1
    return width


class Table:
    """表格类
    
    属性
    ----
    row_headers: 行标题列表。
    col_headers: 列标题列表。
    row_count: 行数。
    col_count: 列数。
    shape: 表格行列数，"m x n" 形式的字符串。 
    data: 存储表格数据的二维列表。用 data[row][column] 获取单元格数据. 序号从 0 开始。

    方法
    ----
    fill(value=0): 所有单元格填入 value。
    random(start=0, end=20): 所有单元格填入 start 至 end 之间的随机整数。
    clear(row, col): 清除全部、一行、一列或一个单元的数据。
    del_row(*rows): 删除表格的指定行。
    del_col(*cols): 删除表格的指定列。
    """
    def __init__(self, row_count=2, col_count=4, row_headers=None, col_headers=None):
        """构造表格对象所需的所有属性。

        row_count: 行数。
        col_count: 列数。
        row_headers: 行标题列表。如果没给出，自动设置为 "第0行, 第1行, 第2行..."。
        col_headers: 列标题列表。如果没给出，自动设置为 "第0列, 第1列, 第2列..."。

        Table(): 实例化一个 2 行 4 列的表格对象。
        Table(row_count, col_count): 实例化一个指定行列数的表格对象。
        Table(row_headers, col_headers): 
            实例化一个设定行、列标题的的表格对象。在这种情况下，表格的行数和列数由行、列标题列表中的元素数决定，
            而不是 row_count 和 col_count 参数。
        """
        if not row_headers:
            self.row_headers = [f'第{str(i)}行' for i in range(row_count)]
            self.row_count = row_count
        else:
            self.row_headers = row_headers
            self.row_count = len(row_headers)
        if not col_headers:
            self.col_headers = [f'第{str(i)}列' for i in range(col_count)]
            self.col_count = col_count
        else:
            self.col_headers = col_headers
            self.col_count = len(col_headers)
        self.shape = str(self.row_count) + ' x ' + str(self.col_count)
        # 初始化所有数据为空白。
        self.data = [['' for j in range(self.col_count)] for i in range(self.row_count)]
        # 用于显示表格对象的内部变量。
        self._cell_width = 0

    def fill(self, value=0):
        """所有单元格填入 value。"""
        self.data = [[value for j in range(self.col_count)] for i in range(self.row_count)]

    def random(self, start=0, end=20):
        """所有单元格填入 start 至 end 之间的随机整数。"""
        self.data = [[randint(start, end) for j in range(self.col_count)]
                     for i in range(self.row_count)]

    def clear(self, row, col):
        """清除全部、一行、一列或一个单元的数据。
        
        clear(): 清除全部数据。
        clear(row=m): 清除第 m 行数据。
        clear(col=n): 清除第 n 列数据。
        clear(row=m, col=n): 清除 data[m][n] 单元格数据。
        """
        if row is not None and col is None:
            for j in range(self.col_count):
                self.data[row][j] = ''
        elif col is not None and row is None:
            for i in range(self.row_count):
                self.data[i][col] = ''
        elif row is not None and col is not None:
            self.data[row][col] = ''
        else:
            self.fill('')

    def del_row(self, *rows):
        """删除表格的指定行。"""
        # 按序号大小从后向前进行删除，因为在列表中删除后面的元素不会影响前面元素的序号。
        rows = sorted(rows, reverse=True)
        for row in rows:
            del self.data[row]
            del self.row_headers[row]
            self.row_count -= 1
        self.shape = str(self.row_count) + " x " + str(self.col_count)

    def del_col(self, *cols):
        """删除表格的指定列。"""
        # 按序号大小从后向前进行删除，因为在列表中删除后面的元素不会影响前面元素的序号。
        cols = sorted(cols, reverse=True)
        for row_data in self.data:
            for col in cols:
                del row_data[col]
        for col in cols:
            del self.col_headers[col]
            self.col_count -= 1
        self.shape = str(self.row_count) + " x " + str(self.col_count)

    def __repr__(self):
        """使用 print() 函数输出表格对象时的显示内容。"""
        string = '\n'

        def print_divider():
            """输出行与行之间的分割线。"""
            nonlocal string
            for _ in range(self.col_count + 1):
                string += ('|' + '-' * self._cell_width)
            string += '|\n'

        def print_cell(cell):
            """输出一个单元格，数据居中显示。"""
            nonlocal string
            space = self._cell_width - get_width(cell)
            space_after = space // 2
            space_before = space_after + space % 2
            string += ('|' + ' ' * space_before + cell + ' ' * space_after)

        def print_col_headers():
            """输出列标题。"""
            nonlocal string
            string += ('|' + ' ' * self._cell_width)
            for text in self.col_headers:
                print_cell(text)
            string += '|\n'

        # 把所有行、列标题和数据放在一个一维列表中。
        all_cells = self.col_headers + self.row_headers + [str(x) for row in self.data for x in row]
        # 表格的宽度由所有行、列标题和数据中最宽的数据决定。
        self._cell_width = max(get_width(cell) for cell in all_cells) + 2
        print_divider()
        print_col_headers()
        print_divider()
        for i, text in enumerate(self.row_headers):
            print_cell(text)
            for j in range(self.col_count):
                print_cell(str(self.data[i][j]))
            string += '|\n'
            print_divider()
        return string


# 使用特殊变量 __name__ 确保此程序在作为模块被其它程序引用时，以下代码不会被执行。
if __name__ == '__main__':
    # 三个班喜欢某种蔬菜的学生人数统计表。
    vegetables = ['萝卜', '黄瓜', '西红柿', '玉米']
    classes = ['一班', '二班', '三班']
    table = Table(row_headers=classes, col_headers=vegetables)
    table.random()
    print(table)
    print(table.shape)
    table.del_row(1)
    table.del_col(2)
    print(table)
    print(table.shape)
