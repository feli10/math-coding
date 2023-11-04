"""A digital clock with timer

Some Useful Information:
1. The clock uses time.sleep() function for timing.
2. The program will end when the time is up or Ctrl-C is pressed.
"""

from time import sleep


second = 0
minute = 0
hour = 0

# Code for timer.
total_sec = 0
timer = int(input('Please set a timer (in seconds): '))

# Use end='\r' to update the digital clock at the same line.
print('00:00:00', end='\r')
# Use try/except to catch KeyboardInterrupt caused by pressing Ctrl-C.
try:
    while True:
        # Wait for 1 second. Reduce the value to speed up to see change in the minute and
        # hour values.
        sleep(1)
        second += 1
        if second == 60:
            second = 0
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1
                if hour == 24:
                    hour = 0
        # Update the digital clock.
        print(f'{hour:0>2d}:{minute:0>2d}:{second:0>2d}', end='\r')

        # Code for timer.
        total_sec += 1
        if total_sec == timer:
            print('\nTime is up!')
            break
except KeyboardInterrupt:
    print('\nStopped!')
