import turtle as t
import random as r

weight = 700 // 2
height = 800 // 2
t.colormode(255)
t.Screen().bgcolor(0,0,0)
t.pencolor(100, 100, 100)
t.tracer(2, 10)
t.hideturtle()
def draw_grid():
    step_grid = 30
    t.penup()
    t.setposition(-weight, -height)
    t.pendown()
    t.setposition(weight, -height)
    t.setposition(weight, height)
    t.setposition(-weight, height)
    t.setposition(-weight, -height)
    for y in range(-height + step_grid, height, step_grid):
        t.setposition(x=-weight, y=y)
        t.setposition(x=weight, y=y)
draw_grid()
t.done()