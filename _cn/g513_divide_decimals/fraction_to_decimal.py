"""常见分数转化为小数练习"""

from random import randint
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


def fraction_to_decimal():
    """随机生成一道分数转化为小数练习题，分数为分母在十以内的常见分数。
    答对返回 True, 答错显示正确答案并返回 False。
    """
    denominator = randint(2, 10)
    numerator = randint(1, denominator - 1)

    print(f"{numerator}/{denominator}")
    correct_answer = round(numerator / denominator, 3)

    return answer_check(correct_answer, prompt='对应的小数? ')

print('分数转化为小数。\n'
      + '(无限小数精确到千分位)\n')
question_generator(fraction_to_decimal, count=4)
