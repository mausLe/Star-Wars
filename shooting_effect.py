import turtle
import time
import random
import math #to calculate square root
import winsound

import global_var

cannon_colors = ["Red", "Chartreuse", "Deep Sky Blue", "Deep Pink"]

class LaserCannon(turtle.Turtle):

    def __init__(self, starcraft, enemy): # Parameter 0-Rebel, 1-Empire
        turtle.Turtle.__init__(self)
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
        self.sound = 'src\\XWing-Laser.wav'

    def enemy_coordinates_f(self):
        turtle1 = turtle.Turtle()
        turtle1.hideturtle()
        turtle1.penup()

        # For each enemy (e.g: 3) calculate coordinates seperately
        self.enemy_coordinates.clear()
        for tie in self.enemy:
            turtle1.goto(tie.position())
            turtle1.setheading(tie.heading())
            list = tie.appearence()

            index = self.enemy.index(tie)*4
            for i in range(len(list)):
                turtle1.left(90)
                turtle1.forward(list[i])
                x_cor = round(turtle1.xcor())
                y_cor = round(turtle1.ycor())
                xy = [x_cor, y_cor]
                self.enemy_coordinates.append(xy)

        return self.enemy_coordinates

    def check_hit_enemy(self):

        max_distance = self.distance(self.enemy[0].position())
        tie_index = 0
        for tie in self.enemy:
            if self.distance(tie.position()) <= max_distance:
                max_distance = self.distance(tie.position())
                tie_index = self.enemy.index(tie)

        tie_index = tie_index
        list_temp = self.enemy_coordinates_f() # coordinates of A, B, C, D
        list = list_temp[tie_index*4:tie_index*4+4]
            # Set a bounding box around enemy
            # calculate sum of triangles that created by Laser 4 points bounding box
            # if sum <= square of bounding box then laser hit enemy
        """
            B______________A
        \___|              | \
        /   |              | /
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

        S1 = P1*(P1 - PA)*(P1 - PB)*(P1 - AB)
        S2 = P2*(P2 - PB)*(P2 - PC)*(P2 - BC)
        S3 = P3*(P3 - PC)*(P3 - PD)*(P3 - CD)
        S4 = P4*(P4 - PD)*(P4 - PA)*(P4 - DA)
        S2s = [S1, S2, S3, S4]

        for i in range (len(S2s)):
            if S2s[i] > 0:
                S2s[i] = math.sqrt(S2s[i])
            else:
                S2s[i] = 0

        if (S2s[0] + S2s[1] + S2s[2] + S2s[3] > S):
            return -1
        else:
            winsound.PlaySound("src\\Explosion.wav", winsound.SND_ASYNC)
            self.enemy[tie_index].hideturtle()
            # Random the fire position every round
            self.enemy[tie_index].fire = random.randint(-500, 500)

            if (self.enemy[tie_index].dir == 1):
                self.enemy[tie_index].dir = -1
                self.enemy[tie_index].goto(global_var.width//2 + 80, 270)
                self.enemy[tie_index].setheading(270)
                # print(self.enemy[tie_index].position())
                # print(self.enemy[tie_index].heading())


            else:
                self.enemy[tie_index].dir = 1
                self.enemy[tie_index].goto(-global_var.width//2 - 80, 270)
                self.enemy[tie_index].setheading(90)

            self.enemy[tie_index].showturtle()

            return tie_index

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
        x = self.check_hit_enemy()
        if self.check_collision() or x != -1:
            self.clear()
        else:
            turtle.ontimer(self.repeat_shoot, t = 1)

    def shoot(self):
        self.hideturtle()
        self.penup()
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())
        self.left(90)
        self.forward(2) # Adjust laser cannon position
        self.right(90)
        self.pendown()
        winsound.PlaySound(self.sound, winsound.SND_ASYNC)
        self.repeat_shoot()

# X-Wing inherite from LaserCannon
class XWingCannon(LaserCannon):
    def check_hit_TIE(self):

        return None

# TIE inherite from LaserCannon
class TIECannon(LaserCannon):
    def __init__(self, starcraft, enemy): # Parameter 0-Rebel, 1-Empire
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.color("Chartreuse")#cannon_colors[random.randint(1, len(cannon_colors) - 1)])
        self.pensize(7)
        self.penup()
        self.speed(0)
        self.enemy = enemy
        self.enemy_coordinates = []
        self.starcraft = starcraft
        self.goto(self.starcraft.position())
        self.setheading(self.starcraft.heading())
        self.sound = 'src\\TIE-Fire.wav'

    def enemy_coordinates_f(self):
        turtle1 = turtle.Turtle()
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

        # Set a bounding box around enemy
        # calculate sum of triangles that created by Laser 4 points bounding box
        # if sum <= square of bounding box then laser hit enemy
        """
        B______________A
    \___|              | \
    /   |              | /
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

        S1 = P1*(P1 - PA)*(P1 - PB)*(P1 - AB)
        S2 = P2*(P2 - PB)*(P2 - PC)*(P2 - BC)
        S3 = P3*(P3 - PC)*(P3 - PD)*(P3 - CD)
        S4 = P4*(P4 - PD)*(P4 - PA)*(P4 - DA)
        S2s = [S1, S2, S3, S4]

        for i in range (len(S2s)):
            if S2s[i] > 0:
                S2s[i] = math.sqrt(S2s[i])
            else:
                S2s[i] = 0

        if (S2s[0] + S2s[1] + S2s[2] + S2s[3] > S):
            return -1
        else:
            winsound.PlaySound("src\\Explosion.wav", winsound.SND_ASYNC)
            return 0

    def random_shoot(self, fire_pos):
        if (self.starcraft.heading() == fire_pos):
            self.shoot()


"""
self.hideturtle()
self.penup()
self.goto(self.starcraft.position())
self.setheading(self.starcraft.heading())
self.left(90)
self.forward(2) # Adjust laser cannon position
self.right(90)
self.pendown()
winsound.PlaySound(self.sound, winsound.SND_ASYNC)
"""
