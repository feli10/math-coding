"""项目程序中多次用到的函数和类"""

from random import choice, randint, uniform


CORRECT_WORDS = ['正确', '回答正确', '完全正确', '对', '对了', '答对', '答对了', '你答对了',
                 '准确', '准确无误', '不错', '真不错', '优秀', '太优秀了', '好样的', '耶',
                 '太棒了', '你太棒了', '真棒', '你真棒', '好棒', '你好棒', '棒', '超棒', '一级棒',
                 '太牛了', '你太牛了', '真牛', '你真牛', '好牛', '你好牛', '牛', '超牛',
                 '神了', '太神了', '你太神了', '超神', '赞', '超赞', '强', '超强', '👍']


def question_generator(*question_types, count=2, perfect_score=100):
    """生成指定数量的一种或多种类型题目，完成全部答题后显示分数。
    
    question_types: 多个函数构成的 tuple. 每个函数调用一次可以生成一道特定类型的题目，
                    并根据答题对错返回 True/False。
    count: 生成题目的数量，默认出 2 道题。
    perfect_score: 满分分值，默认 100 分。
    """
    score_per_question = perfect_score / count
    score = 0
    for i in range(count):
        print(f'题目 {i + 1}/{count}:  ', end='')
        question_type = choice(question_types)
        if question_type():
            print(f'{choice(CORRECT_WORDS)}!\n')
            score += score_per_question
    print(f'你的得分 {round(score)}/{perfect_score}。\n')


def answer_check(correct_answer, prompt='? ', check_mode='equal',
                 displayed_answer=None, is_unique=True):
    """输入答案并检查是否答对，如答对返回 True, 如答错显示正确答案并返回 False。

    correct_answer: 用于检查答案是否正确。
    prompt: 用户输入时，屏幕显示的提示文字。
    check_mode:
        'equal': 用户输入内容在数值上与正确答案相等，即算答对。
        'same' : 用户输入内容与正确答案的字符形式完全相同，即算答对。
        'fraction': 用户可以输入分数形式的答案，在数值上与正确答案相等，即算答对。
        'fraction_only': 用户必须输入一个分数，在数值上与正确答案相等，即算答对。
    displayed_answer: 用于显示的正确答案，如果没给，将显示 correct_answer。
    is_unique: 表明题目的正确答案是否是唯一的。
    """
    answer = input(prompt)
    if check_mode == 'equal':
        try:
            if float(answer) == correct_answer:
                return True
        except ValueError:
            pass
    elif check_mode == 'same':
        if answer.strip() == correct_answer:
            return True
    else:
        value = eval_fraction(answer)
        if value is not None and value == correct_answer:
            return True
        if value is None and check_mode == 'fraction':
            try:
                if float(answer) == correct_answer:
                    return True
            except ValueError:
                pass

    if is_unique:
        print(f'回答有误，正确答案是 {displayed_answer or correct_answer}。\n')
    else:
        print(f'回答有误，正确答案不唯一，其中一个是 {displayed_answer or correct_answer}。\n')
    return False


def input_natural_number(prompt='', minimum=0, maximum=None, digit_count=None):
    """确保用户输入一个有效的自然数，并将这个数以字符串的形式返回。
    
    prompt: 用户输入时，屏幕显示的提示文字。
    minimum/maximum: 输入的自然数需在 [minimum, maximum] 范围内，默认从 0 开始。
    digit_count: 要求输入自然数的位数，默认无要求。
    """
    while True:
        num = input(prompt)
        # 检查删除字符串内的所有逗号和空白字符后，其它字符是否仅由数字构成。
        num = ''.join(num.replace(',', '').split())
        if num.isdecimal():
            # 删除最高位上的所有 "0"。
            num = str(int(num))
            # 检查位数是否满足要求。
            if not digit_count or digit_count == len(num):
                # 检查是否在允许范围内.
                if maximum is None:
                    if int(num) >= minimum:
                        return num
                    print(f'输入的数必须大于 {minimum - 1}。')
                else:
                    if minimum <= int(num) <= maximum:
                        return num
                    print(f'输入的数必须在 {minimum} 到 {maximum} 之间。')
            else:
                print(f'输入的数必须是一个 {digit_count} 位数。')
        else:
            print('你输入的不是一个有效的自然数，请重新输入。')


