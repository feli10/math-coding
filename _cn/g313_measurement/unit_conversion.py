"""单位换算练习

关于程序的几点说明：
1. 程序包含长度单位 (mm, cm, dm, m) 和质量单位 (g, kg, t)。
2. 由于尚未学习分数和小数，题目全部是由较大单位向较小单位进行换算，
   例如 1dm = __cm, 而不会出现 1cm = __dm。
"""

from random import randint
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


def unit_conversion():
    """随机生成一道单位换算练习题。答对返回 True, 答错显示正确答案并返回 False。

    题目包含长度和质量单位换算。
    题目全部是由较大单位向较小单位进行换算。
    """
    LENGTH_UNITS = ['mm', 'cm', 'dm', 'm']
    MASS_UNITS = ['g', 'kg', 't']
    TYPES = [LENGTH_UNITS, MASS_UNITS]
    # FACTORS 中存储的是所有单位类型内部各相邻单位间进行单位换算的进率。
    FACTORS = [10, 1000]

    # 随机选择一种单位类型。
    index = randint(0, len(TYPES) - 1)
    units = TYPES[index]
    factor = FACTORS[index]

    # 从这种单位类型中随机选择两个单位，并确保 unit2 是比 unit1 更小的单位。
    unit1_index = randint(1, len(units) - 1)
    unit1 = units[unit1_index]
    unit2_index = randint(0, unit1_index - 1)
    unit2 = units[unit2_index]
    print(f'1{unit1} = __{unit2}')
    correct_answer = factor ** (unit1_index - unit2_index)

    # 输入答案并检查答案是否正确。
    return answer_check(correct_answer)


question_generator(unit_conversion, count=4)
