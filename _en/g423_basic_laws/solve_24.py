"""Solutions for 24 Game.

Some Useful Information:
1. The 24 Game is played with a deck of playing cards with all the face cards removed. Randomly
   draw 4 cards and the first player that uses all values on the cards, elementary arithmetic
   operations (+, -, *, /), and parentheses to come up with 24 wins. There are also some variants
   of this game such as using J, Q, and K or allowing more operations.
2. Given 4 numbers, the program will display all solutions that are not equivalent to each other.
3. The program uses brute force to try every arithmetic expression and uses the calc() function
   in eval_expressions.py (G421) to calculate the result of the expressions.
4. Many solutions, such as ones using commutative or associative laws, are equivalent. To check
   whether two expressions are equivalent, the 4 given numbers are mapped onto another 4 random
   numbers and the operands in the two expressions are replaced by these new numbers. If the
   results of the two expressions are still the same, they are equivalent.
5. When displaying solutions, parentheses are only used when they are required.
6. The programs can be used to solve problems similar to the 24 Game. In fact, users can enter any
   amount of any numbers and any target number (not necessarily 24) and get all non-equivalent
   solutions.
"""

from itertools import permutations, product
from random import random
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from g421_order_of_operations.eval_expressions import calc


# Use different characters for the operators in the display.
OP_DICT = {'+': '+', '-': '-', '*': '×', '/': '/'}


def is_new(nums, ops, precs):
    """Check whether the solution represented by (nums, ops, precs) is not equivalent to any
    existing solutions by testing another set of operands mapped from nums in test_num_dict for
    the caluculation.
    
    nums: a list/tuple of operands.
    ops: a list/tuple of operators.
    precs: a list/tuple of precedences.
    """
    nums = [test_num_dict[x] for x in nums]
    res = calc(nums, ops, precs)
    for test in test_results:
        # There will be errors in computer calculations. So two numbers are considered equal if
        # their difference is very small.
        if abs(res - test) < 1e-6:
            return False
    test_results.append(res)
    return True


def print_solution(nums, ops, precs):
    """Display the solution which is an arithmetic expression represented by (nums, ops, precs).
    And in the dispaly, use parentheses only when they are required.
    
    nums: a list/tuple of operands.
    ops: a list/tuple of operators.
    precs: a list/tuple of precedences.   
    """
    # Convert or copy the three passed parameters into three new lists. The values of the
    # original parameters will not be affected.
    nums = [str(x) for x in nums]  # Convert the elements in nums to string type.
    ops, precs = list(ops), list(precs)

    while len(nums) > 1:
        idx = precs.index(max(precs))
        expr = nums[idx] + ' ' + OP_DICT[ops[idx]] + ' ' + nums[idx + 1]

        # Determine whether it is necessary to add parentheses on this operation.
        if len(ops) > 1:  # The last operation doesn't need parentheses.
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
        # Remove the used operands, operator, and precedence in their respective lists and
        # replace the removed operands with the cumulative expression string.
        nums.pop(idx)
        nums.pop(idx)
        nums.insert(idx, expr)
        ops.pop(idx)
        precs.pop(idx)
    print(nums[0])


def solve(*cards, target=24):
    """Solve problems similar to the 24 Game. Display all non-equivalent solutions for any
    given cards and target number.

    cards: a tuple of numbers as operands.
    target: a target number, default is 24.
    """
    n = len(cards)
    for card in cards:
        # Each card is mapped onto another random number used for checking equivalent solutions
        # except 1. Because 1 leads to many equivalent solutions that are not due to the laws of
        # operations.
        if card == 1:
            test_num_dict[card] = 1
        else:
            test_num_dict[card] = random()
    # Get all non-repeating permutations of operands.
    nums_list = []
    for nums in permutations(sorted(cards, reverse=True)):
        if nums not in nums_list:
            nums_list.append(nums)
    # Get all possilibities of operators and precedences.
    ops_list = list(product('+-*/', repeat=n-1))
    precs_list = list(permutations(range(n - 1)))
    # Try every arithmetic expression represented by (nums, ops, precs).
    for nums in nums_list:
        for ops in ops_list:
            for precs in precs_list:
                result = calc(nums, ops, precs)
                # There will be errors in computer calculations. So two numbers are considered
                # equal if their difference is very small.
                if result and abs(result - target) < 0.001 and is_new(nums, ops, precs):
                    print_solution(nums, ops, precs)


test_results = []
test_num_dict = {}

solve(2, 4, 8, 10)
