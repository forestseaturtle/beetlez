# This calculator is a headless version of lifecycles.py

# Initial worm entry

worm0 = int(input("How many worms you got - "))

# Age calculation for pupation

pupate = random.randint(15, 75)
age1 = pupate + 15

# Age calculation for adulthood

adult = random.randint(10, 20)
age2 = adult + age1

# Age calculation to lay eggs

eggday = random.randint(5, 10)
age3 = eggday + age2

# Age calculation to hatch eggs

egghatch = random.randint(7, 14)
age4 = egghatch + age3

# Age calculation of death

deadbeetleday = 30 - egghatch
deadbeetle = age4 + deadbeetleday
