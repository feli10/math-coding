"""读出任意自然数

关于程序的几点说明：
1. 主要规则：
   - 先分级，从最高级读起；
   - 每一级都按照个级数的读法来读，读完亿级或万级的数，要加 “亿” 字或 “万” 字；
   - 每级末尾不管有几个零，都不读，其他数位上有一个零或连续几个零，都只读一个零。
2. 补充规则：
   - 在一个数级中如果是十或十几开头（前面没有零），读作 “十” 或 “十几”， 否则读作 “一十” 或 “一十几”。
   - 如果万级是 '0000', 不读 “万” 字，只读一个 “零”。
   - 不使用 ”兆“、”京“ 等计数单位，而是 “亿” 字叠用。
3. 为了方便用户数位数，输入时可以使用逗号或空格把大数进行分段。
"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


DIGITS = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
COUNTING_UNITS = ['千', '百', '十', '']


def read_level_number(num):
    """按照个级的读法把一个数级的数读出来。
    
    num: 字符串类型的自然数 (0-9999之间)。
    """
    # 在一个数级中如果是十或十几开头（前面没有零），读作 “十” 或 “十几”。
    if num[0] != '0' and 10 <= int(num) < 20:
        return '十' + DIGITS[int(num) - 10]

    digit_count = len(num)
    # 每级末尾不管有几个零都不读。
    none_trailing_zero_digit_count = len(num.rstrip('0'))
    text = ''
    after_zero = False
    for i in range(none_trailing_zero_digit_count):
        digit = int(num[i])
        # 每级除末尾外的其他数位，有一个零或连续几个零，都只读一个零。
        if digit == 0 and not after_zero:
            text += '零'
            after_zero = True
        elif digit != 0:
            text += DIGITS[digit] + COUNTING_UNITS[4 - digit_count + i]
            after_zero = False
    return text


def read_number(num):
    """读出任意自然数。
    
    num: 字符串类型的自然数。
    """
    if num == '0':
        return '零'

    level_count = len(num) // 4
    highest_level_digit_count = len(num) % 4
    if highest_level_digit_count == 0:
        highest_level_digit_count = 4
    else:
        level_count += 1

    text =''
    empty_level = False
    for i in range(level_count, 0, -1):
        if i == level_count:
            level_num = num[0:highest_level_digit_count]
            num = num[highest_level_digit_count:]
        else:
            level_num = num[0:4]
            num = num[4:]
        # 如果 level_num 的最高位不为零，则调用 read_level_number() 在最前面不会读零，
        # 此时如果前面有一个空的万级，则需要读出一个零。
        if empty_level and level_num[0] != '0':
            text += '零'
        text += read_level_number(level_num)

        # 每个数级交替读出 “万” 和 “亿”。
        if i > 1:
            if i % 2 == 0:
                # 如果万级是空的，不需要读 “万” 字。
                if level_num == '0000':
                    empty_level = True
                else:
                    text += '万'
                    empty_level = False
            else:
                text += '亿'
                empty_level = False
    return text


num = input_natural_number('输入一个自然数: ')
print(read_number(num))
