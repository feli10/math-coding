"""小数转化为最简分数"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal
from g524_fractions2.gcd_lcm import get_gcd


def simplify(numerator, denominator):
    """化简分数。
    
    numerator/denominator: 正整数，分数的分子和分母。
    """
    gcd = get_gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def decimal_to_fraction(dec):
    """小数转化为最简分数。
    
    dec: 字符串类型的小数。
    """
    # 如果 dec 以 ".0" 结尾，那它一定是一个整数，例如 2.0。
    if dec[-2:] == '.0':
        return f'{dec[:-2]}/1'
    dec_point_pos = dec.index('.')
    dec_place_count = len(dec) - dec_point_pos - 1
    numerator = int(dec[:dec_point_pos] + dec[dec_point_pos + 1:])
    denominator = int('1' + '0' * dec_place_count)
    numerator, denominator = simplify(numerator, denominator)
    return f'{numerator}/{denominator}'


# 使用特殊变量 __name__ 确保此程序在作为模块被其它程序引用时，以下代码不会被执行。
if __name__ == "__main__":
    dec = input_decimal('输入一个小数: ')
    print(f'{dec} = {decimal_to_fraction(dec)}')
