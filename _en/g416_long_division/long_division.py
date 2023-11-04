"""Long Division

Some Useful Information:
1. This program simulates the process of long division and also displays the columns.
2. The basic operations of short division and long division are the same. Therefore,
   short_division.py (G322) can also be used for long division when the restriction of
   divisor's number of digits is removed. Based on short_division.py, this program adds
   an additional step to cancel the dividend and divisor's common trailing zeros. The newly
   added code is marked between two lines.
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def long_divide(dividend, divisor):
    """Divide dividend by divisor by simulating the process of long division 
    instead of using "//" and "%" to get quotient and remainder directly. The program
    also displays the long division columns.

    dividend: string type natural number (non-negative integer).
    divisor: string type non-zero natrual number (positive integer).
    """
    # ----------------------------------------------------------------
    # Cancel the common trailing zeros of dividend and divisor.
    if dividend != '0':
        canceled_zero_count = min(len(dividend) - len(dividend.rstrip('0')),
                                  len(divisor) - len(divisor.rstrip('0')))
        if canceled_zero_count != 0:
            dividend = dividend[:-canceled_zero_count]
            divisor = divisor[:-canceled_zero_count]
    # ----------------------------------------------------------------

    # The following 3 lists are used for displaying the columns.
    step_dividends = []
    products = []
    indents = []

    divisor_int = int(divisor)
    quotient = ''
    step_dividend = ''

    for digit in dividend:
        # Accumulate digits on step_dividend until it is greater than divisor.
        step_dividend += digit
        step_dividend_int = int(step_dividend)
        if step_dividend_int < divisor_int:
            quotient += '0'
            continue

        # Do one step of division.
        step_quotient = step_dividend_int // divisor_int
        product = step_quotient * divisor_int
        remainder = step_dividend_int - product

        # Save intermediate data for later displaying the columns.
        # step_dividend_final is step_dividend with leading zeros removed.
        step_dividend_final = str(step_dividend_int)
        step_dividends.append(step_dividend_final)
        # Adjust last indent since one or more leading zeros of step_dividend might
        # have been removed.
        if indents:
            indents[-1] += len(step_dividend) - len(step_dividend_final)
        products.append(str(product))
        # The indent is the difference in digits between step_dividend_final and remainder.
        indents.append(len(step_dividend_final) - len(str(remainder)))

        quotient += str(step_quotient)
        # step_dividend of the next step starts with remainder of this step.
        # Therefore, if the remainder is zero, the next step's step_dividend will start with
        # at least one zero, which will be removed in the next loop.
        step_dividend = str(remainder)

    # In case dividend is less than divisor and no division is done in the for loop above.
    if len(step_dividends) == 0:
        step_dividends.append(dividend)
        products.append('0')
        indents.append(0)

    # Remove leading zeros of quotient and remainder if any exist.
    quotient = str(int(quotient))
    remainder = str(int(step_dividend))

    # Adjust the final indent when there is a non-zero remainder that might have leading zeros.
    if remainder != '0':
        indents[-1] += len(step_dividend) - len(remainder)

    # Display the long division columns.
    fix_indent = len(divisor) + 1  # Used to display dividing lines.

    print('\n' + quotient.rjust(fix_indent + len(dividend)))
    print(' ' * fix_indent + '-' * len(dividend))
    print(divisor + '/' + dividend)

    indent = fix_indent
    for i in range(len(step_dividends)):
        if i != 0:
            print(' ' * indent + step_dividends[i])
        # step_dividend and product are aligned to the right.
        print(' ' * indent + products[i].rjust(len(step_dividends[i])))
        print(' ' * fix_indent + '-' * len(dividend))
        indent += indents[i]
    print(' ' * indent + remainder)

    # ----------------------------------------------------------------
    # Put the canceled zeros back.
    if dividend != '0':
        dividend += '0' * canceled_zero_count
        divisor += '0' * canceled_zero_count
        # Add the canceled zeros to the end of remainder.
        if remainder != '0':
            remainder += '0' * canceled_zero_count
    # ----------------------------------------------------------------

    print(f'\n{dividend} / {divisor} = {quotient} ... {remainder}\n')


dividend = input_natural_number('Enter a natrual number as the dividend: ')
divisor = input_natural_number('Enter a non-zero natrual number as the divisor: ', minimum=1)
long_divide(dividend, divisor)
