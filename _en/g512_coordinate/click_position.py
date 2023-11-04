"""Coordinate Game - Click position based on coordinates

Some Useful Information:
1. Game sound uses the pygame module. pygame isn't in the Python standard library, so it needs
   to be installed separately. If you don't install pygame, you can also run the game with all
   sound-related statements commented out.
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
    """Draw coordinate system."""
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
    """Generate a pair of new coordinates."""
    canvas.x = randint(0, MAX_COORD)
    canvas.y = randint(0, MAX_COORD)
    value_coord.set(f'({canvas.x}, {canvas.y})')
    canvas.count += 1
    value_count.set(f'{canvas.count}/{QUESTION_COUNT}')


def timer():
    """Timer."""
    canvas.time -= 1
    value_time.set(canvas.time)
    if canvas.time == 0:
        over("Time's Up!")
    else:
        canvas.timer = root.after(1000, timer)


def to_canvas_coord(x, y):
    """Convert game coordinates to actual canvas coordinates.
    
    x, y: game coordinates.
    """
    canvas_x = PADDING + UNIT * x
    canvas_y = PADDING + UNIT * (MAX_COORD - y)
    return canvas_x, canvas_y


def draw_circle(x, y, color):
    """Draw a feedback circle at the positon the mouse clicked.

    x, y: game coodinates corresponding to the position the mouse clicked.
    color: 'green' or 'red' representing right or wrong. 
    """
    x, y = to_canvas_coord(x, y)
    circle = canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS,
                           fill=color, width=0)
    root.after(500, lambda: canvas.delete(circle))


def click(e):
    """Handler for mouse click events.
    
    e: the event detail sent by system.
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
            over('Good Job!')
    else:
        draw_circle(x, y, 'red')
        wrong_sound.play()


def start():
    """Start a new game."""
    canvas.time = TIME_LIMIT
    value_time.set(canvas.time)
    canvas.count = 0
    new_question()
    canvas.timer = root.after(1000, timer)


def over(result):
    """Handle game over.

    result: feedback string "Time's Up!" or "Good Job!".
    """
    root.after_cancel(canvas.timer)
    root.update_idletasks()
    if messagebox.askyesno('', f'{result} Play Again?'):
        start()
    else:
        root.destroy()


# Initiate sounds used in the game.
mixer.init()
correct_sound = mixer.Sound('correct.mp3')
wrong_sound = mixer.Sound('wrong.mp3')

root = tk.Tk()
root.title('Coordinate Game')
font20 = tkfont.Font(size=20)
font40 = tkfont.Font(size=40)
value_time = tk.StringVar()
value_count = tk.StringVar()
value_coord = tk.StringVar()

# Layout: from top to bottom within root are frame, canvas, and label_coord.
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
