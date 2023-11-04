"""随机选择可能性不同的选项

关于程序的几点说明：
1. 程序给出了四种使用常见随机函数选择可能性不同的选项的方法。程序中使用“权重” (Weight) 来表示可能性的大小，
   权重越大，被选中的可能性也越大。
2. get(key, default_value) 方法返回字典 (dict) 中 key 对应的值，如果 key 不存在，则返回 default_value。
   此方法常用于使用字典进行数据统计。
"""

from random import random, randint, choice
import matplotlib as mpl
from matplotlib import pyplot as plt


TIMES = 10000
OPTIONS = ['A', 'B', 'C', 'D']


def chart(result, title='随机选择的统计结果', xlabel='选项'):
    """把 result 中的统计数据绘制成条形统计图。
    
    result: 字典数据类型，其中的 key 是所有可能的选项, value 是各选项出现的次数。
    """
    # Sort result acoording to its keys.
    result = dict(sorted(result.items()))
    xticks = [str(key) for key in result.keys()]
    rect = plt.bar(xticks, result.values(), width=0.4)
    plt.bar_label(rect)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('出现次数')
    plt.show()


def same_weights():
    """随机选择可能性相同的选项。直接使用随机函数即可。"""
    result = {}
    for _ in range(TIMES):
        item = choice(OPTIONS)
        result[item] = result.get(item, 0) + 1
    return result


def hard_cumulative_weights():
    """随机选择可能性不同的选项，使用嵌入函数中的累计权重。
    因为权重值已经写死在函数中，所以函数只能用于一种特定情况，不具备通用性。
    """
    result = {}
    for _ in range(TIMES):
        # 使用 random() 和嵌入函数中的累计权重 [0.4, 0.7, 0.9, 1]。
        # 此处也可以使用 randint(1, 10)，配合相应的累计权重 [4, 7, 9, 10]。
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
    """随机选择可能性不同的选项，使用表示不同可能性的选项分布列表。
    
    dist_list: 选项分布列表。在分布列表中出现次数越多的选项，被选中的可能性也越大。例如 ['A', 'A', 'B']
               表示 'A' 被选中的可能性是 'B' 的二倍。
    """
    result = {}
    for _ in range(TIMES):
        item = choice(dist_list)
        result[item] = result.get(item, 0) + 1
    return result


def cumulative_weights(cum_weight_list):
    """随机选择可能性不同的选项，使用累计权重列表。
    
    cum_weight_list: 累计权重列表。例如，如果三个选项的权重列表是 [1, 2, 1]，则累计权重列表是 [1, 3, 4]。
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
    """随机选择可能性不同的选项，使用权重列表。
    
    weight_list: 权重列表。
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


# 在 Matplotlib 中使用中文字体，SimHei 是 Windows 的内置字体，Arial Unicode MS 是 MacOS 的内置字体。
font_names = ['SimHei', 'Arial Unicode MS']
mpl.rcParams['font.sans-serif'] = font_names + mpl.rcParams['font.sans-serif']

# 使用特殊变量 __name__ 确保此程序在作为模块被其它程序引用时，以下代码不会被执行。
if __name__ == '__main__':
    chart(same_weights(), 'Random Selection with the Same Weights')
    title = 'Random Selection with Weights [4, 3, 2, 1]'
    chart(hard_cumulative_weights(), title)
    chart(distribution(['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D']), title)
    chart(cumulative_weights([4, 7, 9, 10]), title)
    chart(weights([4, 3, 2, 1]), title)
