"""Add two numbers by simulating the process in vertical columns and
also display the vertical columns.
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def add_vertical(num1, num2):
    """Add num1 and num2 by simulating the process in vertical columns instead of
    evaluating num1 + num2 directly. The function also displays the vertical columns.

    num1, num2: two string type natural numbers (non-negative integers).
    """
    # Make num1 the number with more digits.
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    the_sum = ''
    carry = 0
    # Do addition starting from the rightmost digits which are ones.
    for i in range(-1, -len(num1) - 1, -1):
        sum_i = int(num1[i]) + carry
        if i >= -len(num2):
            sum_i += int(num2[i])
        carry = sum_i // 10
        sum_i = sum_i % 10
        the_sum = str(sum_i) + the_sum
    # Put the last carry in the highest digit of the_sum.
    if carry != 0:
        the_sum = str(carry) + the_sum

    # Display the vertical columns.
    # Insert spaces between digits to display the vertical columns clearer.
    num1 = ' '.join(list(num1))
    num2 = ' '.join(list(num2))
    the_sum = ' '.join(list(the_sum))
    # The width of the vertical columns is determined by the_sum which has the most digits.
    width = len(the_sum) + 2
    # Align each line to the right.
    print(num1.rjust(width))
    print('+' + num2.rjust(width - 1))
    print('-' * width)
    print(the_sum.rjust(width))


num1 = input_natural_number('Enter the first number: ')
num2 = input_natural_number('Enter the second number: ')
add_vertical(num1, num2)
