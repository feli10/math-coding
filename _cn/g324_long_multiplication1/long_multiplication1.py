"""多位数乘法竖式

关于程序的几点说明：
1. 程序会将用户输入的两个自然数用乘法竖式求积，并将结果以竖式的形式显示在屏幕上。
2. 多位数乘法竖式的运算过程可以分为两步，第一步是计算多个多位数乘一位数的乘法，第二步是把第一步得到的
   多个乘积相加。此程序通过调用之前编写的《多位数乘一位数乘法竖式》(G316) 程序来完成第一步的工作。
3. long_multipy_core() 函数是模拟多位数乘法竖式运算过程计算两数乘积的代码，把它从主要负责显示乘法竖式的
   long_multiply() 函数中分离出来，是为了在未来最终版本的《通用乘法竖式》(G414) 程序中，可以复用乘法竖式
   运算部分的代码。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number
from g316_short_multiplication.short_multiplication import short_multiply


def add_multiple(nums):
    """模拟多个数加法竖式的运算过程求出 nums 列表中所有数的和。 
    
    nums: 字符串类型的自然数列表。
    """
    # 在所有数前面补零 ，让它们都和列表中数位最多的数的位数一样多。
    max_digit_count = max(len(num) for num in nums)
    for i, num in enumerate(nums):
        nums[i] = '0' * (max_digit_count - len(num)) + num

    the_sum = ''
    carry = 0
    # 从最右边的个位开始做加法。
    for i in range(max_digit_count - 1, -1, -1):
        sum_i = sum(int(num[i]) for num in nums) + carry
        carry = sum_i // 10
        sum_i = sum_i % 10
        the_sum = str(sum_i) + the_sum
    # 如果加到加数的最高位还有进位的话，将该进位作为和的最高位。
    if carry != 0:
        the_sum = str(carry) + the_sum
    return the_sum


def long_multiply_core(num1, num2):
    """模拟乘法竖式的运算过程求出 num1 和 num2 的积 (而不是直接用 num1 * num2), 并将结果返回。
    同时返回的还有 num1 和 num2 每一位的乘积列表，用于显示乘法竖式。

    num1, num2: 两个字符串类型的自然数。
    """
    # 调用之前程序中的 short_multiply() 函数，得到 num1 和 num2 每一位的乘积列表 short_products。
    short_products = []
    short_products_revised = []
    for i in range(len(num2) - 1, -1, -1):
        short_product = short_multiply(num1, num2[i])
        short_products.append(short_product)
        # 用 num2 的某一位乘 num1 时，根据该位所在的数位，在积的末尾补相应数量的零，修订后得到积的真实值，
        # 稍后做加法时使用。
        short_products_revised.append(short_product + '0' * (len(num2) - 1 - i))

    # 把修订后的乘积列表中的数求和，即为 num1 和 num2 的积。
    product = add_multiple(short_products_revised)
    return product, short_products


def expand(string, char=' '):
    """在 string 的每个字符之间插入 char, 默认插入空格。"""
    return char.join(list(string))


def long_multiply(num1, num2):
    """模拟乘法竖式的运算过程求出 num1 和 num2 的积，并将结果以乘法竖式的形式显示在屏幕上。

    num1, num2: 两个字符串类型的自然数。
    """
    # 确保两数中位数较多的是 num1（乘法竖式中，习惯上位数较多的因数在上面）。
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    product, short_products = long_multiply_core(num1, num2)

    # 显示乘法竖式。
    # 把竖式中所有数的各数位之间插入一个空格，使竖式显示更加清晰。
    num1 = expand(num1)
    num2 = expand(num2)
    product = expand(product)
    # 如果积不为 0，则积最大，竖式的宽度由积决定，否则由 num1 决定。
    if product == '0':
        width = len(num1) + 2
    else:
        width = len(product) + 2

    print(num1.rjust(width))
    print('x' + num2.rjust(width - 1))
    print('-' * width)
    if len(num2) != 1:
        for i, short_product in enumerate(short_products):
            if short_product != '0':
                print(expand(short_product).rjust(width - i * 2))
        print('-' * width)
    print(product.rjust(width))


# 使用特殊变量 __name__ 确保此程序在作为模块被其它程序引用时，以下代码不会被执行。
if __name__ == '__main__':
    num1 = input_natural_number('输入第一个自然数: ')
    num2 = input_natural_number('输入第二个自然数: ')
    long_multiply(num1, num2)
