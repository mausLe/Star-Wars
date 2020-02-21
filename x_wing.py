import turtle
import time
import random

xwingcolors = ["Deep Pink", "brown", "Light Gray"]

class XWing(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color(xwingcolors[2], xwingcolors[0])
        self.hideturtle()

    def drawing_xwing(self):
        # create body of the self
        self.begin_poly()
        self.penup()
        self.speed(0)
        self.color("Yellow")
        self.left(90);

        self.forward(15)

        self.left(90)
        self.forward(60)

        self.right(90)
        self.forward(20)

        self.right(90)
        self.forward(30)
        self.left(90)
        self.forward(10)

        self.left(90)
        self.forward(60)

        self.left(90)
        self.forward(15)
        self.setheading(180)
        self.forward(10)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(10)
        self.right(90)

        # Right wing
        self.forward(20)
        self.right(90)
        self.forward(10)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(10)
        self.right(90)
        self.forward(10)

        self.setheading(0)
        self.forward(60)
        self.left(90)
        self.forward(10)
        self.left(90)
        self.forward(30)
        self.right(90)
        self.forward(20)
        self.right(90)
        self.forward(60)
        self.left(90)
        self.forward(10)
        self.setheading(0)
        self.showturtle()
        self.end_poly()

        p = self.get_poly()
        s = turtle.Shape("compound")
        s.addcomponent(p, xwingcolors[2], xwingcolors[0])
        turtle.register_shape("X-Wing", s)
        self.shape("X-Wing")

        return self


    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def go_forward(self):
        self.forward(10)
        # self.forward(2)
        # self.forward(2)
    def go_backward(self):
        self.backward(10)

    def appearence(self):
        list = [45, 100, 90, 100]
        return list

    # def check_hit(self):
        # Checking if it hit the rebel's starcraft

        return None

"""
win = turtle.Screen()

turtle.mode("logo")
xwing = xwing()

xwing.drawing_xwing()


for i in range(3):
    xwing.forward(100)
turtle.done()
"""
