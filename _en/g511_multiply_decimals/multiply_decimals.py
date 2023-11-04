"""Multiply two decimals based on long multiplication of integers.

Some Useful Information:
1. The calculation process of decimal multiplication is as follows:
   1) Ignore decimal points of two factors, and calculate product of corresponding integers by
      long multiplication.
   2) Add a decimal point to the product according to factors' number of decimal places.
   3) If product doesn't have enough digits for decimal places, add leading zeros to product.
   4) Remove trailing zeros of product if any exist.
2. The program uses the long_multiply_core() function from long_multiplication1.py (G324) to
   calculate product of two integers in step 1.
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal, remove_trailing_zeros
from g324_long_multiplication1.long_multiplication1 import long_multiply_core


def dec_to_int(dec):
    """Get dec's number of decimal places and convert it to an integer by removing decimal point.
    
    dec: a string type decimal.
    """
    # If dec ends with ".0", it is actually an integer such as 2.0.
    if dec[-2:] == '.0':
        dec_place_count = 0
        integer = dec[:-2]
    else:
        dec_place_count = len(dec) - 1 - dec.index('.')
        # Remove decimal point and any leading zeros.
        integer = dec.replace('.', '').lstrip('0')
    return dec_place_count, integer


def multiply_decimals(dec1, dec2):
    """Multiply dec1 and dec2 by simulating the process of long multiplication instead of
    evaluating dec1 * dec2 directly. The function then returns the product.

    dec1, dec2: string type decimals.
    """
    # Get dec1 and dec2's number of decimal places and convert them to integers.
    dec_place_count1, num1 = dec_to_int(dec1)
    dec_place_count2, num2 = dec_to_int(dec2)

    # Multiply num1 and num2 by simulating the process of long multiplication.
    product, _ = long_multiply_core(num1, num2)

    # Add a decimal point to product according to dec1 and dec2'a number of decimal places.
    n = dec_place_count1 + dec_place_count2
    # Don't need to add a decimal point if dec1 and dec2 are both integers.
    if n == 0:
        return product
    # If product doesn't have enough digits for decimal places, add leading zeros to product.
    product = '0' * (n + 1 - len(product)) + product
    # Add a decimal point to product.
    product = product[:-n] + '.' + product[-n:]

    # Simplify and return product.
    return remove_trailing_zeros(product)


dec1 = input_decimal('Enter the first decimal: ')
dec2 = input_decimal('Enter the second decimal: ')
product = multiply_decimals(dec1, dec2)
# If dec ends with ".0", it is actually an integer such as 2.0.
dec1 = dec1[:-2] if dec1[-2:] == '.0' else dec1
dec2 = dec2[:-2] if dec2[-2:] == '.0' else dec2
print(f'{dec1} × {dec2} = {product}')
