import time
from turtle import *
def main():
    setup(600,600)
    Screen()
    car=Turtle()
    car.pensize(3)
    car.shape("turtle")
    car.color('cyan')
    showturtle()
    car2=Turtle()
    car2.pensize(3)
    car2.shape("turtle")
    car2.color('red')
    track=Turtle()
    track.speed(0)


    def draw_track():
        track.pu()
        track.forward(150)
        track.left(90)
        track.pd()
        track.forward(100)
        track.left(90)
        track.forward(300)
        track.left(90)
        track.forward(200)
        track.left(90)
        track.forward(300)
        track.left(90)
        track.forward(100)
        track.right(90)
        track.forward(100)
        track.pu()
        track.right(90)
        track.forward(125)
        track.left(90)
        track.left(90)
        track.pd()
        track.forward(350)
        track.left(90)
        track.forward(500)
        track.left(90)
        track.forward(400)
        track.left(90)
        track.forward(500)
        track.left(90)
        track.forward(100)
        track.pu()
        track.forward(1500)
        car.pu()
        car2.pu()
        car.forward(180)
        car2.forward(200)
        car.left(90)
        car2.left(90)
        car.pd()
        car2.pd()

    def no_track():
        car.pu()
        car2.pu()
        car.forward(180)
        car2.forward(200)
        car.left(90)
        car2.left(90)
        car.pd()
        car2.pd()
    dec=input("Have a track? (Y)es (N)o")


    if dec == "n":
        no_track()
    else:
        draw_track()


    def k1():
        car.forward(10)

    def k2():
        car.left(10)
        car.forward(10)

    def k3():
        car.forward(-10)

    def k4():
        car.right(10)
        car.forward(10)

    onkey(k1, "w")
    onkey(k2, "a")
    onkey(k3, "s")
    onkey(k4, "d")

    def k5():
        car2.forward(10)

    def k6():
        car2.left(10)
        car2.forward(10)

    def k7():
        car2.forward(-10)

    def k8():
        car2.right(10)
        car2.forward(10)

    onkey(k5, "Up")
    onkey(k6, "Left")
    onkey(k7, "Down")
    onkey(k8, "Right")

    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print('!!!GO!!!')
    listen()
    mainloop()

main()
