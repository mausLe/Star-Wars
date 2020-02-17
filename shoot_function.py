import turtle
import time
import random

win = turtle.Screen()
width = 1000
height = 700

class Laser(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.pensize(7)

    def check_collision(self):
        if self.xcor() < -width//2 or self.xcor() > width//2:
            return True
        if self.ycor() <-height//2 or self.ycor() > height//2:
            return True

        return False

    def repeat_shoot(self):
        self.forward(20)
        if self.check_collision():
            print("Hit")
            self.clear()
        else:
            turtle.ontimer(self.repeat_shoot,t=30)

    def shoot(self):
        self.penup()
        self.goto(-100,-100)
        self.setheading(90)
        self.pendown()
        self.repeat_shoot()

def border_collision(stuff):
    if stuff.xcor() < -width//2 or stuff.xcor() > width//2:
        return True
    if stuff.ycor() <-height//2 or stuff.ycor() > height//2:
        return True

    return False

cannon = turtle.Turtle()
cannon.speed(10)
def shoot():
    cannon.penup()
    cannon.goto(100,-300)
    cannon.setheading(90)
    cannon.pendown()
    repeat_shoot()

def repeat_shoot():
    cannon.color("Chartreuse")
    cannon.pensize(7)
    cannon.forward(50)
    if border_collision(cannon):
        print("Hit")
        cannon.clear()
    else:
        turtle.ontimer(repeat_shoot,t=30)

laser = Laser()


turtle.onkeypress(shoot, "k")
turtle.onkeypress(laser.shoot, "space")
turtle.listen()

win.tracer(0)
while True:
    win.update()

turtle.done()
