"""小数除法竖式

关于程序的几点说明：
1. 小数除法的计算过程如下：
   1) 先移动除数的小数点，使它变成整数；
   2) 除数的小数点向右移动几位，被除数的小数点也向右移动几位（位数不够的，在被除数的末尾用 0 补足）；
   3) 按除法是整数的小数除法进行计算，商的小数点和被除数的小数点对齐；
   4) 除到被除数的最后一位还没有除尽，添 0 继续除，一直除到余数为 0 (商为有限小数) 或与之前某次的余数相同
     （商为无限循环小数且找到循环节）。
"""

from decimal import Decimal
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal, remove_trailing_zeros


def remove_leading_zeros(num):
    """删除一个数开头的零。
    
    num: 字符串类型的小数或整数。
    """
    if num != '0':
        num = num.lstrip('0')
        if num[0] == '.':
            num = '0' + num
    return num


def divide_decimals(dividend, divisor):
    """模拟除法竖式的运算过程求出 dividend 和 divisor 的商（而不是直接使用 "/"）。如果商是有限小数，
    一直除到余数为 0, 得到商的精确值；如果商是无限循环小数，一直除到找到循环节，并将商以含循环节的方式
    进行表示。之后函数会将商返回。

    dividend, divisor: 字符串类型的小数。
    """
    # 将除数转化成整数。
    if divisor[-2:] == '.0':
        divisor = divisor[:-2]
        if dividend[-2:] == '.0':
            dividend = dividend[:-2]
    else:
        divisor_dec_place_count = len(divisor) - 1 - divisor.index('.')
        divisor = remove_trailing_zeros(str(Decimal(divisor) * 10 ** divisor_dec_place_count))
        dividend = remove_trailing_zeros(str(Decimal(dividend) * 10 ** divisor_dec_place_count))

    # 模拟除法竖式的运算过程，需要时在被除数的末尾补 0，直到得到有限小数或无限循环小数形式的商。

    def is_end(remainder):
        """从被除数补 0 前的最后一步开始，检查终止条件并记录每一步的余数。"""
        nonlocal remainders
        nonlocal quotient
        if i >= dividend_length - 1:
            # 如果余数为 0，除法结束，商为有限小数。
            if remainder == 0:
                return True
            # 如果相同的余数再次出现，除法结束，商为无限循环小数。
            if remainder in remainders:
                # 找到循环节，并为其添加括号。
                repetend_length = len(remainders) - remainders.index(remainder)
                quotient = quotient[:-repetend_length] + '(' + quotient[-repetend_length:] + ')'
                return True
            # 否则，把余数记录下来用于寻找循环节。
            remainders.append(remainder)
        return False

    divisor_int = int(divisor)
    quotient = ''
    step_dividend = ''
    dividend_length = len(dividend)
    remainders = []
    i = 0

    while True:
        if i < dividend_length:
            digit = dividend[i]
            # 商的小数点和被除数的小数点对齐。
            if digit == '.':
                quotient += '.'
                i += 1
                continue
        else:
            # 在被除数首次补 0 前，如果商还没有小数点，为商添加小数点。
            if i == dividend_length and dividend.isdecimal():
                quotient += '.'
            # 在被除数的末尾补 0。
            digit = '0'

        # 补充被除数的下一位到小除法的被除数中，直到大于除数。
        step_dividend += digit
        step_dividend_int = int(step_dividend)
        if step_dividend_int < divisor_int:
            quotient += '0'
            if is_end(step_dividend_int):
                break
            i += 1
            continue

        # 做一步小除法。
        step_quotient = step_dividend_int // divisor_int
        product = step_quotient * divisor_int
        remainder = step_dividend_int - product

        quotient += str(step_quotient)
        # 这一步的 remainder 是下一步 step_dividend 的最高位部分。
        step_dividend = str(remainder)

        if is_end(remainder):
            break
        i += 1

    return remove_leading_zeros(quotient)


dividend = input_decimal('输入被除数（小数或整数）: ')
divisor = input_decimal('输入除数（非零小数或整数）: ', minimum_inclusive=False)
print(f'商: {divide_decimals(dividend, divisor)}')
