"""加法竖式

关于程序的几点说明：
1. 程序会将用户输入的两个自然数用加法竖式求和，并将结果以竖式的形式显示在屏幕上。
2. 程序在求和时真实模拟了加法竖式的运算过程，而不是使用编程语言内置的 "+" 运算符直接得到结果。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def add_vertical(num1, num2):
    """模拟加法竖式的运算过程求出 num1 和 num2 的和 (而不是直接用 num1 + num2),
    并将结果以加法竖式的形式显示在屏幕上。

    num1, num2: 两个字符串类型的自然数。
    """
    # 确保两数中位数较多的是 num1（加法竖式中，习惯上位数较多的加数在上面）。
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    the_sum = ''
    carry = 0
    # 从最右边的个位开始做加法。
    for i in range(-1, -len(num1) - 1, -1):
        sum_i = int(num1[i]) + carry
        if i >= -len(num2):
            sum_i += int(num2[i])
        carry = sum_i // 10
        sum_i = sum_i % 10
        the_sum = str(sum_i) + the_sum
    # 如果加到加数的最高位还有进位的话，将该进位作为和的最高位。
    if carry != 0:
        the_sum = str(carry) + the_sum

    # 显示加法竖式。
    # 把竖式中所有数的各数位之间插入一个空格，使竖式显示更加清晰。
    num1 = ' '.join(list(num1))
    num2 = ' '.join(list(num2))
    the_sum = ' '.join(list(the_sum))
    # 因为加法中和最大（即位数最多），所以竖式的宽度是由和决定的。
    width = len(the_sum) + 2
    # 竖式中所有数右对齐。
    print(num1.rjust(width))
    print('+' + num2.rjust(width - 1))
    print('-' * width)
    print(the_sum.rjust(width))


num1 = input_natural_number('输入第一个自然数: ')
num2 = input_natural_number('输入第二个自然数: ')
add_vertical(num1, num2)
