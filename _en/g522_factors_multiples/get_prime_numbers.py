"""Factors and Prime Numbers

Some Useful Information:
1. There are 4 functions related to factors and prime numbers in the program.
   1) get_factors(n): get all factors of n.
   2) is_prime_number(n): check if n is a prime number.
   3) get_prime_numbers_slow(n): get all prime numbers within n by using is_prime_number() to
      check each number one by one. This method is slower.
   4) get_prime_numbers(n): get all prime numbers within n by removing all multiples of numbers
      within the range. The numbers left are prime numbers. This method is faster.
"""

from math import sqrt
from time import time


def get_factors(n):
    """Get all factors of the given number.
    
    n: a positive integer.
    """
    factors_front = []
    factors_behind = []
    # If i is a factor of n, then n/i is also a factor of n. So, we don't need to find factors
    # from 1 all the way to n or n/2. Instead, we just need to find factors from 1 to sqrt(n).
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors_front.append(i)
            factors_behind.append(n // i)
    if factors_front[-1] == factors_behind[-1]:
        factors_behind.pop()
    factors_behind.reverse()
    return factors_front + factors_behind


def is_prime_number(n):
    """Check if the given number is a prime number.
    
    n: a positive integer.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Besides 2, only odd numbers that are not larger than sqrt(n) need to be checked.
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_prime_numbers_slow(n):
    """Get all prime numbers within the given number by using is_prime_number() to check each
    number one by one. This method is slower.

    n: a positive integer.
    """
    prime_numbers = []
    for i in range(2, n + 1):
        if is_prime_number(i):
            prime_numbers.append(i)
    return prime_numbers


def get_prime_numbers(n):
    """Get all prime numbers within the given number by removing all multiples of numbers
    within the range. The numbers left are prime numbers. This method is faster.

    n: a positive integer.
    """
    # num_list is a list of all numbers up to n. The values represent which numbers are removed
    # (False) and which numbers are left (True). The numbers left will be prime numbers.
    num_list = [True for i in range(n + 1)]
    num_list[0] = num_list[1] = False
    # To find all prime numbers within n, we only need to remove numbers that are multiples of
    # numbers from 2 to int(sqrt(n)). This is because numbers that are k times int(sqrt(n))
    # (k < sqrt(n)) have already been removed and numbers that are k times int(sqrt(n))
    # (k > sqrt(n)) exceed n.
    for i in range(2, int(sqrt(n)) + 1):
        if num_list[i]:
            for j in range(i * i, n + 1, i):
                num_list[j] = False
    # Get prime numbers from num_list.
    prime_numbers = []
    for i in range(2, n + 1):
        if num_list[i]:
            prime_numbers.append(i)
    return prime_numbers


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == '__main__':
    N = 10000000

    print(f'Factors of 100 are: {get_factors(100)}\n')

    print(f'Prime numbers within 100 are: {get_prime_numbers(100)}\n')

    start = time()
    print(f'Number of prime numbers within {N}: {len(get_prime_numbers_slow(N))}')
    print(f'Running time for slow method: {round(time() - start, 2)}s\n')

    start = time()
    print(f'Number of prime numbers within {N}: {len(get_prime_numbers(N))}')
    print(f'Running time for fast method: {round(time() - start, 2)}s\n')
