
import turtle

def drawcoolsquare(t, sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        t=turtle.color(i)
        t=turtle.forward(sz)
        t=turtle.left(90)

wn=turtle.Screen()
wn.bgcolor("yellow")

tt=turtle.Turtle
tt=turtle.pensize(3)


size=20
for i in range(30):
    drawcoolsquare(tt,size)
    size = size +10
    tt=turtle.forward(10)
    tt=turtle.right(18)
wn.mainloop
