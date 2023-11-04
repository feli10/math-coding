"""Generate questions of unit conversion for practice.

Some Useful Information:
1. Includes length units (mm, cm, dm, m) and mass units (g, kg, t).
2. The questions doesn't include conversions from smaller units to larger ones,
   e.g. 1cm = __dm, since fractions and decimals haven't been learned yet.
"""

from random import randint
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


def unit_conversion():
    """Generates a unit conversion question randomly.
    Return True if the answer is correct, otherwise, show the correct answer and return False.

    The questions include length and mass units.
    The questoins only include conversions from larger units to smaller ones.
    """
    LENGTH_UNITS = ['mm', 'cm', 'dm', 'm']
    MASS_UNITS = ['g', 'kg', 't']
    TYPES = [LENGTH_UNITS, MASS_UNITS]
    # FACTORS is a list of conversion factors between all adjacent units of each unit type.
    FACTORS = [10, 1000]

    # Choose a unit type randomly.
    index = randint(0, len(TYPES) - 1)
    units = TYPES[index]
    factor = FACTORS[index]

    # Choose two units from the unit type.
    # And make sure unit2 is a smaller unit than unit1.
    unit1_index = randint(1, len(units) - 1)
    unit1 = units[unit1_index]
    unit2_index = randint(0, unit1_index - 1)
    unit2 = units[unit2_index]
    print(f'1{unit1} = __{unit2}')
    correct_answer = factor ** (unit1_index - unit2_index)

    return answer_check(correct_answer)


question_generator(unit_conversion, count=4)
