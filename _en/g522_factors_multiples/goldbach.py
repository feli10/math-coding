"""Goldbach Guess"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number
from g522_factors_multiples.get_prime_numbers import is_prime_number


def goldbach(n):
    """Find two prime numbers whose sum is n.
    
    n: an even number greater than 2.
    """
    if n == 4:
        return 2, 2
    for i in range(3, n // 2 + 1, 2):
        if is_prime_number(i) and is_prime_number(n - i):
            return i, n - i
    return 'Goldbach Guess is wrong!'


while True:
    num = int(input_natural_number('Enter an even number greater than 2: ', 3))
    if num % 2 == 0:
        break
    print("You didn't enter an even number. Please try again.")

num1, num2 = goldbach(num)
print(f'{num} = {num1} + {num2}')
