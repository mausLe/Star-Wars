import turtle
import time
import random
import global_var

tiecolors = ["black", "brown", "Light Gray"]

class TIE(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color(tiecolors[2], tiecolors[0])
        self.hideturtle()
        self.penup()
        self.name = "TIE Fighter"
        self.dir = -1 # Positive # -1 is Neg
        self.circle_route_pos = random.randint(-100, 100)

    def drawing_tie(self):
        # create body of the tie
        self.begin_poly()
        self.penup()

        self.speed(0)
        #self.left(90);
        self.right(180)

        self.circle(30, 60)

        self.right(45)
        self.forward(30)

        self.right(105)
        self.forward(30)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(74.47)

        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(30)

        self.right(105)
        self.forward(30)

        self.right(45)
        self.circle(30, 120)

        # Right wing
        self.right(45)
        self.forward(30)
        self.right(105)
        self.forward(30)

        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(74.47)
        self.left(90)
        self.forward(20)
        self.left(90)
        self.forward(30)
        self.right(105)
        self.forward(30)

        self.right(45)
        self.circle(30, 60)

        self.showturtle()
        self.end_poly()

        t = self.get_poly()
        sh = turtle.Shape("compound")
        sh.addcomponent(t, tiecolors[2], tiecolors[0])
        turtle.register_shape("TieAdvanced", sh)
        self.shape("TieAdvanced")

        return self

    def orbit(self):
        x_cor = round(self.xcor())
        y_cor = round(self.ycor())
        head = round(self.heading())

        if (x_cor > global_var.width/2 + 80) or (x_cor < -global_var.width/2 - 80):
            self.dir = -self.dir
            self.right(180)
            self.circle_route_pos =  random.randint(-400, 400)

        if ((abs(self.circle_route_pos - x_cor) < 15) and y_cor == 270) or (y_cor < 270) or (y_cor > 270): # Tie meets the fire position
            if self.dir == 1: # Direction West -> East
                # self.circle_route_pos = self.circle_route_pos - 20
                self.fire = random.randrange(105, 270, 15)
                self.circle(-100, 15)
            else:
                self.fire = random.randrange(90, 255, 15)
                self.circle(100, 15)

        if (y_cor == 270):
            self.forward(30)
        elif (self.dir == 1) and (head == 0): # Direction West -> East
            self.goto(self.circle_route_pos + 40, 270)
            self.setheading(0)
        elif (self.dir == -1) and (head == 180):
            self.goto(self.circle_route_pos - 40, 270)
            self.setheading(180)


        turtle.ontimer(self.orbit, 50)

    def move(self): # Bổ sung hàm move
        self.forward(50)
        if self.xcor() > global_var.width/2 - 50 or self.xcor() < -global_var.width/2 + 50:
            self.right(180)
            self.sety(self.ycor()-100)

        # if global_var.tie_status: # Thêm điều kiện nếu như bị bắn vào đây
        turtle.ontimer(self.move,50)


    def tie_shoot(self):
        # Checking if it hit the rebel's starcraft
        return None

    def appearence(self):
        list = [75, 75, 150, 75]
        return list
