"""体积单位换算练习

关于程序的几点说明：
1. 程序在《面积单位换算练习》(G412) 的基础上添加了体积单位；还改用字典 UNIT_DICT 存储所有单位数据，并提供了
   一个列表 PRACTICE_TYPES 方便学习者设置要练习的一种或多种单位类型，列表中默认只有体积单位。
2. 在由较小单位向较大单位换算时，可以输入小数或分数。
3. 当要输入的数位数较多时，可以采用科学计数法。例如 1e3 代表 1 后面有三个 0, 即 1000; 1e-3 代表 1/(1e3),
   即 1/1000 或 0.001。
"""

from random import randint, choice
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


LENGTH_UNITS = ['毫米', '厘米', '分米', '米']
MONEY_UNITS = ['分', '角', '元']
AREA_UNITS = ['平方毫米', '平方厘米', '平方分米', '平方米', '公亩', '公顷', '平方公里']
VOLUME_UNITS = ['立方毫米', '立方厘米', '立方分米', '立方米']
MASS_UNITS = ['克', '千克', '吨']
UNIT_DICT = {'length': (LENGTH_UNITS, 10),
                'money': (MONEY_UNITS, 10),
                'area': (AREA_UNITS, 100),
                'volume': (VOLUME_UNITS, 1000),
                'mass': (MASS_UNITS, 1000)}
# 把要练习的一种或多种单位类型放入下面列表中。
PRACTICE_TYPES = ['volume']


def check_practice_types():
    """检查用户设置的 PRACTICE_TYPES 是否有效。"""
    if not PRACTICE_TYPES:
        raise ValueError('必须至少提供一种单位类型用于练习。')
    for unit_type in PRACTICE_TYPES:
        if unit_type not in UNIT_DICT:
            raise ValueError(f'在 UNIT_DICT 的单位类型中没有 "{unit_type}"。')


def unit_conversion():
    """随机生成一道单位换算练习题。答对返回 True, 答错显示正确答案并返回 False。

    单位换算的题目是双向的， 在由较小单位向较大单位换算时，可以输入小数或分数。
    """
    # 随机选择一种单位类型。
    unit_type = choice(PRACTICE_TYPES)
    units, factor = UNIT_DICT[unit_type]

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


check_practice_types()
question_generator(unit_conversion, count=4)
