import turtle
turtle.speed(0)
for index in range(360):
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.right(0.3)

turtle.mainloop()
