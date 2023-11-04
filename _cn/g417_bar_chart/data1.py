"""创建带有绘图功能的表格类的子类 Data

关于程序的几点说明：
1. Data 类继承了 Table 类的属性和方法，并增加了绘制纵向条形统计图和横向条形统计图的两个方法。
"""

import sys
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from g323_table.table import Table


class Data(Table):
    """Data 类是 Table 类的子类。Data 类继承了 Table 类的属性和方法，并增加了绘制纵向条形统计图和
    横向条形统计图的两个方法。

    方法
    ----
    bar(row=0): 为表格的第 row 行数据绘制纵向条形统计图 (默认绘制首行数据)。
    barh(row=0): 为表格的第 row 行数据绘制横向条形统计图 (默认绘制首行数据)。
    """
    def bar(self, row=0, title=None, xlabel=None, ylabel=None, int_tick=True):
        """为表格的第 row 行数据绘制纵向条形统计图。

        row: 绘制表格第几行数据，默认是首行。
        title: 条形统计图的标题。
        xlabel: 条形统计图横轴说明。
        ylabel: 条形统计图纵轴说明，默认使用该行的表格行标题。
        int_tick: 刻度值是否必须为整数。
        """
        _, ax = plt.subplots(figsize=(10, 6))
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        ax.bar(self.col_headers, self.data[row], width = 0.4)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel if ylabel is not None else self.row_headers[row])
        plt.show()

    def barh(self, row=0, title=None, xlabel=None, ylabel=None, int_tick=True):
        """为表格的第 row 行数据绘制横向条形统计图。

        row: 绘制表格第几行数据，默认是首行。
        title: 条形统计图的标题。
        xlabel: 条形统计图横轴说明，默认使用该行的表格行标题。
        ylabel: 条形统计图纵轴说明。
        int_tick: 刻度值是否必须为整数。
        """
        _, ax = plt.subplots(figsize=(10, 6))
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=int_tick))
        ax.barh(self.col_headers, self.data[row], height = 0.4)
        ax.set_title(title)
        ax.set_xlabel(xlabel if xlabel is not None else self.row_headers[row])
        ax.set_ylabel(ylabel)
        plt.show()


TITLE = '喜欢某种蔬菜的学生人数统计图'
LABEL_ITEM = '蔬菜'
LABEL_VALUE = ['喜欢的人数']
VEGETABLES = ['西红柿', '萝卜', '黄瓜', '茄子']

data = Data(row_headers=LABEL_VALUE, col_headers=VEGETABLES)
data.random()
print(data)

# 在 Matplotlib 中使用中文字体，SimHei 是 Windows 的内置字体，Arial Unicode MS 是 MacOS 的内置字体。
font_names = ['SimHei', 'Arial Unicode MS']
mpl.rcParams['font.sans-serif'] = font_names + mpl.rcParams['font.sans-serif']

data.bar(title=TITLE, xlabel=LABEL_ITEM)
data.barh(title=TITLE, ylabel=LABEL_ITEM)
