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
win.title("Star Wars")
win.bgpic("src\\bg.gif")
win.update()
win.tracer(0)
turtle.mode("logo")

"""
tie1 = tie_fighter.TIE()
tie1.drawing_tie()
tie1.speed(0)
tie1.right(90)
tie1.goto(300, 300)
# win.ontimer(tie1.move(), 500) # Bổ sung hàm move

tie = tie_fighter.TIE()
tie.drawing_tie()
tie.speed(0)
tie.right(90)
tie.goto(-300, 300)
tie.move() # Bổ sung hàm move
"""
xwing = x_wing.XWing()
xwing.drawing_xwing()
xwing.speed(0)
xwing.backward(250)

ties = [tie_fighter.TIE() for i in range(1)]
for tie in ties:
    tie.drawing_tie()

XWing_laser = shooting_effect.XWingCannon(xwing, ties)

TIE0_laser = shooting_effect.TIECannon(ties[0], xwing)
ties[0].goto(700, 270)
ties[0].right(90)
ties[0].orbit()

TIE0_laser = shooting_effect.TIECannon(ties[0], xwing)
# TIE1_laser = shooting_effect.TIECannon(ties[1], xwing)

# ties[1].goto(-200, 270)
# ties[1].right(90)
# ties[1].orbit()
# print(ties[1].position()," ", ties[1].fire)


# ties[1].goto(0, 270)
# ties[1].right(270)

# ties[1].orbit() # Bổ sung hàm move
    # win.ontimer(tie1.move(), 500) # Bổ sung hàm move

win.onkeypress(XWing_laser.shoot, "space")
# win.onkeypress(laser1.shoot, "k")

# laser = shooting_effect.XWingCannon(xwing, tie)

win.onkeypress(xwing.go_forward, "w")
win.onkeypress(xwing.go_backward, "s")
win.onkeypress(xwing.turn_right, "d")
win.onkeypress(xwing.turn_left, "a")
win.listen()

while True:
    # Trong hàm while True chỉ để trường hợp khi nào thua cuộc thì break --> kết thúc trò chơi
    TIE0_laser.random_shoot(ties[0].fire)
    # TIE1_laser.random_shoot(ties[1].fire)
    win.update()
    # if global_var.tie_status == 0:
    #     win.ontimer(win.bye, 1000)

turtle.mainloop()
