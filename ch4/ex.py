# Chapter 4 exercises

import turtle
import math

bob = turtle.Turtle()

def polygon(t, length, n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    
# polygon(bob, 40, 4)

def circle(t, r):
    circ = 2 * math.pi * r
    n = 3
    length = circ / n
    polygon(t, length, n)

# circle(bob, 100)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / math.pi) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# arc(bob, 30, 90)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

#petal(bob, 100, 70)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)

# flower(bob, 5, 100, 70)

def pie(t, length, n):
    """
    t: Turtle
    length: length of sides
    n: number of polygons
    """
    for i in range(n):
        polygon(t, length, 3)
        t.rt(360/n)

pie(bob, 50, 6)

turtle.mainloop()