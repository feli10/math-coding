"""鸡兔同笼"""

from random import randint
import tkinter as tk
import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number


IMG_WIDTH = 155
IMG_HEIGHT = 200

# 随机生成一道鸡兔同笼题。
head_count = randint(1, 10)
# 生成腿数时，腿数介于头数的 2 倍到 4 倍之间，且为偶数。
leg_count = randint(head_count, head_count * 2) * 2
print(f'从上面数，有 {head_count} 个头，从下面数，有 {leg_count} 只脚。')
# 输入答案。
chicken_count = int(input_natural_number('有多少只鸡? '))
rabbit_count = int(input_natural_number('有多少只兔子? '))
# 检查答案。
correct_rabbit_count = leg_count // 2 - head_count
correct_chicken_count = head_count - correct_rabbit_count
if correct_rabbit_count == rabbit_count and correct_chicken_count == chicken_count:
    print('正确！', end='')
else:
    print('回答有误。', end='')
print(f'笼中有 {correct_chicken_count} 只鸡，{correct_rabbit_count} 只兔子。')

# 显示同正确答案数量的鸡和兔子的图片。
root = tk.Tk()
root.title('鸡兔同笼')
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
