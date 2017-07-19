# CS61002: Algorithms and Programming 1
# Name: Matt Gates
# Date: 7/1/17
# Lab3.py

import random
import turtle
import time
import math

# Fun colors to print in terminal with
class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print ("")
print ("")
print (c.OKBLUE + "+++++++++++++++++++Exercise 1+++++++++++++++++++" + c.ENDC)
print ("")
print ("This program draws squares of many colors.")
print ("")
print ("")

turnAngle = 40 # The angle at which to turn
turnCount = 4 # The amount of turns to draw a square.
turtleSpeed = math.pow(10, 10) # How fast we should draw

question = "Enter the number of squares to draw: "
errorMessage = "The number must be an integer greater than or equal to 1."

def turn(x):
    for i in range(x):
        turtle.forward(100)
        turtle.left(90)

# Perpetual loop until a valid integer >= 1 is given
while True:
    num_squares = input(c.WARNING + "Input: " + c.ENDC + question)
    if num_squares.isdigit() and int(num_squares) >= 1: break
    print (c.FAIL + "Error: " + c.ENDC + errorMessage)
    print ("")
    print ("")

# Increase the speed of turtle so we don't have to wait too long
turtle.speed(turtleSpeed)

for i in range(int(num_squares)):
    # Give a new color for each square
    turtle.color(random.random(), random.random(), random.random())
    turtle.begin_fill()
    turtle.left(turnAngle)
    turn(turnCount)
    turtle.end_fill()

time.sleep(5) # Sleep to see the pretty masterpiece
