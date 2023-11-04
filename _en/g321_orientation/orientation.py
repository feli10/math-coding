"""Generate orientation questions with time limits.

Some Useful Information:
1. The program sets a time limit for answering questions in order to add some urgency and fun.
   You can set the time limit through TIME_LIMIT or turn it off by setting HAVE_TIME_LIMIT to False.
2. The timing function uses tk's after(), which triggers an event after the specified time.
   Different from the commonly used time.sleep(), after() does not block the main thread of
   the program.
3. The unit of TIME_LIMIT is seconds, and the unit of the after() time parameter is milliseconds.
"""

import turtle
import tkinter as tk
import tkinter.font as tkfont
from random import randint


QUESTION_COUNT = 10
HAVE_TIME_LIMIT = True
TIME_LIMIT = 4
ORIENTATIONS = ['North', 'South', 'East', 'West',
                'Northeast', 'Northwest', 'Southeast', 'Southwest']
ANGLES = [90, -90, 0, 180, 45, 135, -45, -135]


class Data():
    """Define data shared between various functions of the program.
    
    Attributes
    ----------
    count: current question number.
    orientation: current orientation represented by a number between 0-7.
    correct_count: number of questions answered correctly.
    can_answer: whether it is ready for user to answer the question.
    """
    def __init__(self):
        """Initialize instance variables."""
        self.count = 0
        self.orientation = 0
        self.correct_count = 0
        self.can_answer = False

    def reset(self):
        """Reset instance variables for starting another round."""
        self.__init__()


data = Data()

# Prepare graphic user interface.
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
# Get tk canvas on which turtle screen is based.
canvas = screen.getcanvas()
# Get tk root through tk canvas.
root = canvas.master
# Create 8 tk buttons below the canvas.
for i in range(8):
    button = tk.Button(root, text=ORIENTATIONS[i],
                        command=lambda t=i: check_answer(t), font=tkfont.Font(size=20))
    button.pack(side='left', expand=True, fill='x', pady=10)

pointer = turtle.Turtle()


def new_question():
    """Generate a new question."""
    data.count += 1
    data.orientation = randint(0, 7)
    pointer.reset()
    pointer.pensize(3)
    pointer.shapesize(2)
    pointer.left(ANGLES[data.orientation])
    pointer.forward(200)
    data.can_answer = True
    if HAVE_TIME_LIMIT:
        # Start a timer for the question and create the class variable tk.after_id as its reference
        # instead of a local variable so that it can be accessed in another function.
        tk.after_id = root.after(TIME_LIMIT * 1000, timeout)


def timeout():
    """Handle timeouts."""
    data.can_answer = False
    tk.messagebox.showwarning(title='Timeout', message=
                                f'The correct answer is {ORIENTATIONS[data.orientation]}.')
    manager()


def check_answer(answer):
    """Check answer when button is clicked."""
    if data.can_answer:
        data.can_answer = False
        # Cancel the timer for this question.
        root.after_cancel(tk.after_id)
        if data.orientation == answer:
            data.correct_count += 1
        else:
            tk.messagebox.showerror(title='Incorrect', message=
                                    f'The correct answer is {ORIENTATIONS[data.orientation]}.'
                                    + f'\n(You clicked {ORIENTATIONS[answer]})')
        manager()


def manager():
    """Manage the process of the program."""
    if data.count == QUESTION_COUNT:
        result = tk.messagebox.askyesno(title='Finish', message=
                                        f'You answered {data.correct_count} out of {QUESTION_COUNT}'
                                        ' questions correctly.\nDo you want to try again?')
        # Messagebox returns True if "Yes" button is clicked.
        if result:
            # Start another round.
            data.reset()
            new_question()
        else:
            # End the program.
            turtle.bye()
    else:
        new_question()


new_question()
turtle.mainloop()
