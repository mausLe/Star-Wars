import turtle
import time
import random
import os, sys
import winsound

import global_var
import tie_fighter # To create the Empire's Starcrafts
import x_wing      # To create the Rebel's fighter
import shooting_effect #

os.chdir(os.path.dirname(sys.argv[0]))
# print("Working dir: ", os.getcwd())

win = turtle.Screen()
width, height = global_var.width, global_var.height
win.setup(width, height)
win.title("Star Wars")
win.bgpic("src\\bg.gif")
win.update()
turtle.setundobuffer(42)

global_var.score = 0
score_board = turtle.Turtle()
score_board.color("Deep Sky Blue")
score_board.penup()
score_board.hideturtle()
score_board.speed(1)

win.tracer(0)
xwing = x_wing.XWing()
xwing.drawing_xwing()
xwing.goto(0, -180)


score_board.write("Turn off TELEX method", align = "center", font=("Helvetica", 40, "bold"))
time.sleep(1)

score_board.clear()
score_board.write("Use A/D/R/Q - Control       SPACE - Shoot", align = "center", font=("Helvetica", 40, "bold"))
time.sleep(2)

score_board.clear()
score_board.color("Yellow")
score_board.write("MAY THE FORCE BE WITH YOU...", align = "center", font=("Helvetica", 40, "bold"))
time.sleep(2)

score_board.goto(-400, -320)

ties = [tie_fighter.TIE() for i in range(2)]
for tie in ties:
    tie.drawing_tie()

XWing_laser = shooting_effect.XWingCannon(xwing, ties)
xwing.goto(0, -180)

TIE0_laser = shooting_effect.TIECannon(ties[0], xwing)
TIE1_laser = shooting_effect.TIECannon(ties[1], xwing)

ties[0].left(90)
ties[0].goto(300, 270)
ties[0].orbit()

ties[1].goto(-global_var.width//2 - 80, 270)
ties[1].orbit()

win.onkeypress(XWing_laser.shoot, "space")

# lower key
win.onkeypress(xwing.rotate_left, "q")
win.onkeypress(xwing.rotate_right, "r")
win.onkeypress(xwing.go_toward_right, "d")
win.onkeypress(xwing.go_toward_left, "a")
win.listen()

# Upper key
win.onkeypress(xwing.rotate_left, "Q")
win.onkeypress(xwing.rotate_right, "R")
win.onkeypress(xwing.go_toward_right, "D")
win.onkeypress(xwing.go_toward_left, "A")
win.listen()

while True:
    # Trong hàm while True chỉ để trường hợp khi nào thua cuộc thì break --> kết thúc trò chơi
    TIE0_laser.random_shoot()
    TIE1_laser.random_shoot()
    score_board.clear()
    score_board.write("Score: {}    Shield: {} %".format(global_var.score, global_var.live*25), align = "Center", font=("Helvetica", 24, "normal"))

    if (global_var.live <= 0):
        score_board.clear()
        score_board.goto(0, 40)
        score_board.write("Score: {}".format(global_var.score), align = "Center", font=("Helvetica", 24, "normal"))
        score_board.goto(0, -40)
        score_board.color("Yellow")
        score_board.write("GAMEOVER", align = "center", font=("Helvetica", 40, "bold"))
        time.sleep(2)
        win.bye()

    win.update()

turtle.mainloop()
