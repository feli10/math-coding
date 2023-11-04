"""坐标游戏 —— 根据位置输入坐标

关于程序的几点说明：
1. 输入坐标时，可以使用鼠标或 TAB 键切换 X、Y 坐标输入框和发射按钮的焦点。为了加快发射速度，程序为坐标输入设置
   了键盘快捷键：在 X 输入框内按 RETURN 键可以切换焦点到 Y 输入框，再次按 RETURN 键发射。
2. 游戏中的声音使用了 pygame 模块。pygame 不在 Python 标准库中，所以需要单独安装。在缺少 pygame 的情况下，
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
PADDING = 50
BORDER_LENGTH = UNIT * MAX_COORD
WIDTH = BORDER_LENGTH + PADDING * 2
HEIGHT = WIDTH


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


def place_rocket():
    """生成一个新的位置放置火箭。"""
    canvas.x = randint(0, MAX_COORD)
    canvas.y = randint(0, MAX_COORD)
    canvas.coords(rocket, PADDING + UNIT * canvas.x, PADDING + UNIT * (MAX_COORD - canvas.y))
    canvas.itemconfig(rocket, state=tk.NORMAL)


def timer():
    """计时器。"""
    canvas.time -= 1
    value_time.set(canvas.time)
    if canvas.time == 0:
        over("时间到！")
    else:
        canvas.timer = root.after(1000, timer)


def submit():
    """按钮点击事件响应函数。"""
    # 获取有效输入的坐标。
    x = entry_x.get().strip()
    if not x.isdecimal() or int(x) > MAX_COORD:
        entry_x.focus_set()
        return
    y = entry_y.get().strip()
    if not y.isdecimal() or int(y) > MAX_COORD:
        entry_y.focus_set()
        return
    x, y = int(x), int(y)
    # 在与输入坐标对应的位置显示爆炸。
    canvas.coords(explosion, PADDING + UNIT * x, PADDING + UNIT * (MAX_COORD - y))
    canvas.itemconfig(explosion, state=tk.NORMAL)
    root.after(500, lambda: canvas.itemconfig(explosion, state=tk.HIDDEN))
    explosion_sound.play()
    # 检验输入的坐标与火箭坐标是否一致。
    if x == canvas.x and y == canvas.y:
        if canvas.count == QUESTION_COUNT:
            canvas.itemconfig(rocket, state=tk.HIDDEN)
            over('好样的！')
            return
        place_rocket()
        canvas.count += 1
        value_count.set(f'{canvas.count}/{QUESTION_COUNT}')
    value_x.set('')
    value_y.set('')
    entry_x.focus_set()


def start():
    """开始一局游戏。"""
    canvas.itemconfig(explosion, state=tk.HIDDEN)
    place_rocket()
    canvas.time = TIME_LIMIT
    canvas.count = 1
    value_time.set(canvas.time)
    value_count.set(f'{canvas.count}/{QUESTION_COUNT}')
    value_x.set('')
    value_y.set('')
    entry_x.focus_set()
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


# 设置爆炸声音。
mixer.init()
explosion_sound = mixer.Sound('explosion.mp3')
explosion_sound.set_volume(0.2)

root = tk.Tk()
root.title('坐标游戏')
font20 = tkfont.Font(size=20)
font40 = tkfont.Font(size=40)
value_time = tk.StringVar()
value_count = tk.StringVar()
value_x = tk.StringVar()
value_y = tk.StringVar()

# 窗口布局，从上至下依次是 frame1, canvas 和 frame2。
frame1 = tk.Frame(root)
frame1.pack(fill='x', padx=PADDING, pady=10)
label_time = tk.Label(frame1, textvariable=value_time, font=font40)
label_time.pack(side='left')
label_count = tk.Label(frame1, textvariable=value_count, font=font40)
label_count.pack(side='right')

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
rocket_img = tk.PhotoImage(file='rocket.png')
explosion_img = tk.PhotoImage(file='explosion.png')
rocket = canvas.create_image(0, 0, image=rocket_img, state=tk.HIDDEN)
explosion = canvas.create_image(0, 0, image=explosion_img, state=tk.HIDDEN)

frame2 = tk.Frame(root)
frame2.pack(pady=10)
# frame2 内从左至右依次是 label_x, entry_x, label_y, entry_y 和 button。
label_x = tk.Label(frame2, text='X:', font=font20)
label_x.pack(side='left')
entry_x = tk.Entry(frame2, textvariable=value_x, width=2, font=font20)
entry_x.pack(side='left')
label_y = tk.Label(frame2, text='Y:', font=font20)
label_y.pack(side='left')
entry_y = tk.Entry(frame2, textvariable=value_y, width=2, font=font20)
entry_y.pack(side='left')
button = tk.Button(frame2, text='发射', font=font20, highlightthickness=3, command=submit)
button.pack(side='left')
# 设置键盘快捷键以加快输入坐标的速度。
entry_x.bind('<Return>', lambda e: entry_y.focus_set())
entry_y.bind('<Return>', lambda e: button.invoke())

draw_coord()
start()

root.mainloop()
