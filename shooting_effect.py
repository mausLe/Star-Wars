import turtle
import time
import random
import math #to calculate square root
import global_var
import winsound

cannon_colors = ["Red", "Chartreuse", "Deep Sky Blue", "Deep Pink"]

class LaserCannon(turtle.Turtle):

    def __init__(self, starcraft, enemy): # Parameter 0-Rebel, 1-Empire
        turtle.Turtle.__init__(self)
        # self.color(tie_cannon_colors[side*(random.randint(1, len(tie_cannon_colors)))])
        self.hideturtle()
        self.color(cannon_colors[0])
        self.pensize(7)
        self.penup()
        self.speed(0)
        self.enemy = enemy
        self.enemy_coordinates = []
        self.starcraft = starcraft
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())
        self.sound = 'XWing-Laser.wav'

    def enemy_coordinates_f(self):
        turtle1 = turtle.Turtle()
        # turtle1.speed(1)
        turtle1.hideturtle()
        turtle1.penup()
        turtle1.goto(self.enemy.position())
        turtle1.setheading(self.enemy.heading())
        list = self.enemy.appearence()
        self.enemy_coordinates.clear()
        for i in range(len(list)):
            turtle1.left(90)
            turtle1.forward(list[i])
            x_cor = round(turtle1.xcor())
            y_cor = round(turtle1.ycor())
            xy = [x_cor, y_cor]
            self.enemy_coordinates.append(xy)

        turtle1.clear()

        return self.enemy_coordinates

    def check_hit_enemy(self):
            list = self.enemy_coordinates_f() # coordinates of A, B, C, D

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

            P1 = (PA+PB+AB)//2 + 1 # PAB
            P2 = (PB+PC+BC)//2 + 1 # PBC
            P3 = (PC+PD+CD)//2 + 1 # PCD
            P4 = (PD+PA+DA)//2 + 1 # PDA

            PAB = math.sqrt(P1*(P1 - PA)*(P1 - PB)*(P1 - AB))
            PBC = math.sqrt(P2*(P2 - PB)*(P2 - PC)*(P2 - BC))
            PCD = math.sqrt(P3*(P3 - PC)*(P3 - PD)*(P3 - CD))
            PDA = math.sqrt(P4*(P4 - PD)*(P4 - PA)*(P4 - DA))

            if (PAB + PBC + PCD + PDA > S):
                return False
                # print("Missed")
            else:
                print("Hit")
                return True

    def check_collision(self):
        width = global_var.width
        height = global_var.height
        if self.xcor() < -width//2 or self.xcor() > width//2:
            return True
        if self.ycor() <-height//2 or self.ycor() > height//2:
            return True

        return False

    def repeat_shoot(self):
        self.pendown()
        self.forward(10)
        if self.check_collision() or self.check_hit_enemy():
            self.clear()
        else:
            # turtle.ontimer(self.repeat_shoot, t = 5)
            turtle.ontimer(self.repeat_shoot, t = 1)

    def shoot(self):
        self.hideturtle()
        self.penup()
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())
        self.left(90)
        self.forward(2) # Adjust laser cannon position
        # self.setheading(self.starcraft.heading())
        self.right(90)
        self.pendown()
        winsound.PlaySound(self.sound, winsound.SND_ASYNC)
        self.repeat_shoot()

# X-Wing inherite from LaserCannon
class XWingCannon(LaserCannon):
    def check_hit_TIE(self):
        self.hideturtle()

        return False

# TIE inherite from LaserCannon
class TIECannon(LaserCannon):
    def __init__(self, starcraft, enemy): # Parameter 0-Rebel, 1-Empire
        turtle.Turtle.__init__(self)
        # self.color(tie_cannon_colors[side*(random.randint(1, len(tie_cannon_colors)))])
        self.hideturtle()
        self.color(cannon_colors[random.randint(1, len(cannon_colors) - 1)])
        self.pensize(7)
        self.penup()
        self.speed(0)
        self.enemy = enemy
        self.enemy_coordinates = []
        self.starcraft = starcraft
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())
        self.sound = 'TIE-Fire.wav'


    def orbit(self):


        return None
