"""四类小数练习题

关于程序的几点说明：
1. 小数练习题共有四种类型，可以一次只练习一种类型，或选择多种类型混合出题。
2. 在分数和小数互相转化的题目中，可能涉及一至三位小数，涉及位数越大的题出现的可能性越低。
3. 单位换算的题目是双向的， 在由较小单位向较大单位换算时，可以输入小数或分数。
4. 在十以内的一位小数加减法题目中，运算数有一定可能是整数，用以练习整数和小数的混合运算。
"""

from random import randint, random
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check, decimal_generator


def fraction_to_decimal():
    """随机生成一道分数转化为小数的练习题。答对返回 True, 答错显示正确答案并返回 False。"""
    # 分母有 50% 可能是 10，30% 可能是 100，20% 可能是 1000。
    rand = random()  # 随机返回一个在 [0.0, 1.0) 范围内的浮点数 (float)。
    if rand < 0.5:
        denominator = 10
    elif rand < 0.8:
        denominator = 100
    else:
        denominator = 1000
    numerator = randint(1, denominator)

    print(f'{numerator}/{denominator}')
    correct_answer = numerator / denominator

    return answer_check(correct_answer, prompt='对应的小数? ')


def decimal_to_fraction():
    """随机生成一道小数转化为分数的练习题。答对返回 True, 答错显示正确答案并返回 False。"""
    # 随机生成小数时，有 50% 可能是一位小数，40% 是两位小数，10% 是三位小数。
    decimal_place_count_dist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3]
    decimal, decimal_place_count = decimal_generator(0, 1, decimal_place_count_dist=
                                                     decimal_place_count_dist)

    print(decimal)
    displayed_answer = f'{int(decimal * 10 ** decimal_place_count)}/{10 ** decimal_place_count}'

    return answer_check(decimal, prompt='对应的分数? ', check_mode='fraction_only',
                        displayed_answer=displayed_answer, is_unique=False)


def add_sub_decimals():
    """随机生成一道十以内一位小数加减法练习题。答对返回 True, 答错显示正确答案并返回 False。"""
    # 运算数有 80% 可能是一位小数，20% 可能是整数（即 0 位小数）。
    decimal_place_count_dist = [0, 1, 1, 1, 1]
    decimal1, _ = decimal_generator(0, 10, decimal_place_count_dist=decimal_place_count_dist)
    decimal2, _ = decimal_generator(0, 10, decimal_place_count_dist=decimal_place_count_dist)

    if random() < 0.5:
        print(f'{decimal1} + {decimal2} =')
        # decimal1 和 decimal2 是 float 类型数据，运算后的结果可能出现一些误差，例如：
        # 1.1 + 2.2 = 3.3000000000000003。所以使用 round() 函数四舍五入。
        correct_answer = round(decimal1 + decimal2, 1)
    else:
        if decimal1 < decimal2:
            decimal1, decimal2 = decimal2, decimal1
        print(f'{decimal1} - {decimal2} =')
        correct_answer = round(decimal1 - decimal2, 1)

    # float 类型仍会以小数形式表示整数，例如 5.0，所以显示正确答案时以 int 类型显示整数结果。
    if int(correct_answer) == correct_answer:
        correct_answer = int(correct_answer)

    return answer_check(correct_answer)


def unit_conversion():
    """随机生成一道单位换算练习题。答对返回 True, 答错显示正确答案并返回 False。

    单位换算的题目是双向的， 在由较小单位向较大单位换算时，可以输入小数或分数。
    """
    LENGTH_UNITS = ['mm', 'cm', 'dm', 'm']
    MONEY_UNITS = ['分', '角', '元']
    AREA_UNITS = ['mm²', 'cm²', 'dm²', 'm²']
    MASS_UNITS = ['g', 'kg', 't']
    TYPES = [LENGTH_UNITS, MONEY_UNITS, AREA_UNITS, MASS_UNITS]
    # FACTORS 中存储的是所有单位类型内部各相邻单位间进行单位换算的进率。
    FACTORS = [10, 10, 100, 1000]

    # 随机选择一种单位类型。
    index = randint(0, len(TYPES) - 1)
    units = TYPES[index]
    factor = FACTORS[index]

    # 选择第一个单位。
    unit1_index = randint(0, len(units) - 1)
    unit1 = units[unit1_index]
    # 选择一个与第一个单位不同的单位。
    unit2_index = unit1_index
    while unit2_index == unit1_index:
        unit2_index = randint(0, len(units) - 1)
        unit2 = units[unit2_index]

    print(f'1{unit1} = __{unit2}')
    correct_answer = factor ** (unit1_index - unit2_index)
    if unit1_index > unit2_index:
        return answer_check(correct_answer)
    # 在由较小单位向较大单位换算时，可以输入小数或分数。
    displayed_answer = f'{correct_answer} 或 1/{factor ** (unit2_index - unit1_index)}'
    return answer_check(correct_answer, check_mode='fraction', displayed_answer=displayed_answer)


# 使用特殊变量 __name__ 确保此程序在作为模块被其它程序引用时，以下代码不会被执行。
if __name__ == '__main__':
    question_generator(fraction_to_decimal, decimal_to_fraction,
                       add_sub_decimals, unit_conversion, count=4)
