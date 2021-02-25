import turtle
import math
import random

width = int(input("Enter screen width: "))
height = int(input("Enter screen height: "))




turtle.setup(width, height, startx=None, starty=None)
turtle.Turtle().speed(10)
turtle.Turtle().getscreen().bgcolor("#34baeb")
turtle.colormode(255)



# def fish():
#   fish = turtle.Turtle()
#   for i in range(4):
#     fish.forward(50)
#     fish.pendown()
#     fish.forward(50)
#     fish.left(90)

#   fish.circle(200)
#   turtle.done()

def tail(x, y, color):
  tail = turtle.Turtle()
  tail.penup()
  tail.setpos(x, y)
  tail.forward(105)
  tail.left(90)
  tail.backward(25)
  tail.pendown()
  tail.color(color)
  tail.begin_fill()
  for i in range(3):
    tail.forward(65)
    tail.left(120)
  tail.end_fill()
  tail.hideturtle()

def eye(x,y):
  eye = turtle.Turtle()
  eye.penup()
  eye.setpos(x,y)
  eye.backward(35)
  eye.color("black")
  eye.begin_fill()
  eye.circle(5)
  eye.end_fill()
  eye.hideturtle()

def big_scales(x,y):
  scale_1 = turtle.Turtle()
  scale_1.penup()
  scale_1.setpos(x,y)
  scale_1.backward(20)
  scale_1.right(90)
  scale_1.forward(33)
  scale_1.left(90)
  scale_1.pendown()
  for i in range(3):
    scale_1.circle(10,180)
    scale_1.right(90)
    scale_1.forward(1)
    scale_1.right(90)
  scale_1.hideturtle()

def small_scales(x,y):
  scale_2 = turtle.Turtle()
  scale_2.penup()
  scale_2.setpos(x,y)
  scale_2.forward(10)
  scale_2.right(90)
  scale_2.forward(20)
  scale_2.left(90)
  scale_2.pendown()
  for i in range(2):
    scale_2.circle(10,180)
    scale_2.right(90)
    scale_2.forward(1)
    scale_2.right(90)
  scale_2.hideturtle()

def body(x, y, color):
  body = turtle.Turtle()
  body.penup()
  body.setpos(x,y)
  body.color(color)
  body.begin_fill()
  body.shape("circle")
  body.shapesize(5,6,1)
  body.end_fill()
  body.penup()
  eye(x,y)
  big_scales(x,y)
  small_scales(x,y)
  tail(x, y, color)

# def fish():
#   for i in range(5):
#     randColor = random.randrange(0, len(colors))
#     rand1 = random.randrange(-300, 300)
#     rand2 = random.randrange(-300, 300)
#     turtle.Turtle().penup()
#     turtle.Turtle().setpos((rand1,rand2))
#     body()

# def fish():
#   turtle.Turtle().goto(random.randint(-500,0), random.randint(0,500))
#   body()

def random_color():
    rgbl=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return tuple(rgbl)

def fish():
  for i in range(5):
    randColor = random_color()
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    turtle.Turtle().penup()
    body(rand1, rand2, randColor)
    


fish()

turtle.done()