def input_decimal(prompt='', minimum=0, maximum=None, minimum_inclusive=True, fraction=False):
    """用户输入一个在 [minimun, maximum] 范围内的小数，并将这个数以字符串的形式返回。
    
    prompt: 用户输入时，屏幕显示的提示文字。
    minimum/maximum: 输入的小数需在 [minimum, maximum] 范围内。
    minimum_inclusive: minimum 是否包含在取值范围内。
    fraction: 用户是否可以输入一个分数。
    """
    while True:
        decimal = input(prompt)
        try:
            decimal = float(decimal)
            if (decimal == minimum and minimum_inclusive
                or decimal > minimum and (maximum is None or decimal <= maximum)):
                return str(decimal)
        except ValueError:
            if fraction:
                value = eval_fraction(decimal)
                if value is not None:
                    if (value == minimum and minimum_inclusive
                        or value > minimum and (maximum is None or value <= maximum)):
                        return str(value)
        if fraction:
            print('你输入的不是一个有效的小数或分数，请重新输入。')
        else:
            print('你输入的不是一个有效的小数，请重新输入。')


def input_fraction(prompt=''):
    """用户输入一个分数，并返回它的分子和分母。
    
    prompt: 用户输入时，屏幕显示的提示文字。
    """
    while True:
        fraction = input(prompt)
        # 删除字符串内的所有空白字符。
        fraction = ''.join(fraction.split())
        # 检查 fraction 是否是一个整数。
        if fraction.isdecimal():
            return int(fraction), 1
        # 以 "/" 为分隔字符，把 fraction 分成三段，放在 string_tuple 内。
        string_tuple = fraction.partition('/')
        # 检查 fraction 是否是一个有效的分数。
        if (string_tuple[1] == '/' and string_tuple[0].isdecimal()
            and string_tuple[2].isdecimal() and int(string_tuple[2]) != 0):
            return int(string_tuple[0]), int(string_tuple[2])
        print('你输入的不是一个有效的分数，请重新输入。')


def eval_fraction(string):
    """如果 string 是一个分数，返回它的值，否则返回 None。"""
    # 删除字符串内的所有空白字符。
    string = ''.join(string.split())
    # 以 "/" 为分隔字符，把 string 分成三段，放在 string_tuple 内。
    string_tuple = string.partition('/')
    if (string_tuple[1] == '/' and string_tuple[0].isdecimal()
        and string_tuple[2].isdecimal() and int(string_tuple[2]) != 0):
        return int(string_tuple[0]) / int(string_tuple[2])
    return None


def decimal_generator(minimum=0, maximum=1, decimal_place_count=1, decimal_place_count_dist=None):
    """生成一个在 [minimun, maximum] 范围内的小数，返回这个小数和它的小数位数。

    minimun/maximum: 生成的小数需在 [minimum, maximum] 范围内。
    decimal_place_count: 指定的小数位数, 0 代表整数。
    decimal_place_count_dist: 表示指定小数位数可能性分布的列表。例如：[1, 1, 1, 2, 2] 表示有 60% 的可能性
                              生成 1 位小数，有 40% 的可能性生成 2 位小数。
    """
    if decimal_place_count_dist:
        decimal_place_count = choice(decimal_place_count_dist)
    #  如果 decimal_place_count 是 0，生成一个整数。
    if decimal_place_count == 0:
        return randint(minimum, maximum), 0
    # 生成一个具有 decimal_place_count 个小数位数的小数。
    decimal_str = ''
    while (len(decimal_str) - 1 - decimal_str.find('.') != decimal_place_count
           or decimal_str[-2:] == '.0'):
        # round() 四舍五入后会自动删除小数末尾的零（但会保留十分位的零），使用 while 循环以确保 decimal 具有
        # 所需的位数。
        decimal = round(uniform(minimum, maximum), decimal_place_count)
        decimal_str = str(decimal)

    return decimal, decimal_place_count


def remove_trailing_zeros(decimal):
    """删除小数末尾的零且不改变小数的大小。
    
    decimal: 字符串类型的小数。
    """
    decimal = decimal.rstrip('0')
    if decimal[-1] == '.':
        decimal = decimal[:-1]
    return decimal
