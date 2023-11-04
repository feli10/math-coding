"""Add or subtract two fractions"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_fraction
from g524_fractions2.gcd_lcm import get_lcm
from g524_fractions2.decimal_to_fraction import simplify


def add_sub_fractions(fraction1, fraction2, operator):
    """Add or subtract the given fractions according to operator.
    
    fraction1, fraction2: (numerator, denominator) tuples representing fractions.
    operator: "+" or "-".
    """
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2
    # Find the lowest common denominator.
    denominator = get_lcm(denominator1, denominator2)
    numerator1 = numerator1 * (denominator // denominator1)
    numerator2 = numerator2 * (denominator // denominator2)
    if operator == '+':
        numerator = numerator1 + numerator2
    else:
        # Make fraction1 the larger fraction when doing subtraction.
        if numerator1 < numerator2:
            numerator1, numerator2 = numerator2, numerator1
            fraction1, fraction2 = fraction2, fraction1
        numerator = numerator1 - numerator2
    # Simplify and return the result.
    return fraction1, fraction2, simplify(numerator, denominator)


fraction1 = input_fraction('Enter the first fraction: ')
fraction2 = input_fraction('Enter the second fraction: ')
operator = input('Choose between addition and subtraction (+ or -)? ')
# The default operator is "+".
if operator != '-':
    operator = '+'

fraction1, fraction2, result = add_sub_fractions(fraction1, fraction2, operator)

# Display the result.
fraction1 = fraction1[0] if fraction1[1] == 1 else f'{fraction1[0]}/{fraction1[1]}'
fraction2 = fraction2[0] if fraction2[1] == 1 else f'{fraction2[0]}/{fraction2[1]}'
result = result[0] if result[1] == 1 else f'{result[0]}/{result[1]}'
print(f'{fraction1} {operator} {fraction2} = {result}\n')
