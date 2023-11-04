"""Long Multiplication 2

Some Useful Information:
1. This program multiplies two numbers by simulating the process of long multiplication
   and also displays the columns.
2. The program is an upgrade of long_multiplication1.py (G324) with special handling of
   trailing zeros of the two numbers. Since the core operations of long multiplication are
   the same, long_multiply_core() is reused to multiply the main parts of the two
   numbers after separating their trailing zeros.
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number
from g324_long_multiplication1.long_multiplication1 import long_multiply_core, expand


def separate_trailing_zeros(num):
    """Return the main part of num with its trailing zeros removed, along with the number of
    removed trailing zeros.
    
    num: a string type natural number (non-negative integer).
    """
    if num == '0':
        num_main = '0'
        num_trailing_zero_count = 0
    else:
        num_main = num.rstrip('0')
        num_trailing_zero_count = len(num) - len(num_main)
    return num_main, num_trailing_zero_count


def long_multiply(num1, num2):
    """Multiply num1 and num2 by simulating the process of long multiplication with
    special handling of the two numbers' trailing zeros. The function also displays the
    long multiplication columns.

    num1, num2: two string type natural numbers (non-negative integers).
    """
    # Separate the two numbers' trailing zeros if any exist.
    num1_main, num1_trailing_zero_count = separate_trailing_zeros(num1)
    num2_main, num2_trailing_zero_count = separate_trailing_zeros(num2)

    # Make num1_main the number with more digits.
    if len(num1_main) < len(num2_main):
        num1_main, num2_main = num2_main, num1_main
        num1_trailing_zero_count, num2_trailing_zero_count \
            = num2_trailing_zero_count, num1_trailing_zero_count

    if num2_main == '0':
        product = '0'
    else:
        # Multiply num1_main and num2_main by simulating the process of long multiplication.
        product_main, short_products = long_multiply_core(num1_main, num2_main)
        # Add removed trailing zeros from the two numbers to the end of product_main.
        product = product_main + '0' * (num1_trailing_zero_count + num2_trailing_zero_count)

    # Display the long multiplication columns.
    # The width of the columns is determined by either num1 or product depending on
    # whether product is 0 or not.
    if product == '0':
        # Insert spaces between digits to display the vertical columns clearer.
        num1 = expand(num1)
        width = len(num1) + 2
        print(num1.rjust(width))
        print('x' + num2.rjust(width - 1))
        print('-' * width)
        print(product.rjust(width))
    else:
        # Insert spaces between digits to display the vertical columns clearer.
        num1_main = expand(num1_main)
        num2_main = expand(num2_main)
        product_main = expand(product_main)
        product = expand(product)
        width_main = len(product_main) + 2
        width = len(product) + 2
        # num1_main and num2_main are aligned to the right with zeros after them if any exist.
        print(num1_main.rjust(width_main) + ' 0' * num1_trailing_zero_count)
        print('x' + num2_main.rjust(width_main - 1) + ' 0' * num2_trailing_zero_count)
        print('-' * width)
        if len(num2_main) != 1:
            for i, short_product in enumerate(short_products):
                if short_product != '0':
                    print(expand(short_product).rjust(width_main - i * 2))
            print('-' * width)
        print(product.rjust(width))


num1 = input_natural_number('Enter the first number: ')
num2 = input_natural_number('Enter the second number: ')
long_multiply(num1, num2)
