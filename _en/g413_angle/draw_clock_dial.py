"""Draw clock dial

Some Useful Information:
1. The timing function uses tk's after(), which triggers an event after the specified time.
   Different from the commonly used time.sleep(), after() does not block the main thread of
   the program.
2. Reduce the parameter value in root.after() to speed up the clock.
3. To turn off the clock dial drawing animation, place draw_clock_dial() below screen.tracer(0). 
"""

import turtle


def draw_clock_dial():
    """Draw the clock dial."""
    pen = turtle.Turtle()
    pen.speed(0)  # Speed up the turtle.
    pen.left(90)
    # Draw scales.
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
    # Write numbers.
    for i in range(12):
        if i == 0:
            num = 12
        else:
            num = i
        pen.forward(230)
        pen.right(180 - i * 30)
        pen.forward(31)
        pen.write(num, align="center", font=("Arial", 60, "normal"))
        pen.backward(31)
        pen.left(180 - i * 30)
        pen.backward(230)
        pen.right(30)
    # Draw a circle as the clock border.
    pen.pensize(1)
    pen.pencolor('skyblue')
    pen.right(90)
    pen.forward(310)
    pen.left(90)
    pen.pendown()
    pen.circle(310)
    # Write a message of how to exit on the screen.
    pen.penup()
    pen.home()
    pen.pencolor('black')
    pen.right(90)
    pen.forward(380)
    pen.write("Press any key or click the mouse to exit...", align="center",
              font=("Arial", 24, "normal"))
    pen.hideturtle()


def tick():
    """The clock hands rotate for one second."""
    second.clear()
    second.forward(200)
    minute.clear()
    minute.forward(200)
    hour.clear()
    hour.forward(120)
    # Require manual turtle screen update when tracer is turned off.
    screen.update()

    second.backward(200)
    # The second hand rotates 6 degrees clockwise per second.
    second.right(6)
    minute.backward(200)
    # The minute hand rotates 0.1 degrees clockwise per second.
    minute.right(0.1)
    hour.backward(120)
    # The hour hand rotates 1/120 degrees clockwise per second.
    hour.right(1/120)
    # Wait for 1 second and call tick() again. Reduce the parameter value to speed up.
    root.after(1000, tick)


screen = turtle.Screen()
# Get tk root on which turtle screen is based to use tk's after() function which
# triggers an event after the specified time and does not block the main thread of the program.
canvas = screen.getcanvas()
root = canvas.master
# Press any key to exit.
screen.onkeypress(turtle.bye)
screen.listen()

# Create second, minute, and hour hand.
second = turtle.Turtle(visible=False)
second.pen(pencolor="red", pensize=2)
second.left(90)
minute = turtle.Turtle(visible=False)
minute.pen(pensize=4)
minute.left(90)
hour = turtle.Turtle(visible=False)
hour.pen(pensize=6)
hour.left(90)

# To turn off the clock dial drawing animation, place draw_clock_dial() below screen.tracer(0).
draw_clock_dial()
# Turn off turtle animation.
screen.tracer(0)
tick()
turtle.exitonclick()
