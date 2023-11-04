"""表盘时钟

关于程序的几点说明：
1. 时钟使用 time.sleep() 函数进行计时。
2. 时钟程序采用无限循环结构，按任意键或点击按钮退出（未使用多线程，所以响应会有一点滞后）。
3. 程序使用 turtle 模块绘制时钟， 使用 tkinter 模块创建退出按钮。
"""

import turtle
import tkinter as tk
import tkinter.font as tkfont
from time import sleep


# 设置一个用于退出无限循环的全局变量。
running = True


def stop():
    """退出程序。"""
    global running
    running = False
    print('程序结束!')


screen = turtle.Screen()
# 放置表盘图片作为背景。
screen.bgpic('clock.gif')
# 关闭 turtle 动画。
screen.tracer(0)

# 显示如何退出程序的提示文字。
message = turtle.Turtle(visible=False)
message.penup()
message.right(90)
message.forward(380)
message.write('按任意键或点击按钮退出...', align='center', font=('Arial', 30, 'normal'))

# 在 turtle 底层的 tkinter 上创建退出按钮。（turtle 本身就是建立在 tkinter 的 canvas 之上的。）
canvas = screen.getcanvas()
button = tk.Button(canvas.master, text='退出', command=stop, font=tkfont.Font(size=32))
# 把按钮放在 canvas 内，或放在 canvas 下面。（二选一）
canvas.create_window(400, 360, window=button)  # 放在 canvas 内。
# button.pack(pady=20)  # 放在 canvas 下面。

# 监听键盘事件，按任意键退出。
screen.onkeypress(stop)
screen.listen()

# 创建秒针、分针和时针。
second = turtle.Turtle(visible=False)
second.pencolor('red')
second.pensize(2)
second.left(90)

minute = turtle.Turtle(visible=False)
minute.pensize(4)
minute.left(90)

hour = turtle.Turtle(visible=False)
hour.pensize(6)
hour.left(90)

# 使用 try/except 避免在程序运行中（无限循环）直接关闭窗口退出时弹出的错误信息。
try:
    while running:
        second.clear()
        minute.clear()
        hour.clear()
        second.forward(200)
        minute.forward(200)
        hour.forward(120)

        # 关闭 turtle 动画后，需要手动进行 turtle 的屏幕更新。
        screen.update()
        # 等待 1 秒钟。 减小等待时间或注释掉下面一行，可使时钟加速运转。
        sleep(1)

        second.goto(0, 0)
        minute.goto(0, 0)
        hour.goto(0, 0)
        # 秒针每秒顺时针旋转 6 度。
        second.right(6)
        # 分针每秒顺时针旋转 0.1 度。
        minute.right(0.1)
        # 时针每秒顺时针旋转 1/120 度。
        hour.right(1/120)
except tk.TclError:
    print('程序结束!')
