# direct_needle.py
# joseph fahnestock
# an interpretation of the program written in pseudocode on page 11
# of Statistical Mechanics by Werner Krauth with pebble-needle patch

from numpy import random as rnd # import random module from numpy
from numpy import sqrt

trials = int(input("How many trials would you like to run? "))
b = float(input("What is the width of your floor boards? "))
a = float(input("What is the length of your needle? "))
completed_trials = 0
hits = 0

while completed_trials < trials:
    # Complete number of trials user requested
    # test whether the (x,y) is within a unit circle
    x_center = (b/2 - 0)*rnd.random() # x: [0, b/2)
    dx, dy = 1, 1
    while sqrt(dx**2 + dy**2) > 1:
        dx = rnd.random() # y: [0, 1)
        dy = rnd.random() # y: [0, 1)
    g = sqrt(dx**2 + dy**2)
    x_tip = x_center - (a/2)*dx/g 
    if x_tip < 0:
        hits += 1
    completed_trials += 1

pi = (trials/float(hits))*2*b/a
print("There were " + str(hits) + " hits. The resultant approximation for pi is " + str(pi))

