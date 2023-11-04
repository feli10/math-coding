"""小数乘法竖式

关于程序的几点说明：
1. 小数乘法的计算过程如下：
   1) 先忽略因数的小数点，按照整数乘法算出积；
   2) 看两个因数中一共有几位小数，就从积的个位起数出几位，点上小数点；
   3) 积的小数位数不够时，要在前面用 0 补足，再点小数点；
   4) 结果化简，去掉小数末尾的 0。
2. 程序在实现第一步的整数乘法竖式时，调用了《多位数乘法竖式》(G324) 程序中的 long_multiply_core() 函数
   返回计算结果。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal, remove_trailing_zeros
from g324_long_multiplication1.long_multiplication1 import long_multiply_core


def dec_to_int(dec):
    """获取 dec 的小数位数，并去掉小数点将其变为整数。

    dec: 字符串类型的小数。
    """
    # 如果 dec 以 ".0" 结尾，那它一定是一个整数，例如 2.0。
    if dec[-2:] == '.0':
        dec_place_count = 0
        integer = dec[:-2]
    else:
        dec_place_count = len(dec) - 1 - dec.index('.')
        # 去掉小数点以及最高位上可能余下的 0。
        integer = dec.replace('.', '').lstrip('0')
    return dec_place_count, integer


def multiply_decimals(dec1, dec2):
    """模拟乘法竖式的运算过程求出 dec1 和 dec2 的积 (而不是直接用 dec1 * dec2)，并将结果返回。

    dec1, dec2: 字符串类型的小数。
    """
    # 获取 dec1 和 dec2 的小数位数，并忽略小数点将它们变为整数。
    dec_place_count1, num1 = dec_to_int(dec1)
    dec_place_count2, num2 = dec_to_int(dec2)

    # 模拟乘法竖式计算两个整数的积。
    product, _ = long_multiply_core(num1, num2)

    # 根据两个因数的小数位数，为积添加小数点。
    n = dec_place_count1 + dec_place_count2
    # 如果 dec1 和 dec2 都是整数，不需要添加小数点。
    if n == 0:
        return product
    # 积的小数位数不够时，要在前面用 0 补足。
    product = '0' * (n + 1 - len(product)) + product
    # 为积添加小数点。
    product = product[:-n] + '.' + product[-n:]

    # 返回化简后的结果（去掉小数末尾的 0）。
    return remove_trailing_zeros(product)


dec1 = input_decimal('输入第一个小数（或整数）: ')
dec2 = input_decimal('输入第二个小数（或整数）: ')
product = multiply_decimals(dec1, dec2)
# 如果 dec1/dec2 以 ".0" 结尾，那它一定是一个整数，例如 2.0。
dec1 = dec1[:-2] if dec1[-2:] == '.0' else dec1
dec2 = dec2[:-2] if dec2[-2:] == '.0' else dec2
print(f'{dec1} × {dec2} = {product}')
