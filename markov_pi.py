# markov_pi.py
# joseph fahnestock
# an interpretation of the program written in pseudocode on page 7
# of Statistical Mechanics by Werner Krauth

from numpy import random as rnd # import random module from numpy

trials = int(input("How many trials would you like to run? "))
d = float(input("What is the maximum distance of a new trial? "))
completed_trials = 0
x, y = 1, 1
hits = 0

while completed_trials < trials:
    # Complete number of trials user requested
    # test whether the (x, y) is within the unit square
    # test whether the (x,y) is within a unit circle
    dx = 2*d*rnd.random() - d # x: [-d, d)
    dy = 2*d*rnd.random() - d # y: [-d, d)
    if (abs(x+dx) < 1) and (abs(y+dy) < 1):
        x += dx
        y += dy
    if (x**2 + y**2) < 1:
        hits += 1
    completed_trials += 1

pi = 4*(float(hits)/completed_trials)
print("There were " + str(hits) + " hits. The resultant approximation for pi is " + str(pi))

