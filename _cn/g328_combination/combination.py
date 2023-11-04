"""三类常见计数问题

关于程序的几点说明：
1. 三类计数问题包括：
   - 搭配问题：从两组中各选一个进行搭配，在数学中也被称作笛卡尔积。
   - 排列问题：在同一组中选择多个元素，且选择方案与选择的顺序有关。
   - 组合问题：在同一组中选择多个元素，且选择方案与选择的顺序无关。
2. 程序使用多重循环解决以上三类问题。程序中的三类问题都是选择两个元素，所以都使用二重循环，
   只是各自使用了略有差别的二重循环。如果选择三个元素，则需使用三重循环。当选择元素较多时，
   多重循环就不是一个好的解决方案了，实际中常用递归。但在选择元素不多的情况下，多重循环是
   最能帮助学习者体会和掌握课程内容的实现方法。
3. Python 的标准库中提供了 itertools 模块，其中有与计数相关的多个函数，在今后需要时可以直接调用。
   程序最后把自行编写的函数与 itertools 相应函数的运行结果做了比较，二者是一致的。
"""

import itertools


GROUP1 = ['A', 'B', 'C', 'D']
GROUP2 = ['a', 'b', 'c', 'd']
COUNT1 = len(GROUP1)
COUNT2 = len(GROUP2)


def my_product():
    """从 GROUP1 和 GROUP2 中各选择一个元素。"""
    print('搭配问题')
    results = []
    for i in range(COUNT1):
        print(f'{GROUP1[i]}_:', end='  ')
        for j in range(COUNT2):
            print(f'{GROUP1[i]}{GROUP2[j]}', end= '  ')
            results.append((GROUP1[i], GROUP2[j]))
        print()
    print(f'从第一组 ({COUNT1} 个元素) 和第二组 ({COUNT2} 个元素) 中各选择一个元素，'
          + f'共有 {len(results)} 种选法。\n')
    return results


def my_permutation():
    """从 GROUP1 中选择两个元素 (与数序有关)。"""
    print('排列问题')
    results = []
    for i in range(COUNT1):
        print(f'{GROUP1[i]}_:', end='  ')
        for j in range(COUNT1):
            if i != j:
                print(f'{GROUP1[i]}{GROUP1[j]}', end= '  ')
                results.append((GROUP1[i], GROUP1[j]))
        print()
    print(f'从第一组 ({COUNT1} 个元素) 中选择 2 个元素（与顺序有关），共有 {len(results)} 种选法。\n')
    return results


def my_combination():
    """从 GROUP1 中选择两个元素 (与数序无关)。"""
    print('组合问题')
    results = []
    for i in range(COUNT1):
        print(f'{GROUP1[i]}_:', end='  ')
        for j in range(i + 1, COUNT1):
            print(f'{GROUP1[i]}{GROUP1[j]}', end='  ')
            results.append((GROUP1[i], GROUP1[j]))
        print()
    print(f'从第一组 ({COUNT1} 个元素) 中选择 2 个元素（与顺序无关），共有 {len(results)} 种选法。\n')
    return results


# 显示三类计数问题的结果。
my_product_result = my_product()
my_permutation_result = my_permutation()
my_combination_result = my_combination()

# 检验自行编写的函数与 itertools 相应函数的运行结果是否一致。
print(my_product_result == list(itertools.product(GROUP1, GROUP2)))
print(my_permutation_result == list(itertools.permutations(GROUP1, 2)))
print(my_combination_result == list(itertools.combinations(GROUP1, 2)))
