"""Three common types of counting problems

Some Useful Information:
1. Three counting problems include:
   - Cartesian Product: Select one item each from two groups.
   - Permutation: Select and arrange two items from a group (order matters).
   - Combination: Select two items from a group (order doesn't matter).
2. The program uses three slightly different types of nested loops to solve the above three
   types of problems. Selecting m items will use m nested loops, so when m is large, nested
   loops are not a good solution and recursion is often used in practice. However, when m is
   small, nested loops are the implementation that can best help learners understand counting
   problems.
4. Python's standard library provides the itertools module, which contains multiple functions
   related to counting problems and can be used directly in the future. The program also compares
   the results of self-written functions to corresponding itertools functions, showing they are
   the same.
"""

import itertools


GROUP1 = ['A', 'B', 'C', 'D']
GROUP2 = ['a', 'b', 'c', 'd']
COUNT1 = len(GROUP1)
COUNT2 = len(GROUP2)


def my_product():
    """Select one item each from GROUP1 and GROUP2."""
    print('Cartesian Product')
    results = []
    for i in range(COUNT1):
        print(f'{GROUP1[i]}_:', end='  ')
        for j in range(COUNT2):
            print(f'{GROUP1[i]}{GROUP2[j]}', end= '  ')
            results.append((GROUP1[i], GROUP2[j]))
        print()
    print(f'There are {len(results)} ways to select 1 item each from group1 ({COUNT1} items) '
          + f'and group2 ({COUNT2} items).\n')
    return results


def my_permutation():
    """Select and arrange two items from GROUP1 (order matters)."""
    print('Permutation')
    results = []
    for i in range(COUNT1):
        print(f'{GROUP1[i]}_:', end='  ')
        for j in range(COUNT1):
            if i != j:
                print(f'{GROUP1[i]}{GROUP1[j]}', end= '  ')
                results.append((GROUP1[i], GROUP1[j]))
        print()
    print(f'There are {len(results)} ways to select 2 items from group1 ({COUNT1} items) '
          + 'when order matters.\n')
    return results


def my_combination():
    """Select two items from GROUP1 (order doesn't matter)."""
    print('Combination')
    results = []
    for i in range(COUNT1):
        print(f'{GROUP1[i]}_:', end='  ')
        for j in range(i + 1, COUNT1):
            print(f'{GROUP1[i]}{GROUP1[j]}', end='  ')
            results.append((GROUP1[i], GROUP1[j]))
        print()
    print(f'There are {len(results)} ways to select 2 items from group1 ({COUNT1} items) '
          + "when order doesn't matter.\n")
    return results


# Display the results of three types of common counting problems.
my_product_result = my_product()
my_permutation_result = my_permutation()
my_combination_result = my_combination()

# Show whether the results of self-written functions and
# corresponding itertools functions are the same.
print(my_product_result == list(itertools.product(GROUP1, GROUP2)))
print(my_permutation_result == list(itertools.permutations(GROUP1, 2)))
print(my_combination_result == list(itertools.combinations(GROUP1, 2)))
