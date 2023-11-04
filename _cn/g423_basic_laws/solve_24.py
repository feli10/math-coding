"""解 24 点

关于程序的几点说明：
1. 24 点是一个流行的算数游戏，它的基本规则是：一副扑克牌除去 J、Q、K 和大小王，任抽四张牌，使用加、减、乘、除和
   括号把它们连成算式，使结果等于 24。24 点还有很多变体，例如只去掉大小王，把运算数的范围扩大到 13, 或增加更多的
   运算符等。
2. 此程序对于用户输入的任意四个数，显示通过四则运算和添加括号得到 24 的全部独立解式。
3. 程序使用穷举法，对运算数、运算符和运算顺序的全部可能排列，让计算机逐个检验结果是否等于 24。程序在计算算式结果时,
   调用了《有括号的四则混合运算》(G421) 程序中的 calc() 函数。
4. 通过穷举法得到的全部解式中有很多是“等效”的重复解，例如通过交换律和结合律得到的解。为了得到更有意义的“独立”解，
   需要进行“去重”的操作。程序检查等效解式的方法是：如果把两个解式对应的四个运算数换成任意四个数，计算结果仍然相同，
   就认为这两个解式是等效的。
5. 程序在显示解式时，对每步运算的运算符及其前、后运算符可能出现的所有情况进行判断，决定是否需要添加括号。
6. 程序不止可以解 24 点。用户可以输入任意数量的运算数和任意目标运算结果，在有解的情况下，程序会显示出全部独立解式。
   随着运算数的增加，程序很快会变慢，这也是穷举法的特点：虽然在一定范围内解决问题简单方便，但规模受限。  
"""

from itertools import permutations, product
from random import random
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from g421_order_of_operations.eval_expressions import calc


# 显示算式时，为运算符选择指定的符号。
OP_DICT = {'+': '+', '-': '-', '*': '×', '/': '/'}


def is_new(nums, ops, precs):
    """检测由 (nums, ops, precs) 所代表的解式，与其它已确定的解式是否是等效的。测试时，把算式的四个运算数
    分别替换为 test_num_dict 中对应的四个随机数，如果计算结果在 test_results 中已经存在，则说明这个解式与
    之前已确定的某个解式是等效的，返回 False, 否则返回 Ture。
    
    nums: 运算数 list/tuple。
    ops: 运算符 list/tuple。
    precs: 优先级 list/tuple。
    """
    nums = [test_num_dict[x] for x in nums]
    res = calc(nums, ops, precs)
    for test in test_results:
        # 计算机在进行浮点运算时会有误差，所以如果两个数的差足够小，就可以认为这两个数是相等的。
        if abs(res - test) < 1e-6:
            return False
    test_results.append(res)
    return True


def print_solution(nums, ops, precs):
    """显示由 (nums, ops, precs) 所代表的解式。生成算式字符串时，对每步运算的运算符及其前、后运算符可能出现的
    所有情况进行判断，决定是否需要添加括号。
    
    nums: 运算数 list/tuple。
    ops: 运算符 list/tuple。
    precs: 优先级 list/tuple。 
    """
    # 把传过来的三个参数转变或复制为三个新的 list，原参数的值不会受到影响。
    nums = [str(x) for x in nums]  # Convert the elements in nums to string type.
    ops, precs = list(ops), list(precs)

    while len(nums) > 1:
        idx = precs.index(max(precs))
        expr = nums[idx] + ' ' + OP_DICT[ops[idx]] + ' ' + nums[idx + 1]

        # 决定是否需要为这步运算添加括号。
        if len(ops) > 1:  # 最后一步运算不需要括号。
            need_parentheses = True

            is_first_op = (idx == 0)
            is_last_op = (idx == len(ops) - 1)
            r_outer_parent = not (is_first_op or is_last_op) and (precs[idx + 1] > precs[idx - 1])
            l_outer_parent = not (is_first_op or is_last_op) and (precs[idx - 1] > precs[idx + 1])
            if ops[idx] in ['+', '-']:
                if not is_first_op and ops[idx - 1] == '+':
                    if is_last_op or ops[idx + 1] in ['+', '-'] or l_outer_parent:
                        need_parentheses = False
                if not is_last_op and ops[idx + 1] in ['+', '-']:
                    if is_first_op or r_outer_parent:
                        need_parentheses = False
            elif ops[idx] in ['*', '/']:
                if is_first_op or ops[idx - 1] != '/' or r_outer_parent:
                    need_parentheses = False

            if need_parentheses:
                expr = '(' + expr + ')'
        # 在相应 list 中，删除刚刚使用过的运算数、运算符和优先级，用正在生成中的算式字符串取代原运算数的位置。
        nums.pop(idx)
        nums.pop(idx)
        nums.insert(idx, expr)
        ops.pop(idx)
        precs.pop(idx)
    print(nums[0])


def solve(*cards, target=24):
    """解决类似 24 点的问题，对于任意给定的运算数和目标运算结果，显示全部独立解式。

    cards: 包含任意数量运算数的 tuple。
    target: 目标运算结果，默认值是 24。
    """
    n = len(cards)
    for card in cards:
        # 把每张牌上的数对应到一个随机数存入 test_num_dict，用于判断等效解式。1 仍对应到 1，因为 1 引发的很多
        # 等效解式是由 1 本身的特点而不是运算定律导致的，所以检测等效解式时仍要用 1 进行测试。
        if card == 1:
            test_num_dict[card] = 1
        else:
            test_num_dict[card] = random()
    # 获得所有运算数的不重复的排列。
    nums_list = []
    for nums in permutations(sorted(cards, reverse=True)):
        if nums not in nums_list:
            nums_list.append(nums)
    # 获得所有运算符和优先级的排列。
    ops_list = list(product('+-*/', repeat=n-1))
    precs_list = list(permutations(range(n - 1)))
    # 穷举法检查由 (nums, ops, precs) 所代表的每一个算式计算结果是否为 target。
    for nums in nums_list:
        for ops in ops_list:
            for precs in precs_list:
                result = calc(nums, ops, precs)
                # 计算机在进行浮点运算时会有误差，所以如果两个数的差足够小，就可以认为这两个数是相等的。
                if result and abs(result - target) < 0.001 and is_new(nums, ops, precs):
                    print_solution(nums, ops, precs)


test_results = []
test_num_dict = {}

solve(2, 4, 8, 10)
