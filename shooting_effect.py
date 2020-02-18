import turtle
import time
import random
import math #to calculate square root
import global_var

cannon_colors = ["Red", "Chartreuse", "Deep Sky Blue", "Deep Pink"]

class LaserCannon(turtle.Turtle):

    def __init__(self, starcraft, enemy): # Parameter 0-Rebel, 1-Empire
        turtle.Turtle.__init__(self)
        # self.color(tie_cannon_colors[side*(random.randint(1, len(tie_cannon_colors)))])
        self.color(cannon_colors[0])
        self.pensize(7)
        self.hideturtle()
        self.speed(0)
        self.starcraft = starcraft
        self.enemy = enemy
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())
        self.enemy_coordinates = []

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
            self.clear()
        else:
            turtle.ontimer(self.repeat_shoot, t = 30)

    def enemy_coordinates_f(self):
        turtle1 = turtle.Turtle()
        turtle1.hideturtle()
        turtle1.penup()
        turtle1.goto(self.enemy.position())
        turtle1.setheading(self.enemy.heading())
        list = self.enemy.appearence()
        self.enemy_coordinates.clear()
        for i in range(len(list)):
            turtle1.forward(list[i])
            turtle1.left(90)
            x_cor = round(turtle1.xcor())
            y_cor = round(turtle1.ycor())
            xy = [x_cor, y_cor]
            self.enemy_coordinates.append(xy)

        turtle1.reset()

        return self.enemy_coordinates


    def check_hit_enemy(self):
        list = self.enemy_coordinates # coordinates of A, B, C, D
        """
        B______________A
        |              |
        |              |
        C______________D
        """
        A, B, C, D = list
        AB = CD = round(math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2))
        BC = DA = round(math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2))
        S = AB*BC

        PA = round(math.sqrt((A[0] - self.xcor())**2 + (A[1] - self.ycor())**2))
        PB = round(math.sqrt((B[0] - self.xcor())**2 + (B[1] - self.ycor())**2))
        PC = round(math.sqrt((C[0] - self.xcor())**2 + (C[1] - self.ycor())**2))
        PD = round(math.sqrt((D[0] - self.xcor())**2 + (D[1] - self.ycor())**2))

        P1 = (PA+PB+AB)//2 # PAB
        P2 = (PB+PC+BC)//2 # PBC
        P3 = (PC+PD+CD)//2 # PCD
        P4 = (PD+PA+DA)//2 # PDA

        PAB = math.sqrt(P1*(P1 - PA)*(P1 - PB)*(P1 - AB))
        PBC = math.sqrt(P2*(P2 - PB)*(P2 - PC)*(P2 - BC))
        PCD = math.sqrt(P3*(P3 - PC)*(P3 - PD)*(P3 - CD))
        PDA = math.sqrt(P4*(P4 - PD)*(P4 - PA)*(P4 - DA))

        if (PAB + PBC + PCD + PDA > S):
            False
        else:
            print("Hit")
            True



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
