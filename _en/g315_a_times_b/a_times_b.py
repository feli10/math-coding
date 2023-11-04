"""Generate three types of multiplication word problems (a times b) for practice."""

from random import randint
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


def multiplication_word_problem():
    """Generates one of three types of multiplication word problems randomly.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    # Generate numbers used in the word problem.
    num1 = randint(1, 9)
    times = randint(1, 9)
    num2 = num1 * times

    # Choose one of the three problem types.
    problem_type = randint(1, 3)
    if problem_type == 1:
        print(f'What is {times} times {num1}?')
        correct_answer = num2
    elif problem_type == 2:
        print(f'{num2} is how many times {num1}?')
        correct_answer = times
    else:
        print(f'{times} times a number is {num2}, what is this number?')
        correct_answer = num1

    return answer_check(correct_answer)


question_generator(multiplication_word_problem, count=4)
