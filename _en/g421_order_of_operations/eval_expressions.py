"""Evaluate Arithmetic Expressions

Some Useful Information:
1. The program doesn't use stack or recursion algorithms for evaluating expressions. Instead,
   it simulates our actual calculation process which is less efficient but more understandable.
   The program first converts the arithmetic expression string into three lists of operands,
   operators, and precedences. Then, it calculates the result in descending order of operator
   precedence.
2. Characters in the expression other than digits and "+-*/()" are ignored. Nested parentheses
   all use "()".
"""

def preprocess(expr):
    """Convert an arithmetic expression string into three lists of operands, operators, and
    precedences. Characters other than digits and "+-*/()" are ignored.

    expr: a string type arithmetic expression.
    """
    nums = []  # List of operands.
    ops = []  # List of operators.
    precs = []  # List of precedences.

    num = ''
    # The precedence is 0 for +- and 1 for */. 2 is added for each nested parentheses.
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
    # Deal with the last operand.
    if num:
        nums.append(int(num))
    else:
        ops.pop()
        precs.pop()

    return nums, ops, precs


def calc(nums, ops, precs):
    """Calculate and return the result of an arithmetic expression represented by nums, ops,
    and precs.

    nums: a list/tuple of operands.
    ops: a list/tuple of operators.
    precs: a list/tuple of precedences.
    """
    # Convert or copy the three passed parameters into three new lists. The values of the
    # original parameters will not be affected.
    nums, ops, precs = list(nums), list(ops), list(precs)

    while len(nums) > 1:
        # Find the operators with the largest precedence starting from the smallest index.
        idx = precs.index(max(precs))
        if ops[idx] == '+':
            res = nums[idx] + nums[idx + 1]
        elif ops[idx] == '-':
            res = nums[idx] - nums[idx + 1]
        elif ops[idx] == '*':
            res = nums[idx] * nums[idx + 1]
        else:
            # Return None if the divisor is 0.
            if nums[idx + 1] == 0:
                return None
            res = nums[idx] / nums[idx + 1]
        # Remove the used operands, operator, and precedence in their respective lists and
        # replace the removed operands with the operation result.
        nums.pop(idx)
        nums.pop(idx)
        nums.insert(idx, res)
        ops.pop(idx)
        precs.pop(idx)

    # Return None if there is no operands.
    if not nums:
        return None
    # Return an integer if the result is indeed an integer, because "/" operation will result
    # in a float even when the actual value is an integer (e.g. 4/2 = 2.0).
    if int(nums[0]) == nums[0]:
        return int(nums[0])
    return nums[0]


def my_eval(expr):
    """Evaluate an arithmetic expression.

    expr: a string type arithmetic expression.
    """
    nums, ops, precs = preprocess(expr)
    return calc(nums, ops, precs)


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == '__main__':
    expr = input('Enter an arithmetic expression:\n')
    print(my_eval(expr))
