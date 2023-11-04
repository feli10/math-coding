"""Use equations to solve problems involving chickens and rabbits in the same cage."""

import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number

while True:
    head_count = int(input_natural_number('How many heads? '))
    leg_count = int(input_natural_number('How many legs? '))
    if leg_count % 2 == 0 and head_count * 2 <= leg_count <= head_count * 4:
        break
    print("That's unreasonable! The legs must be an even number and between\n"
          + "two and four times the number of heads. Please enter again.\n")

print(f'\nIf there are x rabbits, then there are {head_count} - x chickens.\n')

left = f'4x + 2·({head_count} - x)'
print(f'{left:>20} = {leg_count}')
left = f'4x + 2·{head_count} - 2x'
print(f'{left:>20} = {leg_count}')
left = '4x - 2x'
print(f'{left:>20} = {leg_count} - {2 * head_count}')
left = '2x'
print(f'{left:>20} = {leg_count - 2 * head_count}')
left = 'x'
print(f'{left:>20} = {leg_count - 2 * head_count} / 2')
rabbit_count = (leg_count - 2 * head_count) // 2
print(f'{left:>20} = {rabbit_count}')
chicken_count = head_count - rabbit_count
print(f'\n    Number of chickens: {head_count} - {rabbit_count} = {chicken_count}')

chicken_ = 'chicken' if chicken_count == 1 else 'chickens'
rabbit_ = 'rabbit' if rabbit_count == 1 else 'rabbits'
print(f'\nSo, there are {chicken_count} {chicken_} and {rabbit_count} {rabbit_}.\n')
