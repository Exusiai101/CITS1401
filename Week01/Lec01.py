def hi():
    print("qwq")

import turtle

def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.right(180-60)

def Wierd_Structure():
    turtle.pendown()
    triangle(300)
    turtle.penup()
    turtle.setx(-100)
    turtle.sety(100)
    turtle.pendown()
    triangle(500)
    turtle.done()

Wierd_Structure()

Scout
Wenbo

Sanchia