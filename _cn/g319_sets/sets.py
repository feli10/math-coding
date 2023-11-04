"""集合运算

关于程序的几点说明：
1. 程序使用两种方法获取两个集合的交集和并集：第一种是使用 list 数据类型表示集合，
   自行编程得到交集和并集；第二种是使用 Python 内置的 set 数据类型表示集合，
   直接使用 set 运算得到交集和并集。
2. 从输出的结果中可以看出：
   - list 使用 [] 而 set 使用 {}。
   - 两个集合的元素数之和减去公共元素数等于全体元素数。
3. set 内没有重复的元素，所以也可以用 set(my_set_a + my_set_b) 去除重复元素
   得到两个集合的并集。
"""

from random import randint, sample


# 生成用 list 数据类型表示的两个集合。
my_set_a = sample(range(10), randint(0, 10))
my_set_b = sample(range(10), randint(0, 10))


def my_set_ops():
    """使用 list 形式的集合自行编程得到交集和并集。"""
    intersection = []
    union = my_set_a.copy()
    for element in my_set_b:
        if element in my_set_a:
            intersection.append(element)
        else:
            union.append(element)
    print('使用 list 自行编程:')
    display(my_set_a, my_set_b, intersection, union)


def builtin_set_ops():
    """使用 set 数据类型以及内置的 set 运算得到交集和并集。"""
    # 把 list 转换为 set 数据类型。
    set_a = set(my_set_a)
    set_b = set(my_set_b)
    # 内置 set 运算。
    intersection = set_a & set_b
    union = set_a | set_b
    print('使用内置 set 运算:')
    display(set_a, set_b, intersection, union)


def display(set_a, set_b, intersection, union):
    """显示两个集合、它们的交集、并集，以及所有集合的元素数。"""
    print(f'A: {set_a}, {len(set_a)} 个元素。')
    print(f'B: {set_b}, {len(set_b)} 个元素。')
    print(f'公共: {intersection}, {len(intersection)} 个元素。')
    print(f'全体: {union}, {len(union)} 个元素。')
    print(f'{len(set_a)} + {len(set_b)} - {len(intersection)} = {len(union)}\n')


my_set_ops()
builtin_set_ops()
