"""分数加减法"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_fraction
from g524_fractions2.gcd_lcm import get_lcm
from g524_fractions2.decimal_to_fraction import simplify


def add_sub_fractions(fraction1, fraction2, operator):
    """根据 operator 的符号，对给定分数做加法或减法。
    
    fraction1, fraction2: 由 (分子, 分母) 构成的 tuple 数对。
    operator: "+" 或 "-".
    """
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2
    # 通分。
    denominator = get_lcm(denominator1, denominator2)
    numerator1 = numerator1 * (denominator // denominator1)
    numerator2 = numerator2 * (denominator // denominator2)
    if operator == '+':
        numerator = numerator1 + numerator2
    else:
        # 做减法时，确保两数中较大的是 fraction1。
        if numerator1 < numerator2:
            numerator1, numerator2 = numerator2, numerator1
            fraction1, fraction2 = fraction2, fraction1
        numerator = numerator1 - numerator2
    # 将结果约分为最简分数并返回。
    return fraction1, fraction2, simplify(numerator, denominator)


fraction1 = input_fraction('输入第一个分数（或整数）: ')
fraction2 = input_fraction('输入第二个分数（或整数）: ')
operator = input('选择做加法还是减法 (+ 或 -)? ')
# 默认做加法。
if operator != '-':
    operator = '+'

fraction1, fraction2, result = add_sub_fractions(fraction1, fraction2, operator)

# 显示结果。
fraction1 = fraction1[0] if fraction1[1] == 1 else f'{fraction1[0]}/{fraction1[1]}'
fraction2 = fraction2[0] if fraction2[1] == 1 else f'{fraction2[0]}/{fraction2[1]}'
result = result[0] if result[1] == 1 else f'{result[0]}/{result[1]}'
print(f'{fraction1} {operator} {fraction2} = {result}\n')
