import random
import statistics
from turtle import Turtle

#defining variables, list
name = input("Please enter Pa, Mi-Ma, or Reg: ")
stepper = int(input("Please input number of steps: "))
trials = int(input("Please input number of trials: "))
total = 0
list = []
t = Turtle()

#defining places to move depending on selection
def pa_walk(steps):
  (x,y) = (0,0)
  for i in range(steps):
    (dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
    x += dx
    y += dy
  return (x,y)

def ma_walk(steps):
  (x,y) = (0,0)
  for i in range(steps):
    (dx, dy) = random.choice([(0,1), (0,-2), (1,0), (-1,0)])
    x += dx
    y += dy
  return (x,y)

def reg_walk(steps):
  (x,y) = (0,0)
  for i in range(steps):
    (dx, dy) = random.choice([(1,0), (-1,0)])
    x += dx
    y += dy
  return (x,y)

def plot(data, color):
  t.up()
  t.goto(data)
  t.dot(5, color)
  t.down()

for i in range(trials):
# selects proper function to use
  if name == 'Pa':
    walk = pa_walk(stepper)
    # print(walk)
    list.append(abs(walk[0]) + abs(walk[1]))
    total += abs(walk[0]) + abs(walk[1])
    plot(walk, "blue")
  elif name == 'Mi-Ma':
    walk = ma_walk(stepper)
    list.append(abs(walk[0]) + abs(walk[1]))
    total += abs(walk[0]) + abs(walk[1])
    plot(walk, "green")
  elif name == 'Reg':
    walk = reg_walk(stepper)
    list.append(abs(walk[0]) + abs(walk[1]))
    total += abs(walk[0]) + abs(walk[1])
    plot(walk, "red")


#print data
mean = total // trials
print(f"{name} random walk of {str(stepper)} steps")
print(f"mean: {str(mean)}")
print(f"max: {str(max(list))}")
print(f"min: {str(min(list))}")
# print(list)

#print CV
print(f"CV: {str(round(statistics.pstdev(list)/mean,2))}")
t.ht()
t.screen.exitonclick()