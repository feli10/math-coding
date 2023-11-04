"""画表盘

关于程序的几点说明：
1. 程序的计时功能使用了 tk 的 after()，它会在指定时间后触发一个事件。与常见的 sleep() 不同的是
   after() 不会阻碍程序主线程的运行。
2. 减小 root.after() 的参数值，可以加速指针转动。
3. 若要关闭绘制表盘的动画，将 draw_clock_dial() 移到 screen.tracer(0) 后面执行。
"""

import turtle


def draw_clock_dial():
    """画表盘。"""
    pen = turtle.Turtle()
    pen.speed(0)  # 加速 turtle 动画。
    pen.left(90)
    # 画表盘刻度。
    for i in range(60):
        if i % 5 == 0:
            length = 20
            pen.pensize(4)
        else:
            length = 10
            pen.pensize(2)
        pen.penup()
        pen.forward(300 - length)
        pen.pendown()
        pen.forward(length)
        pen.penup()
        pen.backward(300)
        pen.right(6)
    # 写表盘读数。
    for i in range(12):
        if i == 0:
            num = 12
        else:
            num = i
        pen.forward(230)
        pen.right(180 - i * 30)
        pen.forward(31)
        pen.write(num, align='center', font=('Arial', 60, 'normal'))
        pen.backward(31)
        pen.left(180 - i * 30)
        pen.backward(230)
        pen.right(30)
    # 画一个圆表示时钟的边框。
    pen.pensize(1)
    pen.pencolor('skyblue')
    pen.right(90)
    pen.forward(310)
    pen.left(90)
    pen.pendown()
    pen.circle(310)
    # 显示如何退出程序的提示文字。
    pen.penup()
    pen.home()
    pen.pencolor('black')
    pen.right(90)
    pen.forward(380)
    pen.write('按任意键或点击窗口退出...', align='center',
              font=('Arial', 24, 'normal'))
    pen.hideturtle()


def tick():
    """每一秒钟，三个指针转动一次。"""
    second.clear()
    second.forward(200)
    minute.clear()
    minute.forward(200)
    hour.clear()
    hour.forward(120)
    # 关闭 turtle 动画后，需要手动进行 turtle 的屏幕更新。
    screen.update()

    second.backward(200)
    # 秒针每秒顺时针旋转 6 度。
    second.right(6)
    minute.backward(200)
    # 分针每秒顺时针旋转 0.1 度。
    minute.right(0.1)
    hour.backward(120)
    # 时针每秒顺时针旋转 1/120 度。
    hour.right(1/120)
    # 等待 1 秒钟，再次调用 tick()。减小参数值以加速指针转动。
    root.after(1000, tick)


screen = turtle.Screen()
# 获取 turtle screen 底层的 tk root，以便可以使用 tk 的 after() 函数。该函数会在
# 指定时间后触发一个事件，并且不会阻碍程序主线程的运行。
canvas = screen.getcanvas()
root = canvas.master
# 监听键盘事件，按任意键退出。
screen.onkeypress(turtle.bye)
screen.listen()

# 创建秒针、分针和时针。
second = turtle.Turtle(visible=False)
second.pen(pencolor='red', pensize=2)
second.left(90)
minute = turtle.Turtle(visible=False)
minute.pen(pensize=4)
minute.left(90)
hour = turtle.Turtle(visible=False)
hour.pen(pensize=6)
hour.left(90)

# 若要关闭绘制表盘的动画，将 draw_clock_dial() 移到 screen.tracer(0) 后面执行。
draw_clock_dial()
# 关闭 turtle 动画。
screen.tracer(0)
tick()
turtle.exitonclick()
