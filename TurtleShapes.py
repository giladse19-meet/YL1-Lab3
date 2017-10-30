import turtle

turtle.register_shape("mozar", ((50,0),(50,-50),(25,-100),(0,-50),(0,0)))
turtle.shape("mozar")

turtle.goto(100,0)
turtle.goto(100,-100)
turtle.goto(50,-200)
turtle.goto(0,-100)
turtle.goto(0,0)

turtle.mainloop()
