"""找次品

关于程序的几点说明：
1. 程序中使用了“递归” (Recursion)，递归是一种在函数中调用自身的结构，可以实现复杂的程序流程。使用递归时一定要
   在递归函数中设置终止条件，否则函数会无休止的调用自身直到超出最大的递归深度后程序报错 (Python 默认为 1000)。
"""

INDENT_SYMBOL = '....'


def identify_outlier(items, count=0):
    """从 items 中找到次品。
    
    items: 待检查的产品列表。
    count: 递归深度，也是已称量的次数。
    """
    # 把所有产品尽可能平均分成三组，并保证 group1 和 group2 的产品数相同。
    item_count = len(items)
    group_count = round(item_count / 3)
    group1 = items[:group_count]
    group2 = items[group_count : group_count * 2]
    group3 = items[group_count * 2:]

    # 称量 group1 和 group2。
    print(INDENT_SYMBOL * count + f'第 {count + 1} 次: {group1} vs {group2}')
    # 如果没有剩余（即 group1 和 group2 各有一个产品，group3 没有产品）。
    if len(group3) == 0:
        print(INDENT_SYMBOL * count + '有问题的是次品。')
        return count + 1

    # 如果天平平衡，检查 group3。
    if len(group3) == 1:
        print(INDENT_SYMBOL * count + f'如果平衡，{group3[0]} 是次品。')
        count_balanced = count + 1
    else:
        print(INDENT_SYMBOL * count + '如果平衡:')
        count_balanced = identify_outlier(group3, count + 1)

    # 如果天平不平衡，检查 group1（假设 group1 有问题）。
    if len(group1) == 1:
        print(INDENT_SYMBOL * count + '如果不平衡，有问题的是次品。')
        return count_balanced
    print(INDENT_SYMBOL * count + f'如果不平衡，假设 {group1} 有问题:')
    count_unbalanced = identify_outlier(group1, count + 1)

    return max(count_balanced, count_unbalanced)

n = int(input('从多少件产品中找次品? '))
items = list(range(1, n + 1))
print(f'{items}\n')
print(f'\n至少称 {identify_outlier(items)} 次，肯定能找出次品。')
