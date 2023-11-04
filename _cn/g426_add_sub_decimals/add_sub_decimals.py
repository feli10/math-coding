"""小数加减法竖式

关于程序的几点说明：
1. 小数加减法竖式本质上就是小数点对齐的整数加减法竖式，所以程序重组了《加法竖式》(G314) 和《减法竖式》(G315) 程序，
   并在此基础上加入了小数加减法竖式的计算过程：
   1) 在小数位数较少的小数末尾补零，使两个小数具有相同的小数位数，即小数点对齐；
   2) 忽略小数点，做整数加减法竖式（同 G314/G315 的程序）；
   3) 在与运算数的小数点相同的位置，为计算结果添加小数点；
   4) 删除在第一步中向加数或减数末尾添加的零，只保留被减数末尾的零；
   5) 对齐小数点位置，显示竖式（同 G314/G315 的程序）；
   6) 对计算结果进行化简，去掉末尾不必要的零，显示最终结果。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal, remove_trailing_zeros


def add_vertical(num1, num2):
    """模拟加法竖式的运算过程求出 num1 和 num2 的和 (而不是直接用 num1 + num2),
    并将结果以加法竖式的形式显示在屏幕上。

    num1, num2: 两个字符串类型的自然数。
    """
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

    return the_sum


def sub_vertical(num1, num2):
    """模拟减法竖式的运算过程求出 num1 和 num2 的差 (而不是直接用 num1 - num2),
    并将结果以减法竖式的形式显示在屏幕上。

    num1, num2: 两个字符串类型的自然数。
    """
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

    return diff


def display_vertical(num1, num2, result, operator):
    """显示竖式。

    num1, num2: 字符串类型的非负小数或整数。
    result: 字符串类型的整数或小数, num1 与 num2 的和或差。
    operator: "+" 或 "-"。
    """
    # 把竖式中所有数的各数位之间插入一个空格，使竖式显示更加清晰。
    num1 = ' '.join(list(num1))
    num2 = ' '.join(list(num2))
    result = ' '.join(list(result))
    # 竖式的宽度由所有数中数位最多的数决定。
    width = max(len(num1), len(num2), len(result)) + 2
    # 竖式中所有数右对齐。
    print(num1.rjust(width))
    print(operator + num2.rjust(width - 1))
    print('-' * width)
    print(result.rjust(width))


def add_sub_decimals(dec1, dec2, operator):
    """模拟小数加减法竖式的运算过程求出 dec1 和 dec2 的和或差，并将结果以加法竖式的形式显示在屏幕上。

    dec1, dec2: 字符串类型的小数。
    operator: "+" 或 "-"
    """
    dec_place_count1 = len(dec1) - 1 - dec1.index('.')
    dec_place_count2 = len(dec2) - 1 - dec2.index('.')
    # 在小数位数较少的小数末尾补零，使两个小数具有相同的小数位数，即小数点对齐。
    if dec_place_count1 < dec_place_count2:
        dec1 += '0' * (dec_place_count2 - dec_place_count1)
        dec_place_count = dec_place_count2
    else:
        dec2 += '0' * (dec_place_count1 - dec_place_count2)
        dec_place_count = dec_place_count1

    # 去掉运算数的小数点。调用整数加减法竖式函数进行计算。
    num1 = dec1[:-dec_place_count-1] + dec1[-dec_place_count:]
    num2 = dec2[:-dec_place_count-1] + dec2[-dec_place_count:]
    if operator == '+':
        result = add_vertical(num1, num2)
    else:
        result = sub_vertical(num1, num2)

    # 在与运算数的小数点相同的位置，为计算结果添加小数点。
    if len(result) < dec_place_count + 1:
        result = '0' * (dec_place_count + 1 - len(result)) + result
    result = result[:-dec_place_count] + '.' + result[-dec_place_count:]

    # 删除向加数或减数末尾添加的零（只保留被减数末尾的零），并以相同的空格符代替以保持原长（用于显示
    # 竖式时对齐小数点）。
    if operator == '+':
        dec = remove_trailing_zeros(dec1)
        dec1 = dec + ' ' * (len(dec1) - len(dec))
    dec = remove_trailing_zeros(dec2)
    dec2 = dec + ' ' * (len(dec2) - len(dec))

    # 显示竖式。
    display_vertical(dec1, dec2, result, operator)

    # 去掉计算结果末尾不必要的零，显示化简后的结果。
    result = remove_trailing_zeros(result)
    print(f'\n化简后的结果是: {result}\n')


dec1 = input_decimal('输入第一个小数（或整数）: ')
dec2 = input_decimal('输入第二个小数（或整数）: ')
operator = input('选择做加法还是减法 (+ 或 -)? ')
print()
# 默认做加法。
if operator != '-':
    operator = '+'
# 确保两数中较大的是 dec1，较小的是 dec2。
if float(dec1) < float(dec2):
    dec1, dec2 = dec2, dec1
# input_decimal() 函数内是使用了内置函数 float()。float() 函数的返回值是一个最简小数（去掉末尾不必要的零），
# 但对于一个整数，float() 函数反而会在小数点后保留一个零，以表示这是一个 float 类型的数，例如 float(2) = 2.0。
# 所以如果 dec1/dec2 以 ".0" 结尾，那它一定是一个整数。
if dec1[-2:] == '.0' and dec2[-2:] == '.0':
    num1 = dec1[:-2]
    num2 = dec2[:-2]
    if operator == '+':
        display_vertical(num1, num2, add_vertical(num1, num2), '+')
    else:
        display_vertical(num1, num2, sub_vertical(num1, num2), '-')
else:
    add_sub_decimals(dec1, dec2, operator)
