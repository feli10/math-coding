"""Convert decimals to simplified fractions."""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_decimal
from g524_fractions2.gcd_lcm import get_gcd


def simplify(numerator, denominator):
    """Simplify the given fraction.
    
    numerator/denominator: positive integers.
    """
    gcd = get_gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def decimal_to_fraction(dec):
    """Convert the given decimal to its simplified fraction.
    
    dec: a string type decimal.
    """
    # If dec ends with ".0", it is actually an integer such as 2.0.
    if dec[-2:] == '.0':
        return f'{dec[:-2]}/1'
    dec_point_pos = dec.index('.')
    dec_place_count = len(dec) - dec_point_pos - 1
    numerator = int(dec[:dec_point_pos] + dec[dec_point_pos + 1:])
    denominator = int('1' + '0' * dec_place_count)
    numerator, denominator = simplify(numerator, denominator)
    return f'{numerator}/{denominator}'


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == "__main__":
    dec = input_decimal('Enter a decimal: ')
    print(f'{dec} = {decimal_to_fraction(dec)}')
