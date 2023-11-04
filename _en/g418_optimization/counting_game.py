"""Counting Game

Some Useful Information:
1. Two player take turns counting. Each turn, they choose a number within a given range and
   add it to the shared counter. Whoever makes the counter reach the target number will win. 
   This program simulates this game with a player and computer. The player counts first.
2. There is a winning strategy to this game. Take the addition range 1 to 3 and the target number
   21 as an example. To make the counter reach 21, you first need to make the counter 17, because
   no matter if the opponent choose +1, +2 or +3, you can add to 21 on your next turn. Similarly,
   if you want to make the counter 17, you have to make the counter 13, and so on. Using this
   method, you will have a list of "winning numbers:" (21, 17, 13, 9, 5, 1). So, as long as 0 is
   not a winning number, the player who counts first can count the first winning number, leading
   to guaranteed victory. The program also uses this strategy. So, If the player makes a mistake,
   the computer will make the counter a winning number and eventually win the game.
"""

from random import randint
from time import sleep
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


def count(counter, target, max_count):
    """If counter is not a winning number for target, return a number from 1 to max_count that can
    be added to counter to make it a winning number. Otherwise, return a random valid number.
    
    counter: the number of current counter.
    target: the target number.
    max_count: the max number that can be added to counter.
    """
    # When counter is a winning number, the following remainder should be zero.
    remainder = (target - counter) % (1 + max_count)
    # If remainder is not zero, remaider itself is the number within [1, max_count] that can be
    # added to counter and make it a winning number. Otherwise, return a random valid number.
    if remainder != 0:
        return remainder
    return randint(1, max_count)


def start():
    """Start a game with random parameters."""
    max_count = randint(2, 5)
    target = randint(max_count * 5, max_count * 10)
    print(f'Each turn, you can choose a number from {list(range(1, max_count + 1))} to add to '
          + f'the shared counter.\nWhoever makes the counter reach exactly {target} wins.\n')

    win = False
    current = 0
    while True:
        # Player's turn.
        print(f'Current counter: {current} -> Target number: {target}')
        num = int(input_natural_number('Your turn: ', 1, min(max_count, target - current)))
        print()
        current += num
        if current == target:
            win = True
            break
        # Computer's turn.
        print(f'Current counter: {current} -> Target number: {target}')
        # flush=True is used to display the string before sleep().
        print("Computer's turn: ", end='', flush=True)
        # Wait a short time, as if the computer is thinking.
        sleep(0.5)
        num = count(current, target, max_count)
        print(f'{num}\n')
        current += num
        if current == target:
            break
    print(f'Current counter: {current} = Target number: {target}')
    if win:
        print('You win!')
    else:
        print('Computer wins!')


start()
