"""Volume unit conversion practice

Some Useful Information:
1. This program is based on area_unit_conversion.py (G412) and adds a new unit type volume to
   it with 4 volume units mm³, cm³, dm³, and m³.
2. The program also uses a dictionary UNIT_DICT to store all unit types and provides the list
   PRACTICE_TYPE for users to set which unit types they want to practice.
3. Users can input either decimals or fractions when converting from a smaller unit to
   a larger unit.
4. When there are many digits to be entered, scientific notation can be used. E.g., 1e3 means
   1 followed by three zeros, which is 1000; 1e-3 means 1/(1e3), which is 1/1000 or 0.001.
"""

from random import randint, choice
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import question_generator, answer_check


LENGTH_UNITS = ['mm', 'cm', 'dm', 'm']
MONEY_UNITS = ['cent', 'dime', 'dollar']
AREA_UNITS = ['mm²', 'cm²', 'dm²', 'm²', 'a', 'ha', 'km²']
VOLUME_UNITS = ['mm³', 'cm³', 'dm³', 'm³']
MASS_UNITS = ['g', 'kg', 't']
UNIT_DICT = {'length': (LENGTH_UNITS, 10),
                'money': (MONEY_UNITS, 10),
                'area': (AREA_UNITS, 100),
                'volume': (VOLUME_UNITS, 1000),
                'mass': (MASS_UNITS, 1000)}
# Put the unit types you want to practice into this list.
PRACTICE_TYPES = ['volume']


def check_practice_types():
    """Check whether PRACTICE_TYPES set by user is valid."""
    if not PRACTICE_TYPES:
        raise ValueError('You must choose at least one unit type for practice.')
    for unit_type in PRACTICE_TYPES:
        if unit_type not in UNIT_DICT:
            raise ValueError(f'There is not a unit type named "{unit_type}" in UNIT_DICT.')


def unit_conversion():
    """Randomly generate a unit conversion question.
    Return True if the answer is correct, otherwise, show the correct answer and return False.

    The conversions are bidirectional. Users can input either decimals or fractions when 
    coverting from a smaller unit to a larger unit.
    """
    # Choose a unit type randomly.
    unit_type = choice(PRACTICE_TYPES)
    units, factor = UNIT_DICT[unit_type]

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


check_practice_types()
question_generator(unit_conversion, count=4)
