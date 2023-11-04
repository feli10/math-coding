"""Randomly select items with different weights.

Some Useful Information:
1. The program uses 4 methods to implement random selection with different weights. Items
   with greater weight will be more likely to be selected.
2. The get(key, default_value) method of dictionary returns the value of key or returns
   default_value if key doesn't exist. It is often used for counting with a dictionary.
"""

from random import random, randint, choice
from matplotlib import pyplot as plt


TIMES = 10000
OPTIONS = ['A', 'B', 'C', 'D']


def chart(result, title='Statistical Results on Random Selection', xlabel='Items'):
    """Draw a bar chart for statistics in result.
    
    result: a dictionary whose keys are the items and values are the number of times
            the items have been selected.
    """
    # Sort result acoording to its keys.
    result = dict(sorted(result.items()))
    xticks = [str(key) for key in result.keys()]
    rect = plt.bar(xticks, result.values(), width=0.4)
    plt.bar_label(rect)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Number of Times')
    plt.show()


def same_weights():
    """Random selection with the same weights.
    No need to do anything besides using random functions.
    """
    result = {}
    for _ in range(TIMES):
        item = choice(OPTIONS)
        result[item] = result.get(item, 0) + 1
    return result


def hard_cumulative_weights():
    """Random selection with hard-coded cumulative weights.
    Hard coding is embedding data directly into the source code. Because of hard coding,
    the function can only be used with specific options and weights.
    """
    result = {}
    for _ in range(TIMES):
        # random() is used with hard-coded cumulative weights [0.4, 0.7, 0.9, 1].
        # randint(1, 10) can also be used with hard-coded cumulative weights [4, 7, 9, 10].
        rand = random()
        if rand < 0.4:
            result['A'] = result.get('A', 0) + 1
        elif rand < 0.7:
            result['B'] = result.get('B', 0) + 1
        elif rand < 0.9:
            result['C'] = result.get('C', 0) + 1
        else:
            result['D'] = result.get('D', 0) + 1
    return result


def distribution(dist_list):
    """Random selection with a distribution list.
    
    dist_list: items with greater weights will appear more times in dis_list. E.g.,
               ['A', 'A', 'B'] means 'A' is twice as likely as 'B' to be selected.
    """
    result = {}
    for _ in range(TIMES):
        item = choice(dist_list)
        result[item] = result.get(item, 0) + 1
    return result


def cumulative_weights(cum_weight_list):
    """Random selection with a list of cumulative weights.
    
    cum_weight_list: a list of cumulative weights. E.g., if the weights of three items are
                     [1, 2, 1], the cumulative weights should be [1, 3, 4].
    """
    result = {}
    for _ in range(TIMES):
        rand = randint(1, max(cum_weight_list))
        for i, item in enumerate(OPTIONS):
            if rand <= cum_weight_list[i]:
                result[item] = result.get(item, 0) + 1
                break
    return result


def weights(weight_list):
    """Random selection with a list of weights.
    
    weight_list: a list of weights.
    """
    result = {}
    for _ in range(TIMES):
        rand = randint(1, sum(weight_list))
        for i, item in enumerate(OPTIONS):
            if rand <= weight_list[i]:
                result[item] = result.get(item, 0) + 1
                break
            rand -= weight_list[i]
    return result


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == '__main__':
    chart(same_weights(), 'Random Selection with the Same Weights')
    title = 'Random Selection with Weights [4, 3, 2, 1]'
    chart(hard_cumulative_weights(), title)
    chart(distribution(['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D']), title)
    chart(cumulative_weights([4, 7, 9, 10]), title)
    chart(weights([4, 3, 2, 1]), title)
