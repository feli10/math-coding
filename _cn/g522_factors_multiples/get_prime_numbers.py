"""获取 n 以内的所有质数

关于程序的几点说明：
1. 程序中编写了与因数和质数有关的四个函数，其中后两个函数是获取 n 以内所有质数的两种方法。
   1) get_factors(n): 获取 n 的所有因数。
   2) is_prime_number(n): 判断 n 是否为质数。
   3) get_prime_numbers_slow(n): 获取 n 以内的所有质数。利用 is_prime_number() 函数依次检验
      每一个小于 n 的数是不是质数。这种方法简单直观，但运行时间较长；
   4) get_prime_numbers(n): 获取 n 以内的所有质数。划掉数表中所有是其它数倍数的数，剩下没有被划掉
      的数就是 n 以内的全部质数。这种方法虽然没有第一种方法直观，运行时间却少得多。
"""

from math import sqrt
from time import time


def get_factors(n):
    """获取 n 的所有因数。
    
    n: 正整数。
    """
    factors_front = []
    factors_behind = []
    # 因数一般都是成对出现的，如果 i 是 n 的因数，那么 n/i 也是 n 的因数。换言之，找到一个小于 sqrt(n)
    # 的因数，也就同时找到了一个大于 sqrt(n) 的因数，因此从 1 循环到 sqrt(n) 就可以找到 n 的全部因数。
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors_front.append(i)
            factors_behind.append(n // i)
    if factors_front[-1] == factors_behind[-1]:
        factors_behind.pop()
    factors_behind.reverse()
    return factors_front + factors_behind


def is_prime_number(n):
    """ 判断 n 是否为质数。
    
    n: 正整数。
    """
    if n < 2:
        return False
    if n == 2:
        return True
    # 检查是否能被 2 整除。
    if n % 2 == 0:
        return False
    # 检查完 2 后，只需检查所有不大于 sqrt(n) 的奇数。
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_prime_numbers_slow(n):
    """获取 n 以内的所有质数。利用 is_prime_number() 函数依次检验每一个小于 n 的数是不是质数。
    这种方法简单直观，但运行时间较长

    n: 正整数。
    """
    prime_numbers = []
    for i in range(2, n + 1):
        if is_prime_number(i):
            prime_numbers.append(i)
    return prime_numbers


def get_prime_numbers(n):
    """获取 n 以内的所有质数。划掉数表中所有是其它数倍数的数，剩下没有被划掉的数就是 n 以内的全部质数。
    这种方法虽然没有第一种方法直观，运行时间却少得多。

    n: 正整数。
    """
    # num_list 是一个包含 n 以内所有数的数表. 取值 False 表示这个数被划掉了，True 表示这个数还在数表中，
    # 数表中最后剩下的数就是 n 以内的全部质数。
    num_list = [True for i in range(n + 1)]
    num_list[0] = num_list[1] = False
    # 只需要划掉 2 到 sqrt(n) 的倍数。因为对于 sqrt(n) 的 k 倍，当 k < sqrt(n) 时，在前面划 k 的倍数
    # 时已经被划掉了；而当 k > sqrt(n) 时，sqrt(n) 的 k 倍又超出了 n 的范围。所以划完 sqrt(n) 的倍数，
    # 数表中所有是其它数倍数的数就都已经被划掉了。
    for i in range(2, int(sqrt(n)) + 1):
        if num_list[i]:
            for j in range(i * i, n + 1, i):
                num_list[j] = False
    # 根据数表中剩余的数，获取所有质数。
    prime_numbers = []
    for i in range(2, n + 1):
        if num_list[i]:
            prime_numbers.append(i)
    return prime_numbers


# 使用特殊变量 __name__ 确保此程序在作为模块被其它程序引用时，以下代码不会被执行。
if __name__ == '__main__':
    N = 10000000

    print(f'100 的所有因数: {get_factors(100)}\n')

    print(f'100 以内的所有质数: {get_prime_numbers(100)}\n')

    start = time()
    print(f'{N} 以内质数的个数: {len(get_prime_numbers_slow(N))}')
    print(f'较慢方法的运行时间: {round(time() - start, 2)}s\n')

    start = time()
    print(f'{N} 以内质数的个数: {len(get_prime_numbers(N))}')
    print(f'较快方法的运行时间: {round(time() - start, 2)}s\n')
