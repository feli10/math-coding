"""复式条形统计图和平均数

关于程序的几点说明：
1. 程序改进了 data1.py (G417) 中的 Data 类，使绘制条形统计图的方法 bar() 和 barh() 现在可以绘制表现多行数据的
   复式条形统计图。
2. 程序还为 Data 类增添了两个新的方法 avg_row() 和 avg_col()，分别用于求指定行或列数据的平均数。
"""

import sys
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from g323_table.table import Table


class Data(Table):
    """Data 类是 Table 类的子类。Data 类继承了 Table 类的属性和方法，还拥有绘制复式条形统计图以及求平均数的方法。

    方法
    ----
    bar(*row): 为给定的一行或多行数据绘制纵向复式条形统计图。
    barh(*row): 为给定的一行或多行数据绘制横向复式条形统计图。
    avg_row(row): 计算第 row 行数据的平均数，如果没有指定 row, 计算每一行数据的平均数。
    avg_col(col): 计算第 col 列数据的平均数，如果没有指定 col, 计算每一列数据的平均数。
    line(*row): 为给定的一行或多行数据绘制复式折线统计图。
    """
    def bar(self, *rows, title=None, xlabel=None, ylabel=None, int_tick=True):
        """为表格中给定的一行或多行数据绘制纵向复式条形统计图。

        rows: 绘制哪几行数据，默认是所有行。
        title: 复式条形统计图的标题。
        xlabel: 复式条形统计图横轴说明。
        ylabel: 复式条形统计图纵轴说明。
        int_tick: 刻度值是否必须为整数。
        """
        _, ax = plt.subplots(figsize=(10, 6))
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        # 如果一行都没给，绘制所有行。
        n = len(rows)
        if n == 0:
            n = self.row_count
            rows = tuple(range(n))
        # 根据一组竖条的数目，设置一组竖条的宽度。
        if n == 1:
            WIDTH = 0.4
        elif n < 5:
            WIDTH = 0.6
        else:
            WIDTH = 0.8
        # 获取一个竖条的宽度。
        width = WIDTH / n
        x = range(self.col_count)
        for i, row in enumerate(rows):
            # 获取代表一行数据的一组竖条，每个竖条中点的位置。
            pos = [value - WIDTH/2 + width/2 + width * i for value in x]
            rect = ax.bar(pos, self.data[row], width=width, label=self.row_headers[row])
            ax.bar_label(rect)
        ax.set_xticks(x, self.col_headers)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()
        plt.show()

    def barh(self, *rows, title=None, xlabel=None, ylabel=None, int_tick=True):
        """为表格中给定的一行或多行数据绘制横向复式条形统计图。

        rows: 绘制哪几行数据，默认是所有行。
        title: 复式条形统计图的标题。
        xlabel: 复式条形统计图横轴说明。
        ylabel: 复式条形统计图纵轴说明。
        int_tick: 刻度值是否必须为整数。
        """
        _, ax = plt.subplots(figsize=(10, 6))
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        # 如果一行都没给，绘制所有行。
        n = len(rows)
        if n == 0:
            n = self.row_count
            rows = tuple(range(n))
        # 根据一组竖条的数目，设置一组竖条的高度。
        if n == 1:
            HEIGHT = 0.4
        elif n < 5:
            HEIGHT = 0.6
        else:
            HEIGHT = 0.8
        # 获取一个竖条的高度。
        height = HEIGHT / n
        y = range(self.col_count)
        for i, row in enumerate(rows):
            # 获取代表一行数据的一组竖条，每个竖条中点的位置。
            pos = [value + HEIGHT/2 - height/2 - height * i for value in y]
            rect = ax.barh(pos, self.data[row], height=height, label=self.row_headers[row])
            ax.bar_label(rect)
        ax.set_yticks(y, self.col_headers)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()
        plt.show()

    def avg_row(self, row=None, rounding=0):
        """计算第 row 行数据的平均数，如果没有指定 row, 返回一个包含每一行数据平均数的列表。

        row: 计算哪一行数据的平均数。如果没指定，计算每一行数据的平均数。
        rounding: 平均数保留几位小数。
        """
        def avg_one_row(row):
            """计算第 row 行数据的平均数。"""
            avg = sum(self.data[row])/self.col_count
            if rounding == 0:
                return round(avg)
            return round(avg, rounding)

        if row is not None:
            return avg_one_row(row)
        avgs = []
        for i in range(self.row_count):
            avgs.append(avg_one_row(i))
        return avgs

    def avg_col(self, col=None, rounding=0):
        """计算第 col 列数据的平均数，如果没有指定 col, 返回一个包含每一列数据平均数的列表。

        col: 计算哪一列数据的平均数。如果没指定，计算每一列数据的平均数。
        rounding: 平均数保留几位小数。
        """
        def avg_one_col(col):
            """计算第 col 列数据的平均数。"""
            total = 0
            for i in range(self.row_count):
                total += self.data[i][col]
            avg = total / self.row_count
            if rounding == 0:
                return round(avg)
            return round(avg, rounding)

        if col is not None:
            return avg_one_col(col)
        avgs = []
        for j in range(self.col_count):
            avgs.append(avg_one_col(j))
        return avgs

    def line(self, *rows, title=None, xlabel=None, ylabel=None, int_tick=True):
        """为表格中给定的一行或多行数据绘制复式折线统计图。

        rows: 绘制哪几行数据，默认是所有行。
        title: 复式折线统计图的标题。
        xlabel: 复式折线统计图横轴说明。
        ylabel: 复式折线统计图纵轴说明。
        int_tick: 刻度值是否必须为整数。
        """
        _, ax = plt.subplots()
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        # 如果一行都没给，绘制所有行。
        n = len(rows)
        if n == 0:
            n = self.row_count
            rows = tuple(range(n))
        n = len(rows)
        # 绘制复式折线统计图。
        for row in rows:
            ax.plot(self.col_headers, self.data[row], marker='o', label=self.row_headers[row])
            # 在每个数据点上面标注数据值。
            for i in range(self.col_count):
                ax.annotate(str(self.data[row][i]), (i, self.data[row][i]),
                            textcoords='offset points', xytext=(0, 6), ha='center')
        ax.set_yticks(list(range(MAX_HOURS * 2)))
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()
        ax.grid(True)
        plt.show()


MAX_HOURS = 3
TITLE = '每日学习时间'
XLABEL = '天'
YLABEL = '小时数'
DAYS = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
SUBJECTS = ['语文', '数学', '科学']

# 创建 data 对象并生成 data 对象的数据。
data = Data(row_headers=SUBJECTS, col_headers=DAYS)
data.random(0, 3)
print(data)

# 在 Matplotlib 中使用中文字体，SimHei 是 Windows 的内置字体，Arial Unicode MS 是 MacOS 的内置字体。
font_names = ['SimHei', 'Arial Unicode MS']
mpl.rcParams['font.sans-serif'] = font_names + mpl.rcParams['font.sans-serif']

# 绘制复式折线统计图。
data.line(title=TITLE, xlabel=XLABEL, ylabel=YLABEL)
