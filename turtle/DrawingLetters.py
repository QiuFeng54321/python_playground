import turtle


t = turtle.Pen()
t.speed(0)
size = (turtle.getscreen().window_width(), turtle.getscreen().window_height())
quaters = (size[0] / 4, size[1] / 4)
scale = 10
std_pos = [0, 0]
pos_offset = (-size[0] / 2 + scale, size[1] / 2 - scale)
def get_abs_pos():
    return pos_offset[0] + std_pos[0] * scale * 6, pos_offset[1] - std_pos[1] * scale * 6

char_map: dict = {
    'A': [
        (1, 0, True),
        (2, 0, False),
        (1, -5, False),
        (-1, 0, False),
        (-0.5, 2, False),
        (-1, 0, False),
        (-0.5, -2, False),
        (-1, 0, False),
        (1, 5, False),
        (0.6, -1, True),
        (0.8, 0, False),
        (0.1, -1, False),
        (-1, 0, False),
         (0.1, 1, False)
    ],
    'T': [
        (5, 0, False),
        (0, -1, False),
        (-2, 0, False),
        (0, -4, False),
        (-1, 0, False),
        (0, 4, False),
        (-2, 0, False),
        (0, 1, False)
    ],
    'D': [
        (2, 0, False),
        (2, -5, False),
        (-4, 0, False),
        (0, 5, False),
        (0, -1, True),
        (1, 0, True),
        (0.5, 0, False),
        (1, -3, False),
        (-1.5, 0, False),
        (0, 3, False)
    ],
    ' ': []
}


def draw_char(arr, t: turtle.Pen, scale = 1):
    x, y = get_abs_pos()
    for dx, dy, penup in arr:
        x += dx * scale
        y += dy * scale
        if penup:
            t.penup()
        t.goto(x, y)
        t.pendown()
    std_pos[0] += 1
    t.penup()
    t.goto(get_abs_pos())
    t.pendown()

def new_line(t: turtle.Pen, scale = 1):
    std_pos[0] = 0
    std_pos[1] += 1


print(size)
t.penup()
t.goto((-size[0] / 2 + 20, size[1] / 2 - 20))
t.pendown()
draw_char(char_map['A'], t, scale)
draw_char(char_map['D'], t, scale)
draw_char(char_map['D'], t, scale)
draw_char(char_map[' '], t, scale)
draw_char(char_map['T'], t, scale)
new_line(t, scale)
draw_char(char_map['A'], t, scale)
input()