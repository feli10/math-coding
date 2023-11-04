"""Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

Some Useful Information:
1. There are 3 functions in the program:
   1) get_gcd_slow(): Get GCD by definition. Even though the number of loops has been optimized
      similar to get_factors() in get_prime_numbers.py (G522), it is still slow.
   2) get_gcd(): Get GCD by Euclidean Algorithm - The GCD of two numbers does not change if the
      larger number is replaced by its remainder when divided by the smaller number. It is
      much faster.
   3) get_lcm(): Get LCM based on get_gcd().
"""

import math
from time import time


def get_gcd_slow(a, b):
    """Get greatest common divisor of two numbers by definition.
    
    a, b: positive integers.    
    """
    # Make b the smaller number.
    if a < b:
        a, b = b, a
    # If i is a factor of b, then b/i is also a factor of b. So, we don't need to find factors
    # from 1 all the way to b. Instead, we just need to find factors from 1 to sqrt(b).
    for i in range(1, int(math.sqrt(b)) + 1):
        if b % i == 0:
            # The first (b // i) that meets the condition is the gcd of a and b.
            if a % (b // i) == 0:
                return b // i
            # i is the current gcd and not the final gcd until the end of the loop.
            if a % i == 0:
                gcd = i
    return gcd


def get_gcd(a, b):
    """Get greatest common divisor of two numbers by Euclidean Algorithm.
    
    a, b: positive integers.
    """
    # The greatest common divisor of two numbers does not change if the larger number is
    # replaced by its remainder when divided by the smaller number. The algorithm stops
    # when a zero remainder is reached.
    while b != 0:
        a, b = b, a % b
    return a


def get_lcm(a, b):
    """Get least common multiple of two numbers.
    
    a, b: positive integers.
    """
    return a * b // get_gcd(a, b)


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == "__main__":
    N1 = 121932630989178480
    N2 = 121932631112635269
    N3, N4 = 36, 48

    start = time()
    print(f'The GCD of {N1} and {N2} is {get_gcd_slow(N1, N2)}.')
    print(f'Running time for slow method: {round(time() - start, 2)}s\n')

    start = time()
    print(f'The GCD of {N1} and {N2} is {get_gcd(N1, N2)}.')
    print(f'Running time for fast method: {round(time() - start, 2)}s\n')

    print(f'The LCM of {N3} and {N4} is {get_lcm(N3, N4)}.')
