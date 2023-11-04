"""多位数乘一位数乘法竖式

关于程序的几点说明：
1. 程序会将用户输入的一个多位自然数和一个一位自然数用乘法竖式求积，并将结果以竖式的形式显示在屏幕上。
2. 程序在求积时真实模拟了乘法竖式的运算过程，而不是使用编程语言内置的 "*" 运算符直接得到结果。
3. short_multiply() 函数有一个是否显示竖式的参数，这样以后在多位数乘多位数乘法竖式的程序中调用
   该函数时，可以只返回结果，不显示竖式。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def short_multiply(num1, num2, display=False):
    """模拟乘法竖式的运算过程求出 num1 和 num2 的积 (而不是直接用 num1 * num2),
    并将结果返回。可以选择是否将乘法竖式显示在屏幕上。

    num1: 字符串类型的自然数。
    num2: 字符串类型的一位自然数。
    display: 是否显示乘法竖式，默认为不显示。
    """
    if num1 == '0' or num2 == '0':
        product = '0'
    else:
        product = ''
        carry = 0
        # 从 num1 最右边的个位开始，与 num2 做一位数乘一位数的乘法。
        for i in range(len(num1) - 1, -1, -1):
            product_i = int(num1[i]) * int(num2) + carry
            carry = product_i // 10
            product_i = product_i % 10
            product = str(product_i) + product
        # 如果乘到最高位有进位的话，将该进位作为积的最高位。
        if carry != 0:
            product = str(carry) + product

    if display:
        # 显示乘法竖式。
        # 把竖式中所有数的各数位之间插入一个空格，使竖式显示更加清晰。
        num1 = ' '.join(list(num1))
        num2 = ' '.join(list(num2))
        product = ' '.join(list(product))
        # 如果积不为 0，则积最大，竖式的宽度由积决定，否则由 num1 决定。
        if product == '0':
            width = len(num1) + 2
        else:
            width = len(product) + 2
        # 竖式中所有数右对齐。
        print(num1.rjust(width))
        print('x' + num2.rjust(width - 1))
        print('-' * width)
        print(product.rjust(width))

    return product


# 使用特殊变量 __name__ 确保此程序在作为模块被其它程序引用时，以下代码不会被执行。
if __name__ == '__main__':
    num1 = input_natural_number('输入第一个自然数: ')
    num2 = input_natural_number('输入第二个自然数（一位数）: ', digit_count=1)
    short_multiply(num1, num2, display=True)
