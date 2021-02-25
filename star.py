import turtle
import math

dot = turtle.Turtle()
dot.getscreen().bgcolor("#abf9ff")
dot.penup()
dot.goto(-100, 70)
dot.pendown()

# for i in range(5):
#   dot.forward(200)
#   dot.left(216)

dot.speed(10)

def star(turtle, size):
  if size <= 10:
    return
  else:
    for i in range(5):
      dot.forward(size)
      star(turtle, size/2)
      dot.left(216)

star(dot, 200)


turtle.done()