"""有括号的四则混合运算

关于程序的几点说明：
1. 程序可以解析含有加减乘除和括号的算术表达式，所用算法模拟了人们实际做计算的步骤：
   - 扫描算式字符串，获取运算数、运算符，以及按照本单元所学的运算顺序规则，为每个运算符设定运算优先级。
   - 再按照优先级的大小顺序，从最高优先级的运算做起，优先级相同时，从左至右依次计算，直至算出最终结果。
   某些堆栈或递归算法，对算式字符串边扫描边计算，完成一次扫描即可得出结果，效率更高。程序中的算法是先扫描一次，
   确定运算顺序后再计算，这和我们在脱式中的计算过程基本一致，所以更容易理解。
2. 程序在扫描用户输入的算式字符串时，会忽略所有 “0123456789+-*/()” 以外的字符，多重括号仅使用小括号。
"""

def preprocess(expr):
    """把算式字符串转化为三个 list: 运算数，运算符和优先级。数字和 “+-*/()” 以外的字符会被忽略。

    expr: 字符串类型的算式。
    """
    nums = []  # 运算数 list。
    ops = []  # 运算符 list。
    precs = []  # 优先级 list。

    num = ''
    # 加减法的优先级是 0，乘除法是 1，每嵌套一层括号加 2。
    precedence = 0
    for char in expr:
        if char in '0123456789':
            num += char
        elif char in '+-*/' and num != '':
            nums.append(int(num))
            num = ''
            if char in '+-':
                ops.append(char)
                precs.append(precedence)
            else:
                ops.append(char)
                precs.append(precedence + 1)
        elif char == '(':
            precedence += 2
        elif char == ')':
            precedence -= 2
    # 处理最后一个运算数。
    if num:
        nums.append(int(num))
    else:
        ops.pop()
        precs.pop()

    return nums, ops, precs


def calc(nums, ops, precs):
    """返回由 nums, ops, precs 表示的算式的计算结果。

    nums: 运算数 list/tuple。
    ops: 运算符 list/tuple。
    precs: 优先级 list/tuple。
    """
    # 把传过来的三个参数转变或复制为三个新的 list，原参数的值不会受到影响。
    nums, ops, precs = list(nums), list(ops), list(precs)

    while len(nums) > 1:
        # 在优先级 list 中，找到最大优先级对应序号中最小的一个序号。
        idx = precs.index(max(precs))
        if ops[idx] == '+':
            res = nums[idx] + nums[idx + 1]
        elif ops[idx] == '-':
            res = nums[idx] - nums[idx + 1]
        elif ops[idx] == '*':
            res = nums[idx] * nums[idx + 1]
        else:
            # 如果除数是 0，返回 None。
            if nums[idx + 1] == 0:
                return None
            res = nums[idx] / nums[idx + 1]
        # 在相应 list 中，删除刚刚使用过的运算数、运算符和优先级，用运算结果取代原运算数的位置。
        nums.pop(idx)
        nums.pop(idx)
        nums.insert(idx, res)
        ops.pop(idx)
        precs.pop(idx)

    # 如果没有运算数，返回 None。
    if not nums:
        return None
    # 如果计算结果应该是整数，确保返回整数结果。因为无论商是否为整数，除法运算符 “/” 的结果都是 float 类型，
    # 例如 4 / 2 = 2.0。
    if int(nums[0]) == nums[0]:
        return int(nums[0])
    return nums[0]


def my_eval(expr):
    """解析一个字符串类型的算式。

    expr: 字符串类型的算式。
    """
    nums, ops, precs = preprocess(expr)
    return calc(nums, ops, precs)


# 使用特殊变量 __name__ 确保此程序在作为模块被其它程序引用时，以下代码不会被执行。
if __name__ == '__main__':
    expr = input('输入有括号的四则混合运算算式:\n')
    print(my_eval(expr))
