import turtle
import time
import random
import tie_fighter # To create the Empire's Starcrafts
import x_wing      # To create the Rebel's figher

width = 1000
height = 700

win = turtle.Screen()
win.tracer(1)
win.bgcolor("pink")
turtle.mode("logo")

xwing = x_wing.XWing()
xwing.drawing_xwing()
xwing.speed(3)

tie = tie_fighter.TIE()
tie.drawing_tie()
tie.speed(3)

tie.forward(100)
xwing.forward(100)
tie.forward(100)
tie.forward(100)


turtle.done()
