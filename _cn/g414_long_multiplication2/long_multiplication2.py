"""通用乘法竖式

关于程序的几点说明：
1. 程序会将用户输入的两个自然数用乘法竖式求积，并将结果以竖式的形式显示在屏幕上。
2. 此程序是对 long_multiplication1.py (G324) 的升级，对于因数末尾有零的情况，先不考虑因数末尾的零，
   把两个因数最右侧的非零位对齐进行乘法竖式运算，最后再把因数末尾的所有零添加到乘积的末尾。两个程序的乘法
   竖式核心运算过程是一致的，所以此程序仍调用 long_multipy_core() 函数计算两个因数（忽略末尾的零）的乘积。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number
from g324_long_multiplication1.long_multiplication1 import long_multiply_core, expand


def separate_trailing_zeros(num):
    """返回 num 去掉末尾零后的部分, 以及 num 末尾零的数量。
    
    num: 字符串类型的自然数。
    """
    if num == '0':
        num_main = '0'
        num_trailing_zero_count = 0
    else:
        num_main = num.rstrip('0')
        num_trailing_zero_count = len(num) - len(num_main)
    return num_main, num_trailing_zero_count


def long_multiply(num1, num2):
    """模拟乘法竖式的运算过程（因数末尾的零不参与竖式运算）求出 num1 和 num2 的积，
    并将结果以乘法竖式的形式显示在屏幕上。

    num1, num2: 两个字符串类型的自然数。
    """
    # 去掉因数末尾的零，同时记录下末尾零的数量。
    num1_main, num1_trailing_zero_count = separate_trailing_zeros(num1)
    num2_main, num2_trailing_zero_count = separate_trailing_zeros(num2)

    # 确保在去掉零后的两个因数中，位数较多的是 num1（乘法竖式中，习惯上位数较多的因数在上面）。
    if len(num1_main) < len(num2_main):
        num1_main, num2_main = num2_main, num1_main
        num1_trailing_zero_count, num2_trailing_zero_count \
            = num2_trailing_zero_count, num1_trailing_zero_count

    if num2_main == '0':
        product = '0'
    else:
        # 模拟乘法竖式的运算过程计算忽略末尾零后两个因数的乘积。
        product_main, short_products = long_multiply_core(num1_main, num2_main)
        # 把因数末尾的所有零添加到乘积的末尾。
        product = product_main + '0' * (num1_trailing_zero_count + num2_trailing_zero_count)

    # 显示乘法竖式。
    # 如果积不为 0，则积最大，竖式的宽度由积决定，否则由 num1 决定。
    if product == '0':
        # 把 num1 的各数位之间插入一个空格，使竖式显示更加清晰。
        num1 = expand(num1)
        width = len(num1) + 2
        print(num1.rjust(width))
        print('x' + num2.rjust(width - 1))
        print('-' * width)
        print(product.rjust(width))
    else:
        # 把竖式中所有数的各数位之间插入一个空格，使竖式显示更加清晰。
        num1_main = expand(num1_main)
        num2_main = expand(num2_main)
        product_main = expand(product_main)
        product = expand(product)
        width_main = len(product_main) + 2
        width = len(product) + 2
        # 对齐两个因数最右侧的非零位。（因数末尾的零不需要对齐）
        print(num1_main.rjust(width_main) + ' 0' * num1_trailing_zero_count)
        print('x' + num2_main.rjust(width_main - 1) + ' 0' * num2_trailing_zero_count)
        print('-' * width)
        if len(num2_main) != 1:
            for i, short_product in enumerate(short_products):
                if short_product != '0':
                    print(expand(short_product).rjust(width_main - i * 2))
            print('-' * width)
        print(product.rjust(width))


num1 = input_natural_number('输入第一个自然数: ')
num2 = input_natural_number('输入第二个自然数: ')
long_multiply(num1, num2)
