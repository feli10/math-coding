"""Area unit conversion practice

Some Useful Information:
1. This program uses the unit_conversion() function of decimal_practice.py (G327) and adds three
   large metric system area units to it: Are (a), Hectare (ha), and Square Kilometer (km²).
2. Users can input either decimals or fractions when converting from a smaller unit to
   a larger unit.
3. When there are many digits to be entered, scientific notation can be used. E.g., 1e3 means
   1 followed by three zeros, which is 1000; 1e-3 means 1/(1e3), which is 1/1000 or 0.001.
"""

from random import randint
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check

# If you want to practice all kinds of units, change AREA_ONLY to False.
AREA_ONLY = True


def unit_conversion():
    """Randomly generate a unit conversion question.
    Return True if the answer is correct, otherwise, show the correct answer and return False.

    The conversions are bidirectional. Users can input either decimals or fractions when 
    coverting from a smaller unit to a larger unit.
    """
    LENGTH_UNITS = ['mm', 'cm', 'dm', 'm']
    MONEY_UNITS = ['cent', 'dime', 'dollar']
    AREA_UNITS = ['mm²', 'cm²', 'dm²', 'm²', 'a', 'ha', 'km²']
    MASS_UNITS = ['g', 'kg', 't']
    TYPES = [LENGTH_UNITS, MONEY_UNITS, AREA_UNITS, MASS_UNITS]
    # FACTORS is a list of conversion factors between all adjacent units of each unit type.
    FACTORS = [10, 10, 100, 1000]

    if AREA_ONLY:
        units = AREA_UNITS
        factor = 100
    else:
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


question_generator(unit_conversion, count=4)
