import turtle as t
import random as r

weight = 550 // 2
height = 550 // 2
t.colormode(255)
t.Screen().bgcolor(0,0,0)
t.pencolor(255, 255, 255)
t.tracer(2, 10)
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
    t.setposition(t_c_x(0), t_c_y(0))
    t.pendown()
    t.setposition(t_c_x(2*weight), t_c_y(2*height))
    t.setposition(t_c_x(2 * weight), t_c_y(2 * height))
draw_grid(0)
t.done()