"""与“倍”有关的文字题

关于程序的几点说明：
1. 题目包含三种简单类型，各举例如下：
   - 4 的 3 倍是几?
   - 12 是 4 的几倍?
   - 一个数的 3 倍是 12, 这个数是几?
"""

from random import randint
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


def word_problem_times():
    """随机生成一道与“倍”有关的文字题（包含三种题型）。答对返回 True, 答错显示正确答案并返回 False。"""
    # 随机生成题目中的数。
    num1 = randint(1, 9)
    times = randint(1, 9)
    num2 = num1 * times

    # 随机选择三种题型中的一种。
    wp_type = randint(1, 3)
    if wp_type == 1:
        print(f'{num1} 的 {times} 倍是几?')
        correct_answer = num2
    elif wp_type == 2:
        print(f'{num2} 是 {num1} 的几倍?')
        correct_answer = times
    else:
        print(f'一个数的 {times} 倍是 {num2}, 这个数是几?')
        correct_answer = num1

    # 输入答案并检查答案是否正确。
    return answer_check(correct_answer)


question_generator(word_problem_times, count=4)
