"""两个骰子的点数和"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from random import choices
from g514_probability.random_with_weights import chart


TIMES = 36000
DICE = [1, 2, 3, 4, 5, 6]


result = {}
for _ in range(TIMES):
    sum_of_two_dice = sum(choices(DICE, k=2))
    result[sum_of_two_dice] = result.get(sum_of_two_dice, 0) + 1

chart(result, title='两个骰子的点数和', xlabel='点数')
