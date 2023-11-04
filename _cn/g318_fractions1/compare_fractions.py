"""同分子或同分母分数比大小练习"""

from random import randint, sample
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


MAX_DENOMINATOR = 10


def compare_fractions():
    """随机生成一道同分子或同分母分数比大小练习题。答对返回 True, 答错显示正确答案并返回 False。"""
    # 随机选择同分子还是同分母分数比大小。
    if randint(1, 2) == 1:
        # 分子相同，分母越大，分数越小。
        numerator = randint(1, MAX_DENOMINATOR - 2)
        denominator1, denominator2 = sample(range(numerator + 1, MAX_DENOMINATOR + 1), 2)
        print(f'{numerator}/{denominator1} __ {numerator}/{denominator2}')
        if denominator1 > denominator2:
            correct_answer = '<'
        else:
            correct_answer = '>'
    else:
        # 分母相同，分子越大，分数越大。
        denominator = randint(3, MAX_DENOMINATOR)
        numerator1, numerator2 = sample(range(1, denominator), 2)
        print(f'{numerator1}/{denominator} __ {numerator2}/{denominator}')
        if numerator1 > numerator2:
            correct_answer = '>'
        else:
            correct_answer = '<'

    # 输入答案并检查答案是否正确。
    return answer_check(correct_answer, prompt='(> 或 <) ? ', check_mode='same')


question_generator(compare_fractions, count=4)
