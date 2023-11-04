"""Built-in set operations

Some Useful Information:
1. The program obtains the intersection and union of two sets using two methods:
   - "list" data type with self-written code;
   - "set" data type with built-in set operations.
2. The output results show:
    - "list" uses [] and "set" uses {}.
    - The sum of the number of elements of the two sets minus the number of elements
      in the intersection is equal to the number of elements in the union.
3. sets have no repeated elements, which means we can also use
   set(my_set_a + my_set_b) to remove repeated elemnets and get the union of two sets.
"""

from random import randint, sample


# Generate two sets represented by list.
my_set_a = sample(range(10), randint(0, 10))
my_set_b = sample(range(10), randint(0, 10))


def my_set_ops():
    """Get intersectoin and union of two sets with using list and self-written code."""
    intersection = []
    union = my_set_a.copy()
    for element in my_set_b:
        if element in my_set_a:
            intersection.append(element)
        else:
            union.append(element)
    print('My set operations using list:')
    display(my_set_a, my_set_b, intersection, union)


def builtin_set_ops():
    """Get intersectoin and union of two sets with using built-in set operations."""
    # Turn lists into built-in sets.
    set_a = set(my_set_a)
    set_b = set(my_set_b)
    # Built-in set operations.
    intersection = set_a & set_b
    union = set_a | set_b
    print('Built-in set operations:')
    display(set_a, set_b, intersection, union)


def display(set_a, set_b, intersection, union):
    """Display the two sets, their intersection and union, and the number of
    elements within each.
    """
    print(f'A: {set_a}, {len(set_a)} elements.')
    print(f'B: {set_b}, {len(set_b)} elements.')
    print(f'Intersection: {intersection}, {len(intersection)} elements.')
    print(f'Union: {union}, {len(union)} elements.')
    print(f'{len(set_a)} + {len(set_b)} - {len(intersection)} = {len(union)}\n')


my_set_ops()
builtin_set_ops()
