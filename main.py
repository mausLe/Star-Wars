import turtle
import time
import random
import os, sys
import winsound

import global_var
import tie_fighter # To create the Empire's Starcrafts
import x_wing      # To create the Rebel's figher
import shooting_effect #
# import shoot_function

winsound.PlaySound("sound\XWing-Laser.wav", winsound.SND_ASYNC)
os.chdir(os.path.dirname(sys.argv[0]))

# file = "C:\Stuff\Teaching at Teky\Star Wars\Vader.mp3"
# playsound(file)
win = turtle.Screen()
width, height = global_var.width, global_var.height
win.setup(width, height)
# win.bgcolor("pink")
win.bgpic("bg.gif")
win.update()
win.tracer(0)
turtle.mode("logo")

tie = tie_fighter.TIE()
tie.drawing_tie()
tie.speed(10)
tie.right(90)
tie.backward(200)

xwing = x_wing.XWing()
xwing.drawing_xwing()
xwing.speed(10)

xwing.position()
xwing.heading()
# laser = shooting_effect.LaserCannon(xwing.position(), xwing.heading())
# laser = shooting_effect.LaserCannon(xwing)
# laser = shooting_effect.XWingCannon(xwing, tie)



# laser1 = shoot_function.Laser()
laser = shooting_effect.TIECannon(tie, xwing)
# laser = shooting_effect.XWingCannon(xwing, tie)

def check():
    l =  laser.enemy_coordinates_f()
    print(l)
    laser.check_hit_enemy()

win.onkeypress(laser.shoot, "space")
win.onkeypress(xwing.go_forward, "w")
win.onkeypress(xwing.go_backward, "s")
win.onkeypress(xwing.turn_right, "r")
win.onkeypress(xwing.turn_left, "q")

win.onkeypress(check, "c")

win.listen()

while True:
    for i in range(4):
        tie.forward(300)
        tie.right(90)
    win.update()

turtle.done()
