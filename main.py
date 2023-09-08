import turtle as t
import random as r

weight = 550 // 2
height = 550 // 2
t.colormode(255)
t.Screen().bgcolor(0,0,0)
t.pencolor(100, 100, 100)
t.tracer(2, 10)
t.hideturtle()
def draw_grid(delta):
    step_grid = height * 2 // 3 - 10
    delta = delta * (height * 2 // 3 + 3)
    t.penup()
    t.setposition(x=-weight, y=-height + delta)
    t.pendown()
    t.setposition(x=weight, y=-height + delta)
    t.setposition(x=weight, y=-height + height * 2 // 3 + delta)
    t.setposition(x=-weight, y=-height + height * 2 // 3 + delta)
    t.setposition(x=-weight, y=-height + delta)
draw_grid(0)
draw_grid(1)
draw_grid(2)
t.done()