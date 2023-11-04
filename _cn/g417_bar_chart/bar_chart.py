"""应用 Matplotlib 绘制条形统计图

关于程序的几点说明：
1. 在 Matplotlib 中，一个窗口内的所有绘图称作一个 Figure, 一个 Figure 可能包含一个或多个绘图，
   每个绘图称作一个 Axes。
2. Matplotlib 有两种代码风格：
   - 面向对象 (OO) 风格：显式创建 Figure 和 Axes, 并调用它们的方法进行绘图。
   - pyplot 风格：使用 pyplot 隐式创建和管理 Figure 和 Axes, 并使用 pyplot 的函数进行绘图。
   一般建议使用面向对象风格，特别是对于复杂的绘图项目，而 pyplot 风格对于快速交互绘图来说非常方便。
3. 作为对比，程序分别使用两种代码风格各在一个 Figure 上绘制条形统计图，绘图效果完全相同。
4. 每个 Figure 有横向排列的两个 Axes, 一个是纵向条形统计图，另一个是横向条形统计图。
"""

from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt


RAND_MAX = 50
TITLE = '喜欢某种蔬菜的学生人数统计图'
LABEL_ITEM = '蔬菜'
LABEL_VALUE = '人数'
ITEMS = ['西红柿', '萝卜', '黄瓜', '茄子', '白菜']


def explicit_oo_style():
    """使用 Matplotlib 的面向对象代码风格在一个 Figure 上绘制纵向和横向条形统计图。"""
    # 创建一个新的 Figure，Figure 上有呈一行两列分布的两个 Axes。
    fig, axs = plt.subplots(1, 2, figsize=(18, 6))
    fig.suptitle(TITLE)
    # 在第一个 Axes 上绘制纵向条形统计图。
    axs[0].bar(ITEMS, values, width=0.4)
    axs[0].set_title('纵向条形统计图')
    axs[0].set_xlabel(LABEL_ITEM)
    axs[0].set_ylabel(LABEL_VALUE)
    # 在第二个 Axes 上绘制横向条形统计图。
    axs[1].barh(ITEMS, values, color='maroon', height=0.4)
    axs[1].set_title('横向条形统计图')
    axs[1].set_xlabel(LABEL_VALUE)
    axs[1].set_ylabel(LABEL_ITEM)


def implicit_pyplot_style():
    """使用 Matplotlib 的 pyplot 代码风格在一个 Figure 上绘制纵向和横向条形统计图。"""
    # 创建一个新的 Figure。
    plt.figure(figsize=(18, 6))
    plt.suptitle(TITLE)
    # 在 Figure 的第一行第一列添加一个 Axes，并将其作为当前 Axes。
    plt.subplot(121)
    # 在当前 Axes 上绘制纵向条形统计图。
    plt.bar(ITEMS, values, width=0.4)
    plt.title('纵向条形统计图')
    plt.xlabel(LABEL_ITEM)
    plt.ylabel(LABEL_VALUE)
    # 在 Figure 的第一行第二列添加一个 Axes，并将其作为当前 Axes。
    plt.subplot(122)
    # 在当前 Axes 上绘制横向条形统计图。
    plt.barh(ITEMS, values, color='maroon', height=0.4)
    plt.title('横向条形统计图')
    plt.xlabel(LABEL_VALUE)
    plt.ylabel(LABEL_ITEM)


# 随机生成数据。
values = []
for i in range(len(ITEMS)):
    values.append(randint(0, RAND_MAX))

# 在 Matplotlib 中使用中文字体，SimHei 是 Windows 的内置字体，Arial Unicode MS 是 MacOS 的内置字体。
font_names = ['SimHei', 'Arial Unicode MS']
mpl.rcParams['font.sans-serif'] = font_names + mpl.rcParams['font.sans-serif']

# 使用 Matplotlib 的两种代码风格绘制条形统计图，绘图效果完全相同。
explicit_oo_style()
implicit_pyplot_style()

# 显示所有 Figure。
plt.show()
