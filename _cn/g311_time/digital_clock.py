"""数字时钟计时器

关于程序的几点说明：
1. 时钟使用 time.sleep() 函数进行计时。
2. 程序会在计时器到时或按下 Ctrl-C 键时终止。
"""

from time import sleep


second = 0
minute = 0
hour = 0

# 用于计时功能。
total_sec = 0
timer = int(input('请输入计时器时间长度（单位秒）: '))

# 加入 end='\r' 可以在同一行内更新数字时钟的显示。
print('00:00:00', end='\r')
# 使用 try/except 捕捉按下 Ctrl-C 键所引起的程序中断。
try:
    while True:
        # 等待 1 秒钟。可以减小等待时间以更快看到分钟和小时数的变化，例如 0.01 秒。
        sleep(0.1)
        second += 1
        if second == 60:
            second = 0
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1
                if hour == 24:
                    hour = 0
        # 更新数字时钟的显示。
        print(f'{hour:0>2d}:{minute:0>2d}:{second:0>2d}', end='\r')

        # 用于计时功能。
        total_sec += 1
        if total_sec == timer:
            print('\n计时器时间到!')
            break
except KeyboardInterrupt:
    print('\n退出计时!')
