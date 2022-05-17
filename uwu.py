from cgitb import grey
import turtle
turtle.title('uwu')
turtle.setworldcoordinates(-2000,-2000,2000,2000)
turtle.speed=500

ewe = turtle.Turtle()
ewe.pen(pencolor="blue")
ewe.penup()
ewe.goto(0,-1425)
ewe.pendown()
ewe.st()
ewe.circle(1425)
ewe.hideturtle()

def draw_outer(x,y,tilt,radius):
    turtle.color("orange")
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)
    
def draw_mid(x,y,tilt,radius):
    turtle.color("purple")
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)

def draw_inner(x,y,tilt,radius):
    turtle.color("green")
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)
    
for tilt in range(0,360,15):
    draw_outer(0,0,tilt,1000)

sumu = turtle.Turtle()
sumu.pen(pencolor="red")
sumu.penup()
sumu.goto(0,-1068.75)
sumu.pendown()
sumu.st()
sumu.circle(1068.75)
sumu.hideturtle()

for tilt in range(0,360,30): 
    draw_mid(0,0,tilt,750)
    
ugu = turtle.Turtle()
ugu.pen(pencolor="pink")
ugu.penup()
ugu.goto(0,-712.5)
ugu.pendown()
ugu.st()
ugu.circle(712.5)
ugu.hideturtle()
    
for tilt in range(0,360,60): 
    draw_inner(0,0,tilt,500)
    