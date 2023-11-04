"""列方程求解鸡兔同笼问题"""

import sys
from pathlib import Path
# 把上级目录添加到模块搜索路径，以便引用其它项目模块。
sys.path.append(str(Path(__file__).parents[1]))
from common import input_natural_number

while True:
    head_count = int(input_natural_number('从上面数，有多少个头? '))
    leg_count = int(input_natural_number('从下面数，有多少只脚? '))
    if leg_count % 2 == 0 and head_count * 2 <= leg_count <= head_count * 4:
        break
    print('输入不合理，脚必须是偶数，且介于头数的二到四倍之间，请重新输入。\n')

print(f'\n解：设有 x 只兔子，则有 {head_count} - x 只鸡。\n')

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
print(f'\n    鸡：{head_count} - {rabbit_count} = {chicken_count} (只)')

print(f'\n答：有 {chicken_count} 只鸡，{rabbit_count} 只兔子。\n')
