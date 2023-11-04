"""Long Multiplication 1

Some Useful Information:
1. This program multiplies two numbers by simulating the process of long multiplication
   and also displays the columns.
2. The porcess of long multiplication includes two main steps. The first step is to calculate
   some short mulitiplication, and the second step is to add up the products obtained from the
   first step. The program uses the short_multiply() function from short_multiplication.py (G316)
   for the first step.
3. long_multipy_core(), which simulates the process of long multiplication, is separated from
   long_multiply(), which mainly displays long multiplication columns, so that long_multipy_core() 
   can be reused in Long Multiplication 2, which is the final program of this multiplication series. 
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number
from g316_short_multiplication.short_multiplication import short_multiply


def add_multiple(nums):
    """Add multiple numbers by simulating the process in vertical columns.
    
    nums: a list of string type natural numbers (non-negative integers).
    """
    # Add leading zeros to all numbers to make them have as many digits as
    # the number with the most digits.
    max_digit_count = max(len(num) for num in nums)
    for i, num in enumerate(nums):
        nums[i] = '0' * (max_digit_count - len(num)) + num

    the_sum = ''
    carry = 0
    # Do addition starting from the rightmost digits which are ones.
    for i in range(max_digit_count - 1, -1, -1):
        sum_i = sum(int(num[i]) for num in nums) + carry
        carry = sum_i // 10
        sum_i = sum_i % 10
        the_sum = str(sum_i) + the_sum
    # Put the last carry in the highest digit of the_sum.
    if carry != 0:
        the_sum = str(carry) + the_sum
    return the_sum


def long_multiply_core(num1, num2):
    """Multiply num1 and num2 by simulating the process of long multiplication instead of
    evaluating num1 * num2 directly. The function returns the product of num1 and num2 and
    a short multiplication product list used to display the long multiplication columns.

    num1, num2: two string type natural numbers (non-negative integers).
    """
    # Use short_multiply() to get all products of num1 with each digit of num2.
    # The products will be stored in short_products which will be returned for
    # displaying long multiplication columns.
    short_products = []
    short_products_revised = []
    for i in range(len(num2) - 1, -1, -1):
        short_product = short_multiply(num1, num2[i])
        short_products.append(short_product)
        # According to the place of num2's multiplied digit, add corresponding trailing zeros
        # to short_product to revise the product to its actual value which will be used later
        # for addition.
        short_products_revised.append(short_product + '0' * (len(num2) - 1 - i))

    # Get the product of num1 and num2 by summing all short multiplication products.
    product = add_multiple(short_products_revised)
    return product, short_products


def expand(string, char=' '):
    """Insert char between each character of string."""
    return char.join(list(string))


def long_multiply(num1, num2):
    """Multiply num1 and num2 by simulating the process of long multiplication.
    The function also displays the long multiplication columns.

    num1, num2: two string type natural numbers (non-negative integers).
    """
    # Make num1 the number with more digits.
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    product, short_products = long_multiply_core(num1, num2)

    # Display the long multiplication columns.
    # Insert spaces between digits to display the vertical columns clearer.
    num1 = expand(num1)
    num2 = expand(num2)
    product = expand(product)
    # The width of the columns is determined by either num1 or product depending on
    # whether product is 0 or not.
    if product == '0':
        width = len(num1) + 2
    else:
        width = len(product) + 2

    print(num1.rjust(width))
    print('x' + num2.rjust(width - 1))
    print('-' * width)
    if len(num2) != 1:
        for i, short_product in enumerate(short_products):
            if short_product != '0':
                print(expand(short_product).rjust(width - i * 2))
        print('-' * width)
    print(product.rjust(width))


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == '__main__':
    num1 = input_natural_number('Enter the first number: ')
    num2 = input_natural_number('Enter the second number: ')
    long_multiply(num1, num2)
