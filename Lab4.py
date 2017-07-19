# CS61002: Algorithms and Programming 1
# Name: Matt Gates
# Date: 7/6/2017
# Lab4.py

print ('********** Exercise 1**********')

import turtle
import math

def moveAndTurn(amount):
    turtle.forward(amount)
    turtle.left(90)

def draw_rectangle(length, height, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        moveAndTurn(length)
        moveAndTurn(height)
    turtle.end_fill()


def draw_star(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


def get_color(color):
    colors = {
        "red": [.698, .132, .203],
        "white": [1.000, 1.000, 1.000],
        "blue": [.234, .233, .430],
    }

    return colors[color]

def draw_stars(flagHeight, unionHeight, stripeHeight, unionLength):
    # Star color
    color = get_color('white')

    # Star variables
    starSize = 4 / 5 * stripeHeight
    size = 1 / 3 * starSize
    x = unionLength / 12
    x_divided = x / 2
    y = unionHeight / 10

    for i in range(9):
        y_divided = flagHeight - unionHeight + i * y + y
        if i % 2:
            for z in range(5):
                turtle.penup()
                turtle.goto(x_divided + x + 2 * x * z, y_divided)
                turtle.pendown()
                draw_star(size, color)
        else:
            for z in range(6):
                turtle.penup()
                turtle.goto(x_divided + 2 * x * z, y_divided)
                turtle.pendown()
                draw_star(size, color)


def draw_flag(height):
    flagHeight, flagLength = float(height), float(1.9 * height)
    unionHeight, unionLength = float(7 / 13 * height), float(2 / 5 * flagLength)
    stripeHeight = float(height / 13)

    for i in range(14):
        color = get_color('white') if i % 2 else get_color('red')
        x, y = 0, i * (1 / 13) * flagHeight

        if i < 6:
            length, height = flagLength, stripeHeight

        elif i >= 6 and i < 13:
            x, length, height = unionLength, flagLength - unionLength, stripeHeight

        elif i == 13:
            color = get_color('blue')
            y, length, height = 6 / 13 * flagHeight, unionLength, unionHeight

        turtle.goto(x, y)
        draw_rectangle(length, height, color)

    draw_stars(flagHeight, unionHeight, stripeHeight, unionLength)

def begin() :
    turtle.speed('fastest')
    draw_flag(200)
    turtle.hideturtle()
    turtle.done()

begin()
