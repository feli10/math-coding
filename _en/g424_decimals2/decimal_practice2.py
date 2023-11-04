"""Generate three types of decimal questions for practice.

Some Useful Information:
1. There are three types of questions, in which unit_conversion() is imported from
   decimal_practice1.py (G327). Users can practice one type at a time, or mix questions
   from multiple types.
2. The default data type for representing decimals in Python is float. Float operation is very
   efficient, but there are often errors, e.g. 1.1 + 2.2 = 3.3000000000000003. There is a data
   type Decimal in the decimal module of the Python standard library that is specially used to
   represent decimals. Although the efficiency is not as good as float, it can obtain accurate
   results of decimal operations. The Decimal data type is used in the program to calculate
   correct answers for questions of rounding decimals and moving decimal points.
"""

from random import randint, random
from decimal import Decimal, getcontext, ROUND_HALF_UP
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check, decimal_generator
from g327_decimals1.decimal_practice1 import unit_conversion


def round_decimal():
    """Randomly generate a rounding decimal question.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    MIN_DEC = 0
    MAX_DEC = 100
    # There are equal chances for generated decimals to have 1, 2, 3, or 4 decimal places.
    DEC_PLACE_COUNT_DIST = [1, 2, 3, 4]
    PHRASES = [('the nearest whole number', '0 decimal places'),
               ('the nearest tenth', '1 decimal place'),
               ('the nearest hundredth', '2 decimal places'),
               ('the nearest thousandth', '3 decimal places')]
    # Set the round() function's mode so that 5 will be rounded up in all cases. (The default value
    # is ROUND_HALF_EVEN with which 1.5 and 2.5 are both rounded to the nearest even number 2.)
    getcontext().rounding = ROUND_HALF_UP
    dec, dec_place_count = decimal_generator(MIN_DEC, MAX_DEC,
                                             decimal_place_count_dist=DEC_PLACE_COUNT_DIST)
    new_dec_place_count = randint(0, dec_place_count - 1)
    print(f'{dec} rounded to {PHRASES[new_dec_place_count][randint(0, 1)]}')
    correct_answer = str(round(Decimal(str(dec)), new_dec_place_count))

    return answer_check(correct_answer, check_mode='same')


def move_decimal_point():
    """Randomly generate a calculation question for multiplying or dividing a decimal by 10, 100
    or 1000 to practice moving the decimal point.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    MIN_DEC = 0
    MAX_DEC = 100
    # There are equal chances for generated decimals to have 0, 1, 2, or 3 decimal places.
    DEC_PLACE_COUNT_DIST = [0, 1, 2, 3]
    MAX_MOVE_COUNT = 3

    dec, _ = decimal_generator(MIN_DEC, MAX_DEC, decimal_place_count_dist=DEC_PLACE_COUNT_DIST)
    factor = 10 ** randint(1, MAX_MOVE_COUNT)
    if random() < 0.5:
        print(f'{dec} * {factor} =')
        correct_answer = Decimal(str(dec)) * factor
    else:
        print(f'{dec} / {factor} =')
        correct_answer = Decimal(str(dec)) / factor

    return answer_check(float(correct_answer))


question_generator(round_decimal, move_decimal_point, unit_conversion, count=4)
