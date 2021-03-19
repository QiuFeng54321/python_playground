import turtle

t: turtle.Pen = turtle.Pen()
t.pencolor("pink")
t2: turtle.Pen = turtle.Pen()
t2.pencolor(173 / 256, 216 / 256, 230 / 256)
t.speed(1000)
t2.speed(1000)
t2.left(181)
i: int = 0


def step(t: turtle.Pen):
    t.penup()
    t.forward(i)
    t.left(46)
    t.pendown()
    t.dot(4 + i / 16)


while True:
    step(t)
    step(t2)
    i += 1
