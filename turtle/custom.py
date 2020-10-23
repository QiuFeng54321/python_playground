import turtle

t: turtle.Pen = turtle.Pen()
t.pencolor("pink")
t.speed(1000)
i: int = 0

while True:
    t.circle(i / 1.5)
    t.left(1)
    i += 1

