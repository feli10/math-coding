"""减法竖式

关于程序的几点说明：
1. 程序会将用户输入的两个自然数用减法竖式求差（大数减小数），并将结果以竖式的形式显示在屏幕上。
2. 程序在求差时真实模拟了减法竖式的运算过程，而不是使用编程语言内置的 "-" 运算符直接得到结果。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def sub_vertical(num1, num2):
    """模拟减法竖式的运算过程求出 num1 和 num2 的差 (而不是直接用 num1 - num2),
    并将结果以减法竖式的形式显示在屏幕上。

    num1, num2: 两个字符串类型的自然数。
    """
    # 确保两数中较大的是 num1，较小的是 num2。
    if int(num1) < int(num2):
        num1, num2 = num2, num1

    diff = ''
    carry = 0
    # 从最右边的个位开始做减法。
    for i in range(-1, -len(num1) - 1, -1):
        diff_i = int(num1[i]) - carry
        if i >= -len(num2):
            diff_i -= int(num2[i])
        if diff_i < 0:
            carry = 1
            diff_i += 10
        else:
            carry = 0
        diff = str(diff_i) + diff
    # 删除差的最高位上可能出现的一个或多个 0。
    diff = str(int(diff))

    # 显示减法竖式。
    # 把竖式中所有数的各数位之间插入一个空格，使竖式显示更加清晰。
    num1 = ' '.join(list(num1))
    num2 = ' '.join(list(num2))
    diff = ' '.join(list(diff))
    # 因为减法中被减数最大（即位数最多），所以竖式的宽度是由 num1 决定的。
    width = len(num1) + 2
    # 竖式中所有数右对齐。
    print(num1.rjust(width))
    print('-' + num2.rjust(width - 1))
    print('-' * width)
    print(diff.rjust(width))


num1 = input_natural_number('输入第一个自然数: ')
num2 = input_natural_number('输入第二个自然数: ')
sub_vertical(num1, num2)
