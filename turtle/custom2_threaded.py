import turtle, threading, queue

t: turtle.Pen = turtle.Pen()
t.pencolor("pink")
t2: turtle.Pen = turtle.Pen()
t2.pencolor(173 / 256, 216 / 256, 230 / 256)
t.speed('fastest')
t2.speed('fastest')
t2.left(181)
i: int = 0


def step(t: turtle.Pen):
    graphics.put((t.penup, ))
    graphics.put((t.forward, i))
    graphics.put((t.left, 46))
    graphics.put((t.pendown, ))
    graphics.put((t.dot, 4 + i / 16))

def step_thread(para: turtle.Pen = None, sleep = 0):
    while True:
        step(para)
        global i
        i += 1

def process_queue():
    while not graphics.empty():
        ele = graphics.get()
        (ele[0])(*ele[1:])

    if threading.active_count() > 1:
        turtle.ontimer(process_queue, 100)

graphics = queue.Queue(1)
thread_t1 = threading.Thread(target=step_thread, args=(t, ))
thread_t2 = threading.Thread(target=step_thread, args=(t2, ))
thread_t1.start()
thread_t2.start()

process_queue()

