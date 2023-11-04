"""辨认方向练习

关于程序的几点说明：
1. 在练习辨认方向时，为了增加一些紧迫感和趣味性，程序为答题添加了时间限制。
   用户可以设置 TIME_LIMIT, 或让 HAVE_TIME_LIMIT = False 关闭限时功能。
2. 程序的计时功能使用了 tk 的 after()，它会在指定时间后触发一个事件。
   与常见的 sleep() 不同的是 after() 不会阻碍程序主线程的运行。
3. TIME_LIMIT 的单位是秒, after() 时间参数的单位是毫秒。
"""

import turtle
import tkinter as tk
import tkinter.font as tkfont
from random import randint


QUESTION_COUNT = 10
HAVE_TIME_LIMIT = True
TIME_LIMIT = 4
ORIENTATIONS = ['东', '西', '南', '北', '东南', '西南', '东北', '西北']
ANGLES = [0, 180, -90, 90, -45, -135, 45, 135]


class Data():
    """定义在各函数间共享的程序数据。
    
    属性
    ----
    count: 当前是第几道题。
    orientation: 当前箭头指向的方向，由一个 0-7 之间的数代表。
    correct_count: 已答对题目的数量。
    can_answer: 是否处于用户可以点击按钮回答问题的阶段。
    """
    def __init__(self):
        """初始化程序数据。"""
        self.count = 0
        self.orientation = 0
        self.correct_count = 0
        self.can_answer = False

    def reset(self):
        """重新初始化程序数据，开始新的一局。"""
        self.__init__()


data = Data()

# 准备图形用户界面。
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
# 获取 turtle screen 底层的 tk canvas。
canvas = screen.getcanvas()
# 通过 tk canvas 获取 tk root。
root = canvas.master
# 在 Canvas 下方创建 8 个 tk 按钮。
for i in range(8):
    button = tk.Button(root, text=ORIENTATIONS[i],
                        command=lambda t=i: check_answer(t), font=tkfont.Font(size=20))
    button.pack(side='left', expand=True, fill='x', pady=10)

pointer = turtle.Turtle()


def new_question():
    """生成一道新方向问题。"""
    data.count += 1
    data.orientation = randint(0, 7)
    pointer.reset()
    pointer.pensize(3)
    pointer.shapesize(2)
    pointer.left(ANGLES[data.orientation])
    pointer.forward(200)
    data.can_answer = True
    if HAVE_TIME_LIMIT:
        # 启动一个计时器，创建一个指向该定时器的类变量 tk.after_id，
        # 使用类变量而不是局部变量，是为了可以在其它函数中访问该变量。
        tk.after_id = root.after(TIME_LIMIT * 1000, timeout)


def timeout():
    """处理超时。"""
    data.can_answer = False
    tk.messagebox.showwarning(title='超时', message=
                                f'正确答案是{ORIENTATIONS[data.orientation]}。')
    manager()


def check_answer(answer):
    """当按钮被按下时检查答案。"""
    if data.can_answer:
        data.can_answer = False
        # 取消这道题的计数器。
        root.after_cancel(tk.after_id)
        if data.orientation == answer:
            data.correct_count += 1
        else:
            tk.messagebox.showerror(title='错误', message=
                                    f'正确答案是{ORIENTATIONS[data.orientation]}。'
                                    + f'\n（你点击了{ORIENTATIONS[answer]}）')
        manager()


def manager():
    """管理整个程序进程。"""
    if data.count == QUESTION_COUNT:
        result = tk.messagebox.askyesno(title='完成', message=
                                        f'你在 {QUESTION_COUNT} 道题中答对了 {data.correct_count} 道题。'
                                        '\n再来一局吗？')
        # 点击 "Yes" 按钮，消息框返回 True。
        if result:
            # 开始新的一局。
            data.reset()
            new_question()
        else:
            # 结束程序。
            turtle.bye()
    else:
        new_question()


new_question()
turtle.mainloop()
