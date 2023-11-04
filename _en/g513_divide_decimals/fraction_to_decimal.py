"""Generate questions of converting common fractions to decimals for practice."""

from random import randint
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


def fraction_to_decimal():
    """Randomly generate a question of converting common fractions to decimals.
    The fraction's denominator is within 10.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    denominator = randint(2, 10)
    numerator = randint(1, denominator - 1)

    print(f"{numerator}/{denominator}")
    correct_answer = round(numerator / denominator, 3)

    return answer_check(correct_answer, prompt='Decimal? ')

print('Convert Fractions to Decimals.\n'
      + '(For repeating decimals, round to 3 decimal places.)\n')
question_generator(fraction_to_decimal, count=4)
