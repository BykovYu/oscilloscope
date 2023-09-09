import turtle as t
import random as r

weight = 550 // 2
height = 550 // 2
t.colormode(255)
t.Screen().bgcolor(0,0,0)
t.pencolor(100, 100, 100)
t.tracer(2, 1)
t.hideturtle()
def t_c_x(x):#transform coordinats
    if x<0: x = -weight
    elif x>weight * 2 - 1: x = weight
    else: x = -weight + x
    return x
def t_c_y(y):#transform coordinats
    if y<0: y = -height
    elif y>weight * 2 - 1: y = weight
    else: y = -weight + y
    return y
def draw_grid(delta):
    t.penup()
    x0, y0 = t_c_x(0), 0 + t_c_y(delta * (2 * height // 3)) + 3
    t.setposition(x0, y0)
    t.pendown()
    t.dot()
    t.penup()
    x_max, y_max = t_c_x(2 * weight), 0 + t_c_y((delta + 1) * (2 * height // 3))
    y_step = int((y_max - y0) / 10)
    print(y_max - y0)
    #vertical lines
    for x in range(x0 + y_step, x_max, y_step):
        t.setposition(x, y0)
        t.pendown()
        t.setposition(x, y_max)
        t.penup()
    #horizontal lines
    for y in range(y0 + y_step, y_max, y_step):
        t.setposition(x0, y)
        t.pendown()
        t.setposition(x_max, y)
        t.penup()
    print()
draw_grid(0)
draw_grid(1)
draw_grid(2)
t.done()