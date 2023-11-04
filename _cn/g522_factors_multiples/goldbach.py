"""哥德巴赫猜想"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number
from g522_factors_multiples.get_prime_numbers import is_prime_number


def goldbach(n):
    """找到两个质数，它们的和是 n。
    
    n: 一个大于 2 的偶数。
    """
    if n == 4:
        return 2, 2
    for i in range(3, n // 2 + 1, 2):
        if is_prime_number(i) and is_prime_number(n - i):
            return i, n - i
    return '哥德巴赫猜想错了！'


while True:
    num = int(input_natural_number('输入一个大于 2 的偶数: ', 3))
    if num % 2 == 0:
        break
    print("你输入的不是偶数，请重新输入。")

num1, num2 = goldbach(num)
print(f'{num} = {num1} + {num2}')
