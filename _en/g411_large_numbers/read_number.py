"""Read and display any given numbers in text.

Some Useful Information:
1. Uses American grammar and spelling.
2. Inputed natural numbers must be within range [0, 10^48).
"""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
SCALES = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion',
          'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion',
          'duodecillion', 'tredecilliion', 'quattuordecillion']


def read_inside_thousand(num):
    """Read a number in range [0, 999] and return the words.

    num: an integer between 0 and 999.
    """
    text = ''
    if num >= 100:
        text += ONES[num // 100] + ' hundred'
        num = num % 100
    if num >= 20:
        text += ' ' + TENS[num // 10]
        num = num % 10
    text += ' ' + ONES[num]
    return text.strip()


def read_number(num):
    """Read any numbers and return the words.
    
    num: string type natural number (non-negative integer).
    """
    if num == '0':
        return 'zero'
    text = ''
    digit_count = len(num)
    scale_count = digit_count // 3
    highest_scale_digit_count = digit_count % 3
    if scale_count != 0 and highest_scale_digit_count != 0:
        text += (read_inside_thousand(int(num[:highest_scale_digit_count])) + ' '
                 + SCALES[scale_count] + ' ')
        num = num[highest_scale_digit_count:]
    for i in range(1, scale_count):
        if int(num[:3]) != 0:
            text += read_inside_thousand(int(num[:3])) + ' ' + SCALES[scale_count - i] + ' '
        num = num[3:]
    text += read_inside_thousand(int(num))
    return text


num = input_natural_number('Enter a natural number: ')
print(read_number(num))
