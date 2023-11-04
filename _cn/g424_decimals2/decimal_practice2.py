"""三类小数练习题

关于程序的几点说明：
1. 小数练习题共有三种类型，其中一种是引用自《四类小数练习题》(G327) 中的双向单位换算。可以一次只练习一种类型，
   或选择多种类型混合出题。
2. Python 中默认表示小数的数据类型是 float (浮点数), float 运算效率很高，但常存在一定误差，例如 1.1 + 2.2
   = 3.3000000000000003。Python 标准库的 decimal 模块里有一种专门用于表示小数的数据类型 Decimal, 虽然
   运算效率不如 float, 但可以得到小数运算的精确结果。程序中求小数的近似数和计算小数点移位的正确答案时，都使用
   了 Decimal 数据类型。
"""

from random import randint, random
from decimal import Decimal, getcontext, ROUND_HALF_UP
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check, decimal_generator
from g327_decimals1.decimal_practice1 import unit_conversion


def round_decimal():
    """随机生成一道求小数近似数的练习题。答对返回 True, 答错显示正确答案并返回 False。"""
    MIN_DEC = 0
    MAX_DEC = 100
    # 随机生成的小数具有 1-4 位小数的可能性相同。
    DEC_PLACE_COUNT_DIST = [1, 2, 3, 4, 5]
    PHRASES = [('保留整数', '精确到个位'),
               ('保留一位小数', '精确到十分位'),
               ('保留两位小数', '精确到百分位'),
               ('保留三位小数', '精确到千分位'),
               ('保留四位小数', '精确到万分位')]
    # 设置 round() 的模式为：任何情况下遇到 5 都向上入。(默认值是 ROUND_HALF_EVEN，在这种该模式下，
    # 1.5 和 2.5 的近似值都是 2，因为 2 是离它们最近的偶数。)
    getcontext().rounding = ROUND_HALF_UP
    dec, dec_place_count = decimal_generator(MIN_DEC, MAX_DEC,
                                             decimal_place_count_dist=DEC_PLACE_COUNT_DIST)
    new_dec_place_count = randint(0, dec_place_count - 1)
    print(f'{dec} {PHRASES[new_dec_place_count][randint(0, 1)]}')
    correct_answer = str(round(Decimal(str(dec)), new_dec_place_count))

    return answer_check(correct_answer, check_mode='same')


def move_decimal_point():
    """随机生成一道小数乘以或除以 10, 100 或 1000 的计算题，通过求积或商练习小数点移位。答对返回 True,
    答错显示正确答案并返回 False。
    """
    MIN_DEC = 0
    MAX_DEC = 100
    # 随机生成的小数具有 0-3 位小数的可能性相同（0 位小数就是整数）。
    DEC_PLACE_COUNT_DIST = [0, 1, 2, 3]
    MAX_MOVE_COUNT = 3

    dec, _ = decimal_generator(MIN_DEC, MAX_DEC, decimal_place_count_dist=DEC_PLACE_COUNT_DIST)
    factor = 10 ** randint(1, MAX_MOVE_COUNT)
    if random() < 0.5:
        print(f'{dec} * {factor} =')
        correct_answer = Decimal(str(dec)) * factor
    else:
        print(f'{dec} / {factor} =')
        correct_answer = Decimal(str(dec)) / factor

    if int(correct_answer) == correct_answer:
        correct_answer = int(correct_answer)
    else:
        correct_answer = float(correct_answer)
    return answer_check(correct_answer)


question_generator(round_decimal, move_decimal_point, unit_conversion, count=4)
