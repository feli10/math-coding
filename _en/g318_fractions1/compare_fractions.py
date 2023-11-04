"""Generate questions about comparing fractions with the same numerator or
denominator for practice.
"""

from random import randint, sample
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


MAX_DENOMINATOR = 10


def compare_fractions():
    """Generate questions about comparing fractions with the same numerator or denominator randomly.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    # Choose one of the two questoin types.
    if randint(1, 2) == 1:
        # With the same numerator, the larger the denominator, the smaller the fraction.
        numerator = randint(1, MAX_DENOMINATOR - 2)
        denominator1, denominator2 = sample(range(numerator + 1, MAX_DENOMINATOR + 1), 2)
        print(f'{numerator}/{denominator1} __ {numerator}/{denominator2}')
        if denominator1 > denominator2:
            correct_answer = '<'
        else:
            correct_answer = '>'
    else:
        # With the same denominator, the larger the numerator, the larger the fraction.
        denominator = randint(3, MAX_DENOMINATOR)
        numerator1, numerator2 = sample(range(1, denominator), 2)
        print(f'{numerator1}/{denominator} __ {numerator2}/{denominator}')
        if numerator1 > numerator2:
            correct_answer = '>'
        else:
            correct_answer = '<'

    return answer_check(correct_answer, prompt='(> or <) ? ', check_mode='same')


question_generator(compare_fractions, count=4)
