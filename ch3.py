## Chapter 3 -- Functions

type(42) # a function call

int('32') # casts to int
float('3.1415') # casts to float
str(32) # casts to string

import math # imports math module object
# ratio = signal_power / noise_power
# decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)

# Composition
# x = math.sin(degrees / 360 * 2 * math.pi)

# Function definitions
def print_lyrics():
    print("I'm a lumberjack, and I'm OK.")
    print("I sleep all night and I work all day")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# repeat_lyrics()

def right_justify(string):
    repeat = 70 - len(string) 
    print((" " * repeat) + string)

# right_justify('aos')

def do_twice(f, v1, v2):
    f(v1, v2)
    f(v1, v2)

def print_twice(string):
    print(string)
    print(string)

# do_twice(print_twice, 'hello')

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

# do_four(print, 'hello')

def draw_plus():
    print('+', end=' ')

def draw_hline():
    print('- ' * 4, end='')

def draw_vline():
    print('|', end='')
    print(' ' * 8, end=' ')
    print('|', end='')
    print(' ' * 8, end=' ')
    print('|', end='')
    print(' ' * 8, end=' ')
    print('|', end='')
    print(' ' * 8, end=' ')
    print('|')
    
def alternate_once(f_one, f_two):
    f_one()
    f_two()

def do_four(f):
    f()
    f()
    f()
    f()


def draw_grid():
    alternate_once(draw_plus, draw_hline)
    alternate_once(draw_plus, draw_hline)
    draw_plus()
    print()
    do_four(draw_vline)
    alternate_once(draw_plus, draw_hline)
    alternate_once(draw_plus, draw_hline)
    draw_plus()
    print()
    do_four(draw_vline)
    alternate_once(draw_plus, draw_hline)
    alternate_once(draw_plus, draw_hline)
    draw_plus()
    print()

def draw_big():
    do_twice(alternate_once, draw_plus, draw_hline)
    do_twice(alternate_once, draw_plus, draw_hline)
    draw_plus()
    print()
    do_four(draw_vline)
    do_twice(alternate_once, draw_plus, draw_hline)
    do_twice(alternate_once, draw_plus, draw_hline)
    draw_plus()
    print()
    do_four(draw_vline)
    do_twice(alternate_once, draw_plus, draw_hline)
    do_twice(alternate_once, draw_plus, draw_hline)
    draw_plus()
    print()
    do_four(draw_vline)
    do_twice(alternate_once, draw_plus, draw_hline)
    do_twice(alternate_once, draw_plus, draw_hline)
    draw_plus()
    print()
    do_four(draw_vline)
    do_twice(alternate_once, draw_plus, draw_hline)
    do_twice(alternate_once, draw_plus, draw_hline)
    draw_plus()
    print()

draw_big()