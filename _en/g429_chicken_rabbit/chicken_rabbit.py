"""Chickens and Rabbits in the Same Cage"""

from random import randint
import tkinter as tk
import sys
from pathlib import Path
# Add the parent directory to sys.path so that other project modules can be imported.
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


IMG_WIDTH = 155
IMG_HEIGHT = 200

# Generate a question of chickens and rabbits.
head_count = randint(1, 10)
# The number of legs is between twice and four times the number of heads and is an even number.
leg_count = randint(head_count, head_count * 2) * 2
head_ = 'head' if head_count == 1 else 'heads'
print(f'There are {head_count} {head_} and {leg_count} legs.')
# Input answer.
chicken_count = int(input_natural_number('How many chickens? '))
rabbit_count = int(input_natural_number('How many rabbits? '))
# Check answer.
correct_rabbit_count = leg_count // 2 - head_count
correct_chicken_count = head_count - correct_rabbit_count
if correct_rabbit_count == rabbit_count and correct_chicken_count == chicken_count:
    print('Correct!', end=' ')
else:
    print('Incorrect.', end=' ')
chicken_ = 'chicken' if correct_chicken_count == 1 else 'chickens'
rabbit_ = 'rabbit' if correct_rabbit_count == 1 else 'rabbits'
print(f'There are {correct_chicken_count} {chicken_} and {correct_rabbit_count} {rabbit_}.')

# Display the same number of chickens and rabbits as the correct answer.
root = tk.Tk()
root.title('Chickens and Rabbits in the Same Cage')
c = tk.Canvas(root, width=IMG_WIDTH * head_count, height=IMG_HEIGHT)
c.pack()
chicken_img = tk.PhotoImage(file='chicken.png')
rabbit_img = tk.PhotoImage(file='rabbit.png')
for i in range(head_count):
    if i < correct_chicken_count:
        c.create_image(i * IMG_WIDTH, 0, image=chicken_img, anchor='nw')
    else:
        c.create_image(i * IMG_WIDTH, 0, image=rabbit_img, anchor='nw')

root.mainloop()
