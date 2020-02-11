import turtle
import time
import random

# The X-wing
def drawingXWing(xwing):
    # create body of the xwing
    xwing.begin_poly()
    xwing.hideturtle()
    xwing.penup()
    xwing.speed(0)
    xwing.color("Yellow")
    xwing.left(90);

    xwing.forward(15)

    xwing.left(90)
    xwing.forward(60)

    xwing.right(90)
    xwing.forward(20)

    xwing.right(90)
    xwing.forward(30)
    xwing.left(90)
    xwing.forward(10)

    xwing.left(90)
    xwing.forward(60)

    xwing.left(90)
    xwing.forward(15)
    xwing.setheading(180)
    xwing.forward(10)
    xwing.left(90)
    xwing.forward(20)
    xwing.left(90)
    xwing.forward(10)
    xwing.right(90)

    # Right wing
    xwing.forward(20)
    xwing.right(90)
    xwing.forward(10)
    xwing.left(90)
    xwing.forward(20)
    xwing.left(90)
    xwing.forward(10)
    xwing.right(90)
    xwing.forward(10)

    xwing.setheading(0)
    xwing.forward(60)
    xwing.left(90)
    xwing.forward(10)
    xwing.left(90)
    xwing.forward(30)
    xwing.right(90)
    xwing.forward(20)
    xwing.right(90)
    xwing.forward(60)
    xwing.left(90)
    xwing.forward(10)
    xwing.setheading(0)
    xwing.showturtle()
    xwing.end_poly()

    p = xwing.get_poly()
    s = turtle.Shape("compound")
    s.addcomponent(p, "cyan", "black")
    turtle.register_shape("xwingAdvanced", s)
    xwing.shape("xwingAdvanced")

    return xwing

# The Tie
def drawingTIE(tie):
    # create body of the tie
    tie.begin_poly()

    tie.penup()
    tie.hideturtle()
    tie.speed(0)
    tie.color("Green")
    tie.left(90);
    tie.circle(30, 60)
    tie.right(45)
    tie.forward(30)

    tie.right(105)
    tie.forward(30)

    tie.left(90)
    tie.forward(20)
    tie.left(90)
    tie.forward(74.47)

    tie.left(90)
    tie.forward(20)
    tie.left(90)
    tie.forward(30)

    tie.right(105)
    tie.forward(30)

    tie.right(45)
    # tie.setheading(210)
    tie.circle(30, 120)

    # Right wing
    tie.right(45)
    tie.forward(30)

    tie.setheading(180)
    tie.forward(30)

    tie.left(90)
    tie.forward(20)
    tie.left(90)
    tie.forward(74.47)

    tie.left(90)
    tie.forward(20)
    tie.left(90)
    tie.forward(30)
    tie.right(105)
    tie.forward(30)

    tie.right(45)
    tie.circle(30, 60)
    tie.setheading(0)
    tie.showturtle()
    tie.end_poly()

    t = tie.get_poly()
    sh = turtle.Shape("compound")
    sh.addcomponent(t, "black", "black")
    turtle.register_shape("TieAdvanced", sh)
    tie.shape("TieAdvanced")

    return tie


# Setup screen
win = turtle.Screen()
win.title("Star Wars")
win.bgcolor("pink")
win.setup(width=1000, height=700)
win.tracer(0)

# Create the TIE Fighter
turtle.mode("logo")
tie = turtle.Turtle()
tie = drawingTIE(tie)
tie.penup()
turtle.right(90)
tie.speed(3)

# Creating the X-Wing
xwing = turtle.Turtle()
xwing = drawingXWing(xwing)
xwing.penup()
xwing.speed(6)

def turn_left():
    xwing.left(10)
    # xwing.left(5)
    # xwing.left(5)
def turn_right():
    xwing.right(10)

def go_forward():
    xwing.forward(10)
    # xwing.forward(2)
    # xwing.forward(2)
def go_backward():
    xwing.backward(10)

def shoot(x, y):
    cannon = turtle.Turtle()
    cannon.color("red")
    cannon.pensize(7)
    cannon.penup()
    cannon.goto(xwing.position())
    cannon.pendown()
    cannon.setheading(xwing.heading())
    cannon.forward(1250)

    # cannon.undo()
    # cannon.clear()


while True:
    win.update()
    # win.clear()
    # tie.forward(10)
    # tie.right(10)

    # Keyboard bindings
    win.onkeypress(turn_left, "q")
    win.onkeyrelease(None, "q")
    win.listen()

    win.onkeypress(turn_right, "r")
    win.onkeyrelease(None, "r")
    win.listen()

    win.onkeypress(go_forward, "w")
    win.onkeyrelease(None, "w")
    win.listen()
    # win.onkey(go_forward, "Up")
    win.onkeypress(go_backward, "s")
    win.onkeyrelease(None, "s")
    win.listen()

    win.onscreenclick(shoot, 1)
    win.listen()
    #time.sleep(0.1)

turtle.done()
