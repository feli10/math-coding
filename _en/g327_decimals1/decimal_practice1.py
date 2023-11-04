"""Generate four types of decimal questions for practice.

Some Useful Information:
1. There are four types of questions. Users can practice one type at a time, or mix
   questions from multiple types.
2. Questions on converting between fractions and decimals may involve 1 to 3 decimal places.
   Questions involving more decimal places are less likely to occur.
3. The unit conversions are bidirectional. Users can input either decimals or fractions when
   converting from a smaller unit to a larger unit.
4. In addition and subtraction of decimals within ten, some operands may be integers to
   increase diversity.
"""

from random import randint, random
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check, decimal_generator


def fraction_to_decimal():
    """Randomly generate a question of converting fractions to decimals.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    # Denominator is 50% likely to be 10, 30% likely to be 100, and 20% likely to be 1000.
    rand = random()  # Return a random float number in the range [0.0, 1.0).
    if rand < 0.5:
        denominator = 10
    elif rand < 0.8:
        denominator = 100
    else:
        denominator = 1000
    numerator = randint(1, denominator)

    print(f'{numerator}/{denominator}')
    correct_answer = numerator / denominator

    return answer_check(correct_answer, prompt='Decimal? ')


def decimal_to_fraction():
    """Randomly generate a question of converting decimals to fractions.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    # Number of decimal places is 50% likely to be 1, 40% likely to be 2, and 10% likely to be 3.
    decimal_place_count_dist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3]
    decimal, decimal_place_count = decimal_generator(0, 1, decimal_place_count_dist=
                                                     decimal_place_count_dist)

    print(decimal)
    displayed_answer = f'{int(decimal * 10 ** decimal_place_count)}/{10 ** decimal_place_count}'

    return answer_check(decimal, prompt='Fraction? ', check_mode='fraction_only',
                        displayed_answer=displayed_answer, is_unique=False)


def add_sub_decimals():
    """Randomly generate a simple decimal addition or subtraction question.
    Return True if the answer is correct, otherwise, show the correct answer and return False.
    """
    # 80% are decimals with one decimal place, 20% are integers (0 decimal places).
    decimal_place_count_dist = [0, 1, 1, 1, 1]
    decimal1, _ = decimal_generator(0, 10, decimal_place_count_dist=decimal_place_count_dist)
    decimal2, _ = decimal_generator(0, 10, decimal_place_count_dist=decimal_place_count_dist)

    if random() < 0.5:
        print(f'{decimal1} + {decimal2} =')
        # decimal1 and decimal2 are actually float numbers and float number operations may
        # behave unexpectedly such as 1.1 + 2.2 = 3.3000000000000003. This is why round() is used.
        correct_answer = round(decimal1 + decimal2, 1)
    else:
        if decimal1 < decimal2:
            decimal1, decimal2 = decimal2, decimal1
        print(f'{decimal1} - {decimal2} =')
        correct_answer = round(decimal1 - decimal2, 1)

    # Remove possible trailing zeros for displaying correct_answer.
    if int(correct_answer) == correct_answer:
        correct_answer = int(correct_answer)

    return answer_check(correct_answer)


def unit_conversion():
    """Randomly generate a unit conversion question.
    Return True if the answer is correct, otherwise, show the correct answer and return False.

    The conversions are bidirectional. Users can input either decimals or fractions when 
    coverting from a smaller unit to a larger unit.
    """
    LENGTH_UNITS = ['mm', 'cm', 'dm', 'm']
    MONEY_UNITS = ['cent', 'dime', 'dollar']
    AREA_UNITS = ['mm²', 'cm²', 'dm²', 'm²']
    MASS_UNITS = ['g', 'kg', 't']
    TYPES = [LENGTH_UNITS, MONEY_UNITS, AREA_UNITS, MASS_UNITS]
    # FACTORS is a list of conversion factors between all adjacent units of each unit type.
    FACTORS = [10, 10, 100, 1000]

    # Choose a unit type randomly.
    index = randint(0, len(TYPES) - 1)
    units = TYPES[index]
    factor = FACTORS[index]

    # Choose the first unit.
    unit1_index = randint(0, len(units) - 1)
    unit1 = units[unit1_index]
    # Choose the second unit different from the first one.
    unit2_index = unit1_index
    while unit2_index == unit1_index:
        unit2_index = randint(0, len(units) - 1)
        unit2 = units[unit2_index]

    print(f'1{unit1} = __{unit2}')
    correct_answer = factor ** (unit1_index - unit2_index)
    if unit1_index > unit2_index:
        return answer_check(correct_answer)
    # Users can input either decimals or fractions when coverting from
    # a smaller unit to a larger unit.
    displayed_answer = f'{correct_answer} or 1/{factor ** (unit2_index - unit1_index)}'
    return answer_check(correct_answer, check_mode='fraction', displayed_answer=displayed_answer)


# Use the special variable __name__ to only execute the following code when this program
# is run and not when it is imported as a module.
if __name__ == '__main__':
    question_generator(fraction_to_decimal, decimal_to_fraction,
                       add_sub_decimals, unit_conversion, count=4)
