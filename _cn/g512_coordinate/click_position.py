"""坐标游戏 —— 根据坐标点击位置

关于程序的几点说明：
1. 游戏中的声音使用了 pygame 模块。pygame 不在 Python 标准库中，所以需要单独安装。在缺少 pygame 的情况下，
   把与声音有关的语句注释掉，也可以运行游戏。
"""

from random import randint
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from pygame import mixer


QUESTION_COUNT = 5
TIME_LIMIT = 20
UNIT = 60
MAX_COORD = 9
BORDER_LENGTH = UNIT * MAX_COORD
PADDING = 50
WIDTH = BORDER_LENGTH + PADDING * 2
HEIGHT = WIDTH
RADIUS = 15


def draw_coord():
    """绘制坐标系网格。"""
    start = PADDING
    end = PADDING + BORDER_LENGTH
    for i in range(MAX_COORD + 1):
        pos = PADDING + UNIT * i
        canvas.create_line(start, pos, end, pos)
        if i != MAX_COORD:
            canvas.create_text(start - 10, pos, text=str(MAX_COORD - i), font=font20)
        canvas.create_line(pos, start, pos, end)
        canvas.create_text(pos, end + 10, text=str(i), font=font20)


def new_question():
    """生成一组新的坐标数对。"""
    canvas.x = randint(0, MAX_COORD)
    canvas.y = randint(0, MAX_COORD)
    value_coord.set(f'({canvas.x}, {canvas.y})')
    canvas.count += 1
    value_count.set(f'{canvas.count}/{QUESTION_COUNT}')


def timer():
    """计时器。"""
    canvas.time -= 1
    value_time.set(canvas.time)
    if canvas.time == 0:
        over("时间到！")
    else:
        canvas.timer = root.after(1000, timer)


def to_canvas_coord(x, y):
    """把游戏坐标转换为 Tk Canvas 的绘图坐标。
    
    x, y: 游戏坐标。
    """
    canvas_x = PADDING + UNIT * x
    canvas_y = PADDING + UNIT * (MAX_COORD - y)
    return canvas_x, canvas_y


def draw_circle(x, y, color):
    """在鼠标点击的位置画一个反馈圆圈。

    x, y: 鼠标点击位置所对应的游戏坐标。
    color: 'green' 或 'red'，绿色或红色分别代表点对或点错。 
    """
    x, y = to_canvas_coord(x, y)
    circle = canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS,
                           fill=color, width=0)
    root.after(500, lambda: canvas.delete(circle))


def click(e):
    """鼠标点击事件的响应函数。
    
    e: 系统自动传给响应函数的事件参数。
    """
    shortest_distance_squared = RADIUS ** 2
    for i in range(MAX_COORD + 1):
        for j in range(MAX_COORD + 1):
            canvas_x, canvas_y = to_canvas_coord(i, j)
            distance_squared = (e.x - canvas_x) ** 2 + (e.y - canvas_y) ** 2
            if distance_squared < shortest_distance_squared:
                shortest_distance_squared = distance_squared
                x, y  = i, j
    if shortest_distance_squared == RADIUS ** 2:
        return
    if x == canvas.x and y == canvas.y:
        draw_circle(x, y, 'green')
        correct_sound.play()
        if canvas.count < QUESTION_COUNT:
            new_question()
        else:
            over('好样的！')
    else:
        draw_circle(x, y, 'red')
        wrong_sound.play()


def start():
    """开始一局游戏。"""
    canvas.time = TIME_LIMIT
    value_time.set(canvas.time)
    canvas.count = 0
    new_question()
    canvas.timer = root.after(1000, timer)


def over(result):
    """处理游戏结束。

    result: 反馈字符串 "时间到！" 或 "好样的！"。
    """
    root.after_cancel(canvas.timer)
    root.update_idletasks()
    if messagebox.askyesno('', f'{result}再来一局吗？'):
        start()
    else:
        root.destroy()


# 设置游戏中用到的声音。
mixer.init()
correct_sound = mixer.Sound('correct.mp3')
wrong_sound = mixer.Sound('wrong.mp3')

root = tk.Tk()
root.title('坐标游戏')
font20 = tkfont.Font(size=20)
font40 = tkfont.Font(size=40)
value_time = tk.StringVar()
value_count = tk.StringVar()
value_coord = tk.StringVar()

# 窗口布局，从上至下依次是  frame, canvas 和 label_coord。
frame = tk.Frame(root)
frame.pack(fill='x', padx=PADDING, pady=10)
label_time = tk.Label(frame, textvariable=value_time, font=font40)
label_time.pack(side='left')
label_count = tk.Label(frame, textvariable=value_count, font=font40)
label_count.pack(side='right')

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind('<Button-1>', click)

label_coord = tk.Label(root, textvariable=value_coord, font=font40)
label_coord.pack(pady=10)

draw_coord()
start()

root.mainloop()
