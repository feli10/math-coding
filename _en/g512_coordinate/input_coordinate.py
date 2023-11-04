"""Coordinate Game - Input coordinates based on position

Some Useful Information:
1. You can use mouse or TAB key to change focus when inputting and submitting coordinates, but
   the fastest way is pressing RETURN in entry_x to change focus to entry_y and pressing RETURN
   again to submit.
2. Game sound uses the pygame module. pygame isn't in the Python standard library, so it needs
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
PADDING = 50
BORDER_LENGTH = UNIT * MAX_COORD
WIDTH = BORDER_LENGTH + PADDING * 2
HEIGHT = WIDTH


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


def place_rocket():
    """Generate a new position to place a rocket."""
    canvas.x = randint(0, MAX_COORD)
    canvas.y = randint(0, MAX_COORD)
    canvas.coords(rocket, PADDING + UNIT * canvas.x, PADDING + UNIT * (MAX_COORD - canvas.y))
    canvas.itemconfig(rocket, state=tk.NORMAL)


def timer():
    """Timer."""
    canvas.time -= 1
    value_time.set(canvas.time)
    if canvas.time == 0:
        over("Time's Up!")
    else:
        canvas.timer = root.after(1000, timer)


def submit():
    """Handler for button click event."""
    # Get input coordinates that are valid.
    x = entry_x.get().strip()
    if not x.isdecimal() or int(x) > MAX_COORD:
        entry_x.focus_set()
        return
    y = entry_y.get().strip()
    if not y.isdecimal() or int(y) > MAX_COORD:
        entry_y.focus_set()
        return
    x, y = int(x), int(y)
    # Display explosion at the corresponding position of the coordinates.
    canvas.coords(explosion, PADDING + UNIT * x, PADDING + UNIT * (MAX_COORD - y))
    canvas.itemconfig(explosion, state=tk.NORMAL)
    root.after(500, lambda: canvas.itemconfig(explosion, state=tk.HIDDEN))
    explosion_sound.play()
    # Check if the coordinates are the same as the rocket's.
    if x == canvas.x and y == canvas.y:
        if canvas.count == QUESTION_COUNT:
            canvas.itemconfig(rocket, state=tk.HIDDEN)
            over('Good Job!')
            return
        place_rocket()
        canvas.count += 1
        value_count.set(f'{canvas.count}/{QUESTION_COUNT}')
    value_x.set('')
    value_y.set('')
    entry_x.focus_set()


def start():
    """Start a new game."""
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
    """Handle game over.

    result: feedback string "Time's Up!" or "Good Job!".
    """
    root.after_cancel(canvas.timer)
    root.update_idletasks()
    if messagebox.askyesno('', f'{result} Play Again?'):
        start()
    else:
        root.destroy()


# Initiate explosion sound.
mixer.init()
explosion_sound = mixer.Sound('explosion.mp3')
explosion_sound.set_volume(0.2)

root = tk.Tk()
root.title('Coordinate Game')
font20 = tkfont.Font(size=20)
font40 = tkfont.Font(size=40)
value_time = tk.StringVar()
value_count = tk.StringVar()
value_x = tk.StringVar()
value_y = tk.StringVar()

# Layout: from top to bottom within root are frame1, canvas, and frame2.
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
# From left to right within frame2 are label_x, entry_x, label_y, entry_y, and button.
label_x = tk.Label(frame2, text='X:', font=font20)
label_x.pack(side='left')
entry_x = tk.Entry(frame2, textvariable=value_x, width=2, font=font20)
entry_x.pack(side='left')
label_y = tk.Label(frame2, text='Y:', font=font20)
label_y.pack(side='left')
entry_y = tk.Entry(frame2, textvariable=value_y, width=2, font=font20)
entry_y.pack(side='left')
button = tk.Button(frame2, text='Fire', font=font20, highlightthickness=3, command=submit)
button.pack(side='left')
# Set keyboard shortcuts to speed up the input process.
entry_x.bind('<Return>', lambda e: entry_y.focus_set())
entry_y.bind('<Return>', lambda e: button.invoke())

draw_coord()
start()

root.mainloop()
