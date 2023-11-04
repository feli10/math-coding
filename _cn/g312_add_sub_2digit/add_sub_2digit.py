"""两位数加减法练习"""

from random import randint
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


def add_sub_2digit():
    """随机生成一道两位数加减法练习题。答对返回 True, 答错显示正确答案并返回 False。"""
    # 随机生成两个两位数。
    num1 = randint(10, 99)
    num2 = randint(10, 99)

    # 随机选择加法或减法，机会各半。
    if randint(0, 1) == 0:
        print(f'{num1} + {num2} =')
        correct_answer = num1 + num2
    else:
        # 做减法时，确保被减数大于等于减数。
        if num1 < num2:
            num1, num2 = num2, num1
        print(f'{num1} - {num2} =')
        correct_answer = num1 - num2

    # 输入答案并检查答案是否正确。
    return answer_check(correct_answer)


question_generator(add_sub_2digit, count=4)
