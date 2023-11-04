"""Subtract two numbers by simulating the process in vertical columns and
also display the vertical columns.
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def sub_vertical(num1, num2):
    """Subtract num2 from num1 by simuating the process with vertical columns instead of
    evaluating num1 - num2 directly. The function also displays the vertical columns.
    
    num1, num2: two string type natural numbers (non-negative integers).
    """
    # Make num1 the larger number.
    if int(num1) < int(num2):
        num1, num2 = num2, num1

    diff = ''
    carry = 0
    # Do subtraction starting from the rightmost digits which are ones.
    for i in range(-1, -len(num1) - 1, -1):
        diff_i = int(num1[i]) - carry
        if i >= -len(num2):
            diff_i -= int(num2[i])
        if diff_i < 0:
            carry = 1
            diff_i += 10
        else:
            carry = 0
        diff = str(diff_i) + diff
    # Remove leading zeros if any exist.
    diff = str(int(diff))

    # Display the vertical columns.
    # Insert spaces between digits to display the vertical columns clearer.
    num1 = ' '.join(list(num1))
    num2 = ' '.join(list(num2))
    diff = ' '.join(list(diff))
    # The width of the vertical columns is determined by num1 which has the most digits.
    width = len(num1) + 2
    # Align each line to the right.
    print(num1.rjust(width))
    print('-' + num2.rjust(width - 1))
    print('-' * width)
    print(diff.rjust(width))


num1 = input_natural_number('Enter the first number: ')
num2 = input_natural_number('Enter the second number: ')
sub_vertical(num1, num2)
