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
win.tracer(0)

turtle.mode("logo")


xwing = x_wing.XWing()
xwing.drawing_xwing()
xwing.speed(10)

tie = tie_fighter.TIE()
tie.drawing_tie()
tie.speed(10)


xwing.position()
xwing.heading()
# laser = shooting_effect.LaserCannon(xwing.position(), xwing.heading())
# laser = shooting_effect.LaserCannon(xwing)
laser = shooting_effect.XWingCannon(xwing, tie)

# laser1 = shoot_function.Laser()

win.onkeypress(laser.shoot, "space")
win.onkeypress(xwing.go_forward, "w")
win.onkeypress(xwing.go_backward, "s")
win.onkeypress(xwing.turn_right, "r")
win.onkeypress(xwing.turn_left, "q")
l =  laser.enemy_coordinates_f()
print(l)
laser.check_hit_enemy()

win.listen()

while True:

    win.update()

turtle.done()
