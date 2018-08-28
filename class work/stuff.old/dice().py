import turtle

#create turtle and window()
wn=turtle.Screen()
wn.bgcolor('cyan')
t=turtle.Turtle()
t.shape('turtle')
#create movement()
t.penup()
size=20
for i in range(30):
    t.stamp()
    size=size+3
    t.forward(size)
    t.right(24)
#finialize()
wn.mainloop()
#bug test()
