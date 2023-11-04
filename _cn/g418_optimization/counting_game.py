"""报数游戏

关于程序的几点说明：
1. 报数游戏的规则如下：两人轮流报数，每次在给定范围内选择一个加数累加到公共计数器中，谁报数后使计数器加到约定的数，
   谁就获胜。
2. 程序编写的报数游戏是由玩家对电脑。游戏开始时会随机给出加数的选择范围和和胜利条件，然后由玩家首先开始报数，
   如果玩家输入的数超出了可选择范围，会给出提示并让玩家重新输入。之后电脑和玩家轮流报数，直到一方获胜。
3. 报数游戏是有必胜策略的，以加数范围 1 到 3, 目标 21 为例。要想抢到 21, 就需要抢到 17, 因为无论对方 +1、+2
   还是 +3, 你在下一次都可以加到 21。而想要抢到 17, 就要抢到 13, 以此类推，就必须抢到 9、5 和 1 这些“必胜数”。
   所以只要 0 不是“必胜数”，先报数的玩家就一定能抢到第一个“必胜数”进而赢得比赛。电脑程序也是按照这个策略编写的，
   如果玩家在报数过程中出现失误，电脑就会抢到“必胜数”并取得最终胜利。
"""

from random import randint
from time import sleep
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def count(counter, target, max_count):
    """如果当前计数器不是必胜数，返回一个 1 到 max_count 之间的数，让当前计数器加上这个数后是一个必胜数。
    否则随机返回一个可选择范围内的数。
    
    counter: 当前计数器的累加值。
    target: 目标累加值。
    max_count: 最大可选的加数。
    """
    # 当前计数器是必胜数时，下式中得到的余数应该为 0。
    remainder = (target - counter) % (1 + max_count)
    # 如果余数不为 0, 余数本身就是那个在 1 到 max_count 之间，累加到计数器后可以使计数器成为必胜数的数。
    # 否则随机返回一个可选择范围内的数。
    if remainder != 0:
        return remainder
    return randint(1, max_count)


def start():
    """开始一盘游戏，随机给出加数的选择范围和胜利条件。"""
    max_count = 2#randint(2, 5)
    target = 10#randint(max_count * 5, max_count * 10)
    print(f'每回合在 {list(range(1, max_count + 1))} 中选择一个数累加到公共计数器中。\n'
          + f'谁报数后使计数器加到 {target}，谁就获胜。\n')

    win = False
    current = 0
    while True:
        # 玩家的回合。
        print(f'当前计数器: {current} -> 目标累加值: {target}')
        num = int(input_natural_number('你的选择: ', 1, min(max_count, target - current)))
        print()
        current += num
        if current == target:
            win = True
            break
        # 计算机的回合。
        print(f'当前计数器: {current} -> 目标累加值: {target}')
        # flush=True 用于在 sleep() 前显示字符串。
        print("计算机选择: ", end='', flush=True)
        # 等一小段时间，就好像计算机在思考。
        sleep(0.5)
        num = count(current, target, max_count)
        print(f'{num}\n')
        current += num
        if current == target:
            break
    print(f'当前计数器: {current} = 目标累加值: {target}')
    if win:
        print('你赢了!')
    else:
        print('计算机赢了！')


start()
