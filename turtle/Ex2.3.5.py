import turtle
t = turtle.Pen()

dimensions = (50, 100)

for i in range(4):
    t.forward(dimensions[i % 2])
    t.left(90)

input()