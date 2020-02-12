import turtle
import time
import random

tiecolors = ["black", "brown", "Light Gray"]

class TIE(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color(tiecolors[2], tiecolors[0])

    def drawing_tie(self):
        # create body of the tie
        self.begin_poly()
        self.penup()
        self.hideturtle()

        self.speed(0)
        self.left(90);
        self.circle(30, 60)
        self.right(45)
        self.forward(30)

        self.right(105)
        self.forward(30)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(74.47)

        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(30)

        self.right(105)
        self.forward(30)

        self.right(45)
        # self.setheading(210)
        self.circle(30, 120)

        # Right wing
        self.right(45)
        self.forward(30)

        self.setheading(180)
        self.forward(30)

        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(74.47)

        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(30)
        self.right(105)
        self.forward(30)

        self.right(45)
        self.circle(30, 60)
        self.setheading(0)
        self.showturtle()
        self.end_poly()

        t = self.get_poly()
        sh = turtle.Shape("compound")
        sh.addcomponent(t, tiecolors[2], tiecolors[0])
        turtle.register_shape("TieAdvanced", sh)
        self.shape("TieAdvanced")

        return self

        def orbit(self):

            return None

    def check_hit(self):
        # Checking if it hit the rebel's starcraft
        return None

"""
win = turtle.Screen()

turtle.mode("logo")
tie = TIE()

tie.drawing_tie()


for i in range(3):
    tie.forward(100)
turtle.done()
"""
