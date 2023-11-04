"""面积单位换算练习

关于程序的几点说明：
1. 程序扩充了 decimal_practice.py (G327) 中的 unit_conversion() 函数，向其中添加了三个新的面积单位：
   公亩、公顷和平方千米。
2. 在由较小单位向较大单位换算时，可以输入小数或分数。
3. 当要输入的数位数较多时，可以采用科学计数法。例如 1e3 代表 1 后面有三个 0, 即 1000; 1e-3 代表 1/(1e3),
   即 1/1000 或 0.001。
"""

from random import randint
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check

# 如果想练习所有单位，把 AREA_ONLY 设置为 False。
AREA_ONLY = True


def unit_conversion():
    """随机生成一道单位换算练习题。答对返回 True, 答错显示正确答案并返回 False。

    单位换算的题目是双向的， 在由较小单位向较大单位换算时，可以输入小数或分数。
    """
    LENGTH_UNITS = ['毫米', '厘米', '分米', '米']
    MONEY_UNITS = ['分', '角', '元']
    AREA_UNITS = ['平方毫米', '平方厘米', '平方分米', '平方米', '公亩', '公顷', '平方公里']
    MASS_UNITS = ['克', '千克', '吨']
    TYPES = [LENGTH_UNITS, MONEY_UNITS, AREA_UNITS, MASS_UNITS]
    # FACTORS 中存储的是所有单位类型内部各相邻单位间进行单位换算的进率。
    FACTORS = [10, 10, 100, 1000]

    if AREA_ONLY:
        units = AREA_UNITS
        factor = 100
    else:
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


question_generator(unit_conversion, count=4)
