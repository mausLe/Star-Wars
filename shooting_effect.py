import turtle
import time
import random

cannon_colors = ["Red", "Chartreuse", "Deep Sky Blue", "Deep Pink"]

class LaserCannon(turtle.Turtle):
    def __init__(self): # Parameter 0-Rebel, 1-Empire
        turtle.Turtle.__init__(self)
        # self.color(tie_cannon_colors[side*(random.randint(1, len(tie_cannon_colors)))])
        self.color(cannon_colors[0])
        self.pensize(7)

    def check_collision(self):
        if self.xcor() < -width//2 or self.xcor() > width//2:
            return True
        if self.ycor() <-height//2 or self.ycor() > height//2:
            return True

        return False

    def repeat_shoot(self):

        return None

    def shoot(self):

        return None

# X-Wing inherite from LaserCannon
class XWingCannon(LaserCannon):
    def check_hit_TIE(self):


        return False

# TIE inherite from LaserCannon
class TIECannon(LaserCannon):
    def __init__(self):
        self.color(cannon_colors[random.randint(1, len(cannon_colors))])
        self.pensize(7)

    def orbit(self):


        return None
