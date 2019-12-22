# direct_pi.py
# joseph fahnestock
# an interpretation of the program written in pseudocode on page 3
# of Statistical Mechanics by Werner Krauth

from numpy import random as rnd # import random module from numpy

trials = int(input("How many trials would you like to run? "))
completed_trials = 0
hits = 0

while completed_trials < trials:
    # Complete number of trials user requested
    # test whether the (x,y) is within a unit circle
    x = 2*rnd.random() - 1 # x: [-1, 1)
    y = 2*rnd.random() - 1 # y: [-1, 1)
    if (x**2 + y**2) < 1:
        hits += 1
    completed_trials += 1

pi = 4*(float(hits)/completed_trials)
print("There were " + str(hits) + " hits. The resultant approximation for pi is " + str(pi))

