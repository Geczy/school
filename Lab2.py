# CS61002: Algorithms and Programming 1
# Name: Matt Gates
# Date: 6 / 22 / 2017
# Lab #2.py

import math

print ("********** Exercise 1 **********")

side = float(input("What is the side length (in feet) of the finished garden? "))
spacing = float(input("What is the recommended spacing (in feet) between plants? "))
depthBeds = float(input("What is the depth (in feet) of the flowerbeds? "))
depthFilled = float(input("What is the depth (in feet) of the filled areas? "))

r = side / 4
initVolume = math.pi * (r * r) * depthBeds
initArea = math.pi * r * r

plantsForSemi = math.trunc((initArea / 2) / (spacing * spacing))
plantsForCircle = math.trunc(initArea / (spacing * spacing))
plantsTotal = plantsForCircle + (plantsForSemi * 4)

volume = initVolume / 2
soilForSemi = round(volume / 27, 1)

soilForCircle = round(initVolume / 27, 1)

totalSoil = round((soilForSemi * 4) + soilForCircle, 1)

volume = (side * side) * depthFilled
volumeCircle = initVolume * 3
totalFill = round((volume - volumeCircle) / 27, 1)

print("----------------------------------")
print("Requirements")

print('Plants for each semicircle garden: {}'.format(plantsForSemi))
print('Plants for the circle garden: {}'.format(plantsForCircle))
print('Total plants for garden: {}'.format(plantsTotal))

print('Soil for each semicircle garden: {} cubic yards'.format(soilForSemi))
print('Soil for the circle garden: {} cubic yards'.format(soilForCircle))

print('Total soil for the garden: {} cubic yards'.format(totalSoil))
print('Total fill for the circle garden: {} cubic yards'.format(totalFill))
