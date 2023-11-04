"""Short Multiplication

Some Useful Information:
1. This program multiplies two numbers (one of which is 1-digit) by simulating the process of
   short multiplication and also displays the columns.
2. short_multiply() contains an optional parameter for displaying short multiplication columns. 
   This way, future programs can use the function without displaying the columns.
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def short_multiply(num1, num2, display=False):
    """Multiply num1 and 1-digit num2 by simulating the process of short multiplication 
    instead of evaluating num1 * num2 directly. The function then returns the product.
    The short multiplication columns can be displayed optionally.

    num1: string type natural number (non-negative integer).
    num2: string type 1-digit natural number.
    display: whether or not to display short multiplication columns.
    """
    if num1 == '0' or num2 == '0':
        product = '0'
    else:
        product = ''
        carry = 0
        # Do 1-digit multiplication starting from num1's rightmost digit which is ones.
        for i in range(len(num1) - 1, -1, -1):
            product_i = int(num1[i]) * int(num2) + carry
            carry = product_i // 10
            product_i = product_i % 10
            product = str(product_i) + product
        # Put the last carry in the highest digit of product.
        if carry != 0:
            product = str(carry) + product

    if display:
        # Display the short multiplication columns.
        # Insert spaces between digits to display the columns clearer.
        num1 = ' '.join(list(num1))
        num2 = ' '.join(list(num2))
        product = ' '.join(list(product))
        # The width of the columns is determined by either num1 or product depending on
        # whether product is 0 or not.
        if product == '0':
            width = len(num1) + 2
        else:
            width = len(product) + 2
        # Align each line to the right.
        print(num1.rjust(width))
        print('x' + num2.rjust(width - 1))
        print('-' * width)
        print(product.rjust(width))

    return product


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == '__main__':
    num1 = input_natural_number('Enter the first number: ')
    num2 = input_natural_number('Enter the second number (1-digit): ', digit_count=1)
    short_multiply(num1, num2, display=True)
