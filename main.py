import turtle
import time
import random

import global_var
import tie_fighter # To create the Empire's Starcrafts
import x_wing      # To create the Rebel's figher
import shooting_effect #
# import shoot_function



win = turtle.Screen()
width, height = global_var.width, global_var.height
win.setup(width, height)
win.bgcolor("pink")

turtle.mode("logo")


xwing = x_wing.XWing()
xwing.drawing_xwing()
xwing.speed(3)

tie = tie_fighter.TIE()
tie.drawing_tie()
tie.speed(3)

xwing.position()
xwing.heading()
laser = shooting_effect.LaserCannon(xwing.position(), xwing.heading())
# laser1 = shoot_function.Laser()

win.onkeypress(laser.shoot, "space")
win.listen()
win.tracer(1)

while True:
    win.update()

turtle.done()
