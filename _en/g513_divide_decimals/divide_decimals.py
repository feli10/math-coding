"""Decimal division based on long division process.

Some Useful Information:
1. The calculation process of decimal division is as follows:
   1) Convert the divisor to an integer and adjust the decimal point position of the
      dividend accordingly.
   2) Do long division with the quotient's decimal point aligned with the dividend's.
   3) The long division process won't end until the quotient of a terminating decimal or
      a repeating decimal with repetend is obtained. Zeros will be added to the end of the
      dividend if nessecary.
2. Repetend is the infinitely repeated digit sequence in a repeating decimal.
"""

from decimal import Decimal
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal, remove_trailing_zeros


def remove_leading_zeros(num):
    """Remove leading zeros of a number.
    
    num: a string type decimal or integer.
    """
    if num != '0':
        num = num.lstrip('0')
        if num[0] == '.':
            num = '0' + num
    return num


def divide_decimals(dividend, divisor):
    """Divide dividend by divisor by simulating the process of long division instead of evaluating
    dividend / divisor directly. The process won't end until the quotient of a terminating decimal
    or a repeating decimal with repetend is obtained. The function then returns the quotient.

    dividend, divisor: string type decimals.
    """
    # Convert divisor to an integer.
    if divisor[-2:] == '.0':
        divisor = divisor[:-2]
        if dividend[-2:] == '.0':
            dividend = dividend[:-2]
    else:
        divisor_dec_place_count = len(divisor) - 1 - divisor.index('.')
        divisor = remove_trailing_zeros(str(Decimal(divisor) * 10 ** divisor_dec_place_count))
        dividend = remove_trailing_zeros(str(Decimal(dividend) * 10 ** divisor_dec_place_count))

    # Simulate the process of long division until the quotient of a terminating decimal or
    # a repeating decimal with repetend is obtained. Zeros will be added to the end of the
    # dividend if nessecary.

    def is_end(remainder):
        """Check termination conditions and record remainder starting from the last step of
        division before adding zeors to dividend.
        """
        nonlocal remainders
        nonlocal quotient
        if i >= dividend_length - 1:
            # End the division if remainder is zero. The quotient is a terminating decimal.
            if remainder == 0:
                return True
            # End the division if the same remainder appears again in remainders. The quotient is
            # a repeating decimal.
            if remainder in remainders:
                # Find the repetend in quotient and add parentheses to it.
                repetend_length = len(remainders) - remainders.index(remainder)
                quotient = quotient[:-repetend_length] + '(' + quotient[-repetend_length:] + ')'
                return True
            # Otherwise, record remainder for finding the repetend of repeating decimals.
            remainders.append(remainder)
        return False

    divisor_int = int(divisor)
    quotient = ''
    step_dividend = ''
    dividend_length = len(dividend)
    remainders = []
    i = 0

    while True:
        if i < dividend_length:
            digit = dividend[i]
            # Align the decimal point of quotient with dividend.
            if digit == '.':
                quotient += '.'
                i += 1
                continue
        else:
            # If quotient doesn't have a decimal point, add it.
            # This will happen just before the step that the first zero is added to dividend.
            if i == dividend_length and dividend.isdecimal():
                quotient += '.'
            # Add a zero to dividend.
            digit = '0'

        # Accumulate digits on step_dividend until it is greater than divisor.
        step_dividend += digit
        step_dividend_int = int(step_dividend)
        if step_dividend_int < divisor_int:
            quotient += '0'
            if is_end(step_dividend_int):
                break
            i += 1
            continue

        # Do one step of division.
        step_quotient = step_dividend_int // divisor_int
        product = step_quotient * divisor_int
        remainder = step_dividend_int - product

        quotient += str(step_quotient)
        # step_dividend of the next step starts with remainder of this step.
        step_dividend = str(remainder)

        if is_end(remainder):
            break
        i += 1

    return remove_leading_zeros(quotient)


dividend = input_decimal('Enter the dividend: ')
divisor = input_decimal('Enter the non-zero divisor: ', minimum_inclusive=False)
print(f'The quotient is: {divide_decimals(dividend, divisor)}')
