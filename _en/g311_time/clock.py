"""An analog clock with a dial

Some Useful Information:
1. The clock uses time.sleep() function for timing.
2. The program is in an infinite loop. Press any key or click Exit button to exit
   (there will be a little lag in response since the program doesn't use multithreading).
3. The program uses turtle module to draw the clock and tk module to create Exit button.
"""

import turtle
import tkinter as tk
import tkinter.font as tkfont
from time import sleep


# Set a global variable for breaking the inifinite loop.
running = True


def stop():
    """Stop the program."""
    global running
    running = False
    print('Stopped!')


screen = turtle.Screen()
# Use a dial image as background.
screen.bgpic('clock.gif')
# Turn off turtle animation.
screen.tracer(0)

# Write a message of how to exit on the screen.
message = turtle.Turtle(visible=False)
message.penup()
message.right(90)
message.forward(380)
message.write('Press any key or click the button to exit...', align='center',
              font=('Arial', 30, 'normal'))

# Create an exit button using the underlying tk infrastructure of turtle module.
canvas = screen.getcanvas()
button = tk.Button(canvas.master, text='Exit', command=stop, font=tkfont.Font(size=32))
# Put the button on or under the tk canvas.
canvas.create_window(400, 360, window=button)  # On the canvas.
# button.pack(pady=20)  # Under the canvas.

# Create a key press event (press any key to exit).
screen.onkeypress(stop)
screen.listen()

# Create second, minute, and hour hand.
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

# Use try/except to avoid error message if the user directly close the window
# while the program is still running in an infinite loop.
try:
    while running:
        second.clear()
        minute.clear()
        hour.clear()
        second.forward(200)
        minute.forward(200)
        hour.forward(120)

        # Require manual turtle screen update when tracer is turned off.
        screen.update()
        # Wait for 1 second. Ruduce the value or comment out the line to speed up.
        sleep(1)

        second.goto(0, 0)
        minute.goto(0, 0)
        hour.goto(0, 0)
        # The second hand rotates 6 degrees clockwise per second.
        second.right(6)
        # The minute hand rotates 0.1 degrees clockwise per second.
        minute.right(0.1)
        # The hour hand rotates 1/120 degrees clockwise per second.
        hour.right(1/120)
except tk.TclError:
    print('Stopped!')
