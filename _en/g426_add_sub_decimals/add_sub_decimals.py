"""Add or subtract two decimal numbers by simulating the process in vertical columns and
also display the vertical columns.

Some Useful Information:
1. Addition and subtraction of decimals with the decimal points aligned are almost the same as 
   addition and subtraction of integers. So, the program simulate the calculation process of
   decimals based on reorganized elements of add_vertical.py (G314) and sub_vertical.py (G315).
   1) Add zeros to the end of the decimal with fewer decimal places to make both decimals have
      the same number of decimal places - making their decimal points aligned.
   2) Remove decimal points of operands and do integer addion or subtraction (same as in the
      programs of G314/G315).
   3) Add decimal point to the result at the same position as operands' decimal points.
   4) Remove operands' trailing zeros added at step 1, except those of the minuend.
   5) Display the vertical columns (same as in the programs of G314/G315).
   6) Remove trailing zeros of the result and diaplay the simplified result.
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal, remove_trailing_zeros


def add_vertical(num1, num2):
    """Add num1 and num2 by simulating the process in vertical columns instead of
    evaluating num1 + num2 directly, and return the sum.

    num1, num2: two string type natural numbers (non-negative integers).
    """
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

    return the_sum


def sub_vertical(num1, num2):
    """Subtract num2 from num1 by simuating the process with vertical columns instead of
    evaluating num1 - num2 directly, and return the difference.
    
    num1, num2: two string type natural numbers (non-negative integers).
    """
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

    return diff


def display_vertical(num1, num2, result, operator):
    """Display the vertical columns.

    num1, num2: string type non-negative integers of decimals.
    result: string type integer or deciaml that is the sum or difference of num1 and num2.
    operator: "+" or "-".
    """
    # Insert spaces between digits to display the vertical columns clearer.
    num1 = ' '.join(list(num1))
    num2 = ' '.join(list(num2))
    result = ' '.join(list(result))
    # The width of the vertical columns is determined by the number with the most digits.
    width = max(len(num1), len(num2), len(result)) + 2
    # Align each line to the right.
    print(num1.rjust(width))
    print(operator + num2.rjust(width - 1))
    print('-' * width)
    print(result.rjust(width))


def add_sub_decimals(dec1, dec2, operator):
    """Depending on operator, add dec1 and dec2 or subtract dec2 from dec1 by simuating the
    process with vertical columns instead of using built-in operators directly. The function also
    displays the vertical columns.

    dec1, dec2: string type decimals.
    operator: "+" or "-"
    """
    dec_place_count1 = len(dec1) - 1 - dec1.index('.')
    dec_place_count2 = len(dec2) - 1 - dec2.index('.')
    # Add zeros to the end of the decimal with fewer decimal places to make both decimals have
    # the same number of decimal places - making their decimal points aligned.
    if dec_place_count1 < dec_place_count2:
        dec1 += '0' * (dec_place_count2 - dec_place_count1)
        dec_place_count = dec_place_count2
    else:
        dec2 += '0' * (dec_place_count1 - dec_place_count2)
        dec_place_count = dec_place_count1

    # Remove the decimal points of dec1 and dec2.
    num1 = dec1[:-dec_place_count-1] + dec1[-dec_place_count:]
    num2 = dec2[:-dec_place_count-1] + dec2[-dec_place_count:]
    # Do integer addition or subtraction of num1 and num2 in vertical columns by using
    # add_vertical() or sub_vertical().
    if operator == '+':
        result = add_vertical(num1, num2)
    else:
        result = sub_vertical(num1, num2)

    # Add a decimal point to result at the same position as dec1 and dec2's decimal points.
    if len(result) < dec_place_count + 1:
        result = '0' * (dec_place_count + 1 - len(result)) + result
    result = result[:-dec_place_count] + '.' + result[-dec_place_count:]

    # Remove trailing zeros of operands other than the minuend and replace them with the same
    # number of space characters to maintain the original length for later displaying.
    if operator == '+':
        dec = remove_trailing_zeros(dec1)
        dec1 = dec + ' ' * (len(dec1) - len(dec))
    dec = remove_trailing_zeros(dec2)
    dec2 = dec + ' ' * (len(dec2) - len(dec))

    # Display the vertical columns.
    display_vertical(dec1, dec2, result, operator)

    # Remove trailing zeros of result and diaplay the final simplified result.
    result = remove_trailing_zeros(result)
    print(f'\nThe simplified result is: {result}\n')


dec1 = input_decimal('Enter the first decimal: ')
dec2 = input_decimal('Enter the second decimal: ')
operator = input('Choose between addition and subtraction (+ or -)? ')
print()
# The default operator is "+".
if operator != '-':
    operator = '+'
# Make dec1 the larger decimal.
if float(dec1) < float(dec2):
    dec1, dec2 = dec2, dec1
# input_decimal() uses float() inside it. float() will return a simplified decimal with trailing
# zeros removed unless the decimal is actually an integer, in which case it will keep a trailing
# zero (E.g. float(2) = 2.0). So, if dec1/dec2 ends with ".0", it is actually an integer.
if dec1[-2:] == '.0' and dec2[-2:] == '.0':
    num1 = dec1[:-2]
    num2 = dec2[:-2]
    if operator == '+':
        display_vertical(num1, num2, add_vertical(num1, num2), '+')
    else:
        display_vertical(num1, num2, sub_vertical(num1, num2), '-')
else:
    add_sub_decimals(dec1, dec2, operator)
