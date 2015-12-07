# This calculator is going to attempt to calculate the rate at which beetles and eggs will be produced by the colony

# Imports

import random

# Introduction

print ()
print ()
print ("Please enter the amount of worms you are starting with: ")
print ()
print ()

# Initial worm entry

worm0 = int(input("How many worms you got - "))
print ()
print ()


# Explination of age calculation

print("The average time for the mealworm to begin a pupa is between 30 and 90 days. We will assume that you got these in the mail. That being said, it is likely that they are at the middle of their lifetimes - so let us assume they are 15 days old when you get them. What this means is that the range of days before they hatch is between 15 and 75 days from this point.")
print ()
print ()

# Age calculation for pupation

pupate = random.randint(15, 75)
age1 = pupate + 15

print ("It was randomly determine that your eegs would hatch on this day out of a possible remaining 75: ", pupate)
print ("This means your mealworms are", age1, "days old when they hatch.")
print ()
print ()

# Age calculation for adulthood

adult = random.randint(10, 20)
age2 = adult + age1

print ("It takes between 10-20 days for a pupa to turn into an adult beetle. Here we have randomly chosen one of those days: ", adult)
print ("This means your mealworms are", age2, "days old when they become adult beetles.")
print ()
print ()

# Age calculation to lay eggs

eggday = random.randint(5, 10)
age3 = eggday + age2

print ("It takes between 5-10 days for an adult beetle to lay eggs. Here we have randomly chosen one of those days: ", eggday)
print ("This means your mealworms are", age3, "days old when they lay their eggs")
print ()
print ()

# Age calculation to hatch eggs

egghatch = random.randint(7, 14)
age4 = egghatch + age3

print ("It takes between 7-14 days for the eggs to hatch. Here we have randomly chosen one of those days: ", egghatch)
print ("This means your mealworms are", age4, "days old when their eggs hatch")
print ()
print ()

# Age calculation of death

deadbeetleday = 30 - egghatch
deadbeetle = age4 + deadbeetleday

print ("Assuming that the average adult beetle lifespan is 30 days, your beetles died when they were", deadbeetle, "days old.")
print ()
print ()
