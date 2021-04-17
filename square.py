import turtle



crush = turtle.Turtle()
# record a polygon
turtle.begin_poly()
  
# form a polygon
turtle.forward(20)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(20)

turtle.end_poly()

numbers = turtle.get_poly()
turtle.register_shape("triangle", numbers)

turtle.shape("triangle")
# do some motion
for i in range(100):
    turtle.forward(3+2*i)
    turtle.right(95)

turtle.done()

# input("Press any key to exit ...")