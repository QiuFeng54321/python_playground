import turtle

t = turtle.Pen()
t.speed(1)
size = (turtle.getscreen().window_width(), turtle.getscreen().window_height())
quaters = (size[0] / 4, size[1] / 4)
print(size)
t.goto((-size[0] / 2, size[1] / 2))

for i in range(3):
    t.forward(size[0])
    t.right(90)
    t.forward(quaters[1])
    t.right(90)
    t.forward(size[0])
    t.left(90)
    t.forward(quaters[1])
    t.left(90)

input()
