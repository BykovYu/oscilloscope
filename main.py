import turtle as t
from math import sin, pi
import random as r

weight = 550 // 2
height = 550 // 2
coordinats_grids = [{}, {}, {}]
t.colormode(255)
t.Screen().bgcolor(0,0,0)
t.pencolor(100, 100, 100)
t.speed(1)
t.tracer(1, 1)
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
    coordinats_grids[delta]['x0'] = x0
    coordinats_grids[delta]['y0'] = y0
    t.setposition(x0, y0)
    t.pendown()
    t.dot()
    t.penup()
    x_max, y_max = t_c_x(2 * weight), 0 + t_c_y((delta + 1) * (2 * height // 3))
    coordinats_grids[delta]['x_max'] = x_max
    coordinats_grids[delta]['y_max'] = y_max
    y_step = int((y_max - y0) / 10)
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

draw_grid(0)
draw_grid(1)
draw_grid(2)
kanals = [t.Turtle(), t.Turtle(), t.Turtle()]
for i in range(len(kanals)):
    kanals[i].hideturtle()
    kanals[i].penup()
    y = coordinats_grids[i]['y0'] + (coordinats_grids[i]['y_max'] - coordinats_grids[i]['y0']) // 2
    kanals[i].setposition(x=coordinats_grids[i]['x0'], y=y)
    kanals[i].pencolor((48, 213, 200) if i==0 else (255, 255, 0) if i==2 else (139, 0, 255))
    kanals[i].pendown()
for x in range(-weight, weight, 10):
    print(x, end=' ')
    for i in range(len(kanals)):
        sr_y = coordinats_grids[i]['y0']+(coordinats_grids[i]['y_max']-coordinats_grids[i]['y0']) / 2
        kanals[i].setposition(x, sr_y+45*sin(2*pi*x/200))

print(*coordinats_grids, sep='\n')
t.done()