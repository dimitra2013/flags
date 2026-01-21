import turtle
import random

scn = turtle.Screen()
sam= turtle.Turtle()
turtle.title("guess the flag")

points = 0
lives =  1


def Germany():

    sam.penup()
    sam.goto(0,0)
    sam.fillcolor("black")
    sam.pencolor("black")


    sam.pendown()
    sam.begin_fill()
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.right(90)
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.end_fill()

    sam.penup()
    sam.left(180)
    sam.forward(41)
    sam.fillcolor("red")
    sam.pencolor("red")


    sam.pendown()
    sam.begin_fill()
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

    sam.penup()
    sam.left(90)
    sam.forward(41)
    sam.fillcolor("yellow")
    sam.pencolor("yellow")

    sam.pendown()
    sam.begin_fill()
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

def Italy():
    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("green")
    sam.pencolor("green")


    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.pencolor("black")


    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.fillcolor("red")
    sam.pencolor("red")


    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

def Monaco():

    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(190)
    sam.right(90)
    sam.forward(60)
    sam.right(90)
    sam.forward(190)
    sam.right(90)
    sam.forward(60)
    sam.end_fill()

    sam.penup()
    sam.right(180)
    sam.forward(61)
    sam.pencolor("black")


    sam.pendown()
    sam.forward(60)
    sam.left(90)
    sam.forward(190)
    sam.left(90)
    sam.forward(60)
    sam.left(90)
    sam.forward(190)

def Poland():
    sam.penup()
    sam.goto(0, 0)
    sam.pencolor("black")

    sam.pendown()
    sam.forward(190)
    sam.right(90)
    sam.forward(60)
    sam.right(90)
    sam.forward(190)
    sam.right(90)
    sam.forward(60)


    sam.penup()
    sam.right(180)
    sam.forward(61)
    sam.pencolor("red")
    sam.fillcolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(60)
    sam.left(90)
    sam.forward(190)
    sam.left(90)
    sam.forward(60)
    sam.left(90)
    sam.forward(190)
    sam.end_fill()

def France():
    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("blue")
    sam.pencolor("blue")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.pencolor("black")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

def Ireland():

    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("green")
    sam.pencolor("green")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.pencolor("black")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.fillcolor("orange")
    sam.pencolor("orange")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

def Lithuania():
    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("yellow")
    sam.pencolor("yellow")

    sam.pendown()
    sam.begin_fill()
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.right(90)
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.end_fill()

    sam.penup()
    sam.left(180)
    sam.forward(41)
    sam.fillcolor("green")
    sam.pencolor("green")

    sam.pendown()
    sam.begin_fill()
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

    sam.penup()
    sam.left(90)
    sam.forward(41)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

def Belgium():
    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("black")
    sam.pencolor("black")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.pencolor("yellow")
    sam.fillcolor("yellow")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

def Netherlands():

    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.right(90)
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.end_fill()

    sam.penup()
    sam.left(180)
    sam.forward(41)
    sam.pencolor("black")

    sam.pendown()
    sam.begin_fill()
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(45)
    sam.left(90)
    sam.forward(170)


    sam.penup()
    sam.left(90)
    sam.forward(41)
    sam.fillcolor("blue")
    sam.pencolor("blue")

    sam.pendown()
    sam.begin_fill()
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

def Bulgaria():
    sam.penup()
    sam.goto(0, 0)

    sam.pencolor("black")

    sam.pendown()
    sam.begin_fill()
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.right(90)
    sam.forward(170)
    sam.right(90)
    sam.forward(40)


    sam.penup()
    sam.left(180)
    sam.forward(41)
    sam.fillcolor("green")
    sam.pencolor("green")

    sam.pendown()
    sam.begin_fill()
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

    sam.penup()
    sam.left(90)
    sam.forward(41)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

def Austria():

    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.right(90)
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.end_fill()

    sam.penup()
    sam.left(180)
    sam.forward(41)
    sam.pencolor("black")

    sam.pendown()
    sam.begin_fill()
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(45)
    sam.left(90)
    sam.forward(170)

    sam.penup()
    sam.left(90)
    sam.forward(41)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

def Romania():
    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("blue")
    sam.pencolor("blue")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.pencolor("yellow")
    sam.fillcolor("yellow")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

    sam.penup()
    sam.right(90)
    sam.forward(52)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.right(90)
    sam.forward(55)
    sam.right(90)
    sam.forward(150)
    sam.end_fill()

def Russia():
    sam.penup()
    sam.goto(0, 0)

    sam.pencolor("black")

    sam.pendown()
    sam.begin_fill()
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.right(90)
    sam.forward(170)
    sam.right(90)
    sam.forward(40)

    sam.penup()
    sam.left(180)
    sam.forward(41)
    sam.fillcolor("blue")
    sam.pencolor("blue")

    sam.pendown()
    sam.begin_fill()
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

    sam.penup()
    sam.left(90)
    sam.forward(41)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

def Ukraine():
    sam.penup()
    sam.goto(0, 0)
    sam.pencolor("blue")
    sam.fillcolor("blue")

    sam.pendown()
    sam.begin_fill()
    sam.forward(190)
    sam.right(90)
    sam.forward(60)
    sam.right(90)
    sam.forward(190)
    sam.right(90)
    sam.forward(60)
    sam.end_fill()

    sam.penup()
    sam.right(180)
    sam.forward(61)
    sam.pencolor("yellow")
    sam.fillcolor("yellow")

    sam.pendown()
    sam.begin_fill()
    sam.forward(60)
    sam.left(90)
    sam.forward(190)
    sam.left(90)
    sam.forward(60)
    sam.left(90)
    sam.forward(190)
    sam.end_fill()

def Armenia():
    sam.penup()
    sam.goto(0, 0)
    sam.fillcolor("red")
    sam.pencolor("red")

    sam.pendown()
    sam.begin_fill()
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.right(90)
    sam.forward(170)
    sam.right(90)
    sam.forward(40)
    sam.end_fill()

    sam.penup()
    sam.left(180)
    sam.forward(41)
    sam.fillcolor("blue")
    sam.pencolor("blue")

    sam.pendown()
    sam.begin_fill()
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(45)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()

    sam.penup()
    sam.left(90)
    sam.forward(41)
    sam.fillcolor("orange")
    sam.pencolor("orange")

    sam.pendown()
    sam.begin_fill()
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.left(90)
    sam.forward(43)
    sam.left(90)
    sam.forward(170)
    sam.end_fill()


countries = [Germany , Italy , Monaco , Poland , France , Ireland , Lithuania , Belgium , Netherlands , Bulgaria , Austria , Romania , Russia , Ukraine , Armenia]

while lives > 0 and len(countries) > 0:
    sam.reset()
    flag = random.choice(countries)
    flag()
    answer = input("FLAG:")

    if answer == flag.__name__:
        print("YES")
        points = points + 1
        countries.remove(flag)
    else:
        print("NO")
        lives = lives - 1
    print("LIVES:", lives)
    print("POINTS: ", points)

if points < 5:
    print("C")
elif points < 10:
    print("B")
else:
    print("A")



































turtle.done()