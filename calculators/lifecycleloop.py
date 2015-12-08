# This calculator is an automatic version of lifecycles.py that will give you 100 solutions to a specific life event of the mealworms

import random

# While loop for iterating over this 100 times automatically
i = 0

while i < 100:
    if i <= 100:
        pupate = random.randint(15, 75)
        adult = random.randint(10, 20)
        eggday = random.randint(5, 10)
        egghatch = random.randint(7, 14)
        deadbeetleday = 30 - egghatch
        age1 = pupate + 15
        age2 = adult + age1
        age3 = eggday + age2
        age4 = egghatch + age3
        deadbeetle = age4 + deadbeetleday
        i = i + 1
        print(age3)
        with open("lifecyclelog.txt", "a") as myfile:
            myfile.write(str(age3))
            myfile.write("\n")
