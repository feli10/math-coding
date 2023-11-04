"""Generate questions of 2-digit addition or subtraction for practice."""

from random import randint
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


def add_sub_2digit():
    """Generates a 2-digit addition or subtraction question randomly.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    # Generate two random 2-digit numbers.
    num1 = randint(10, 99)
    num2 = randint(10, 99)

    # Choose addition or subtraction randomly. Each has 50% chance to be chosen.
    if randint(0, 1) == 0:
        print(f'{num1} + {num2} =')
        correct_answer = num1 + num2
    else:
        # Make num1 the larger number when doing subtraction.
        if num1 < num2:
            num1, num2 = num2, num1
        print(f'{num1} - {num2} =')
        correct_answer = num1 - num2

    return answer_check(correct_answer)


question_generator(add_sub_2digit, count=4)
