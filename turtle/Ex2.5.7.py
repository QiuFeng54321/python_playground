import turtle
t = turtle.Pen()
t.speed(0)
def pen_up_goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def circ(times):
    for i in range(times):
        t.circle(50)
        t.penup()
        t.forward(100)
        t.pendown()

pen_up_goto(-100, -350)
c = 10 * 75 ** 0.5
circ(3)
pen_up_goto(-50, -350 + c)
circ(2)
pen_up_goto(0, -350 + 2 * c)
circ(1)
input()