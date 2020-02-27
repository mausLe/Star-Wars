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
turtle.mode("logo")
turtle.setundobuffer(42)

global_var.score = 0
score_board = turtle.Turtle()
#score_board.shape("square")
score_board.color("Deep Sky Blue")
score_board.penup()
score_board.hideturtle()
score_board.speed(1)

# score_board.goto(-450, -300)
# score_board.write("Score: {}".format(global_var.score), align = "center", font=("Courier", 24, "normal"))

win.tracer(0)
xwing = x_wing.XWing()
xwing.drawing_xwing()
xwing.speed(0)
xwing.backward(230)

score_board.goto(0, 0)
win.tracer(1)

score_board.write("Use W/S/A/D - Control       SPACE - Shoot", align = "center", font=("Helvetica", 40, "bold"))
time.sleep(2)
score_board.clear()

score_board.color("Yellow")
score_board.write("MAY THE FORCE BE WITH YOU", align = "center", font=("Helvetica", 40, "bold"))
time.sleep(2)

win.tracer(0)
score_board.goto(-450, -300)

ties = [tie_fighter.TIE() for i in range(2)]
for tie in ties:
    tie.drawing_tie()

XWing_laser = shooting_effect.XWingCannon(xwing, ties)

TIE0_laser = shooting_effect.TIECannon(ties[0], xwing)
ties[0].goto(700, 270)
ties[0].right(90)
ties[0].orbit()

TIE0_laser = shooting_effect.TIECannon(ties[0], xwing)
TIE1_laser = shooting_effect.TIECannon(ties[1], xwing)

ties[1].goto(-200, 270)
ties[1].right(90)
ties[1].orbit()


# ties[1].orbit() # Bổ sung hàm move
    # win.ontimer(tie1.move(), 500) # Bổ sung hàm move

win.onkeypress(XWing_laser.shoot, "space")


win.onkeypress(xwing.go_forward, "w")
win.onkeypress(xwing.go_backward, "s")
win.onkeypress(xwing.turn_right, "d")
win.onkeypress(xwing.turn_left, "a")
#print(turtle.turtles())
win.listen()

while True:
    # Trong hàm while True chỉ để trường hợp khi nào thua cuộc thì break --> kết thúc trò chơi
    # TIE0_laser.random_shoot(ties[0].fire) Khong truyen tham so fire_pos
    TIE0_laser.random_shoot()
    TIE1_laser.random_shoot()
    score_board.clear()
    score_board.write("Score: {}".format(global_var.score), align = "Center", font=("Helvetica", 24, "normal"))

    win.update()

turtle.mainloop()
