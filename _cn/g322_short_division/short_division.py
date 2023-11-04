"""除数是一位数的除法竖式

关于程序的几点说明：
1. 程序会将用户输入的一个多位自然数和一个一位非零自然数用除法竖式求商和余数，并将结果以竖式的形式显示在屏幕上。
2. 程序在求商时真实模拟了除法竖式的运算过程，而不是使用编程语言内置的 "//" 和 "%" 运算符直接得到商和余数。
3. 比较复杂的是除法竖式的显示，关键是确定每一行的起始位置，主要考虑以下两个因素：
   - 除法竖式中包含若干步“小”除法，每一步的余数也是下一步被除数的最高位部分，所以在一步小除法中被除数和余数的数位差，
     就是下一步小除法中被除数的缩进量；
   - 如果前一步小除法的余数是 0, 则下一步被除数的最高位上至少会有一个 0, 在显示竖式时要将开头的 0 去掉，
     但 0 所占的位置要空出来并补充到缩进量中。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def short_divide(dividend, divisor):
    """模拟除法竖式的运算过程求出 dividend 和 divisor 的商和余数 (而不是直接使用 "//" 和 "%"),
    并将结果以除法竖式的形式显示在屏幕上。

    dividend: 字符串类型的自然数。
    divisor: 字符串类型的一位非零自然数。
    """
    # 下面三个 list 用于显示除法竖式。
    step_dividends = []
    products = []
    indents = []

    divisor_int = int(divisor)
    quotient = ''
    step_dividend = ''

    for digit in dividend:
        # 补充被除数的下一位到小除法的被除数中，直到大于除数。
        step_dividend += digit
        step_dividend_int = int(step_dividend)
        if step_dividend_int < divisor_int:
            quotient += '0'
            continue

        # 做一步小除法。
        step_quotient = step_dividend_int // divisor_int
        product = step_quotient * divisor_int
        remainder = step_dividend_int - product

        # 存储显示除法竖式所需的中间数据。
        # step_dividend_fianl 是把 step_dividend 去掉开头的 0（如果有的话）。
        step_dividend_final = str(step_dividend_int)
        step_dividends.append(step_dividend_final)
        # 因为可能去掉了开头的 0，所以需要把去掉的 0 的个数补充到前一步的缩进量中。
        if indents:
            indents[-1] += len(step_dividend) - len(step_dividend_final)
        products.append(str(product))
        # 下一步的缩进量是 step_dividend_final 和 remainder 的数位差。
        indents.append(len(step_dividend_final) - len(str(remainder)))

        quotient += str(step_quotient)
        # 这一步的 remainder 是下一步 step_dividend 的最高位部分。（需要注意的是，
        # 如果 remainder 是 0, 则下一步的 step_dividend 的最高位上至少会有一个 0，
        # 开头的 0 会在下一次循环中被删除。）
        step_dividend = str(remainder)

    # 如果 dividend 小于 divisor，则在以上循环中，一步小除法都没做，所以需要向以下 3 个 list 中手动添加
    # 显示竖式所需的数据。
    if len(step_dividends) == 0:
        step_dividends.append(dividend)
        products.append('0')
        indents.append(0)

    # 删除商和余数最高位上可能出现的一个或多个 0。
    quotient = str(int(quotient))
    remainder = str(int(step_dividend))

    # 如果有余数，因为可能去掉了余数开头的 0，所以需要把去掉的 0 的个数补充到最后一步的缩进量中。
    if remainder != '0':
        indents[-1] += len(step_dividend) - len(remainder)

    # 显示除法竖式。
    fix_indent = len(divisor) + 1  # 用于显示分割线。

    print('\n' + quotient.rjust(fix_indent + len(dividend)))
    print(' ' * fix_indent + '-' * len(dividend))
    print(divisor + '/' + dividend)

    indent = fix_indent
    for i in range(len(step_dividends)):
        if i != 0:
            print(' ' * indent + step_dividends[i])
        # 每一步小除法的被除数和积的右侧对齐。
        print(' ' * indent + products[i].rjust(len(step_dividends[i])))
        print(' ' * fix_indent + '-' * len(dividend))
        indent += indents[i]
    print(' ' * indent + remainder)

    print(f'\n{dividend} / {divisor} = {quotient} ... {remainder}\n')


dividend = input_natural_number('输入一个自然数作为被除数: ')
divisor = input_natural_number('输入一个一位非零自然数作为除数: ',
                               minimum=1, digit_count=1)
short_divide(dividend, divisor)
