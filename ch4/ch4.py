# Chapter 4 - Interface design

import turtle
import math
bob = turtle.Turtle()

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)
    
# turtle.mainloop()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

    turtle.mainloop()
# square(bob, 300)

def polygon(t, length, n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polygon(bob, 100, 3)

def circle(t, r):
    circ = 2 * math.pi * r
    n = 30
    length = circ / n
    polygon(t, length, n)

# circle(bob, 100)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(bob, 100, 330)