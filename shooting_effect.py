import turtle
import time
import random
import global_var

cannon_colors = ["Red", "Chartreuse", "Deep Sky Blue", "Deep Pink"]

class LaserCannon(turtle.Turtle):
    def __init__(self, starcraft): # Parameter 0-Rebel, 1-Empire
        turtle.Turtle.__init__(self)
        # self.color(tie_cannon_colors[side*(random.randint(1, len(tie_cannon_colors)))])
        self.color(cannon_colors[0])
        self.pensize(7)
        self.hideturtle()
        self.speed(0)
        self.starcraft = starcraft
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())

    def check_collision(self):
        width = global_var.width
        height = global_var.height
        if self.xcor() < -width//2 or self.xcor() > width//2:
            return True
        if self.ycor() <-height//2 or self.ycor() > height//2:
            return True

        return False

    def shoot(self):
        self.penup()
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())
        self.pendown()
        self.repeat_shoot()

    def repeat_shoot(self):
        self.forward(50)
        if self.check_collision():
            print("Hit")
            self.clear()
        else:
            turtle.ontimer(self.repeat_shoot, t = 30)

# X-Wing inherite from LaserCannon
class XWingCannon(LaserCannon):
    def check_hit_TIE(self):


        return False

# TIE inherite from LaserCannon
class TIECannon(LaserCannon):
    def __init__(self, starcraft): # Parameter 0-Rebel, 1-Empire
        turtle.Turtle.__init__(self)
        # self.color(tie_cannon_colors[side*(random.randint(1, len(tie_cannon_colors)))])
        self.color(cannon_colors[random.randint(1, len(cannon_colors) - 1)])
        self.pensize(7)
        self.hideturtle()
        self.speed(0)
        self.starcraft = starcraft
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())
    """
    """

    def orbit(self):


        return None
