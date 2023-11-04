"""Sum of Two Dice"""

from random import choices
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from g514_probability.random_with_weights import chart


TIMES = 36000
DICE = [1, 2, 3, 4, 5, 6]


result = {}
for _ in range(TIMES):
    sum_of_two_dice = sum(choices(DICE, k=2))
    result[sum_of_two_dice] = result.get(sum_of_two_dice, 0) + 1

chart(result, title='Sum of Two Dice', xlabel='Numbers')
