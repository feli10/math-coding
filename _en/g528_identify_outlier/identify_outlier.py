"""Identify the Defective Item

Some Useful Information:
1. The program uses recursion - an algorithm that solves a problem by solving a smaller instance
   of the same problem until the problem is so small that it can be solved directly (this smallest
   problem is known as the base case). Specifically, recursion uses functions that call themselves
   from within their own code.
2. When using recursion, it is essential to provide termination conditions (base cases). Otherwise,
   the program will result in infinite recursion and end up exceeding the maximum recursion depth
   (default is 1000 in Python).
"""

INDENT_SYMBOL = '....'


def identify_outlier(items, count=0):
    """Identify the outlier from items.
    
    items: list of identical items that need to be checked for the outlier.
    count: recursion depth, also the number of rounds weighed.
    """
    # Divide all items into three groups as equally as possible, with equal quantities of
    # items in group1 and group2.
    item_count = len(items)
    group_count = round(item_count / 3)
    group1 = items[:group_count]
    group2 = items[group_count : group_count * 2]
    group3 = items[group_count * 2:]

    # Weigh group1 and group2.
    print(INDENT_SYMBOL * count + f'Round {count + 1}: {group1} vs {group2}')
    # If nothing left.
    if len(group3) == 0:
        print(INDENT_SYMBOL * count + 'The defective item is identified.')
        return count + 1

    # If balanced, check group3.
    if len(group3) == 1:
        print(INDENT_SYMBOL * count + f'If balanced, {group3[0]} contains the outlier.')
        count_balanced = count + 1
    else:
        print(INDENT_SYMBOL * count + 'If balanced:')
        count_balanced = identify_outlier(group3, count + 1)

    # If unbalanced, check group1.
    if len(group1) == 1:
        print(INDENT_SYMBOL * count + 'If unbalanced, the defective item is identified.')
        return count_balanced
    print(INDENT_SYMBOL * count + f'If unbalanced, assuming {group1} contains the outlier:')
    count_unbalanced = identify_outlier(group1, count + 1)

    return max(count_balanced, count_unbalanced)

n = int(input('How many items need to be checked? '))
items = list(range(1, n + 1))
print(f'{items}\n')
print('\nWe can ensure that we will find the defective item in at least'
      + f' {identify_outlier(items)} rounds.\n')
