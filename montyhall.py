##############################
# Written by Steven Kaplan
# email: smkaplan87@gmail.com
##############################

from numpy.random import randint
nTrials = 1000000

nShouldStay = 0
nShouldSwitch = 0

for i in range(nTrials):
    doorWithCar = randint(1,4) #random integer, either 1, 2, or 3
    doors = {

    }

    if doorWithCar == 1:
        doors[1] = "car"
        doors[2] = "goat"
        doors[3] = "goat"
    elif doorWithCar == 2:
        doors[1] = "goat"
        doors[2] = "car"
        doors[3] = "goat"
    elif doorWithCar == 3:
        doors[1] = "goat"
        doors[2] = "goat"
        doors[3] = "car"

    firstGuess = randint(1,4)
    if (doors[firstGuess] == "car"):
        nShouldStay += 1
    else:
        nShouldSwitch += 1

print "########################"
print "#"
print "# Results:"
print "#"
print "# nShouldStay = %i"%nShouldStay
print "# nShouldSwitch = %i"%nShouldSwitch
print "#"
print "# pShouldStay = %.4f"%(1.*nShouldStay/(nShouldStay+nShouldSwitch))
print "# pShouldSwitch = %.4f"%(1.*nShouldSwitch/(nShouldStay+nShouldSwitch))
print "########################"