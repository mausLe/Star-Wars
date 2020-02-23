import turtle
import time
import random
import os, sys
import winsound

import global_var
import tie_fighter # To create the Empire's Starcrafts
import x_wing      # To create the Rebel's figher
import shooting_effect #

os.chdir(os.path.dirname(sys.argv[0]))
# print("Working dir: ", os.getcwd())

win = turtle.Screen()
width, height = global_var.width, global_var.height
win.setup(width, height)
win.bgpic("src\\bg.gif")
win.update()
win.tracer(0)
turtle.mode("logo")

tie = tie_fighter.TIE()
tie.drawing_tie()
tie.speed(3)
tie.right(90)
tie.backward(200)

xwing = x_wing.XWing()
xwing.drawing_xwing()
xwing.speed(0)
xwing.backward(200)

# laser = shooting_effect.TIECannon(tie, xwing)
laser = shooting_effect.XWingCannon(xwing, tie)

win.onkeypress(laser.shoot, "space")
win.onkeypress(xwing.go_forward, "w")
win.onkeypress(xwing.go_backward, "s")
win.onkeypress(xwing.turn_right, "d")
win.onkeypress(xwing.turn_left, "a")
win.listen()

while True:
    win.tracer(1)
    for i in range(2):
        tie.forward(1000)
        tie.right(90)
        tie.forward(200)
        tie.right(90)

    win.update()

turtle.mainloop()
