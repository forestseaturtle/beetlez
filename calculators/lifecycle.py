# This calculator is going to give you and idea of the average lifecycle expectations of
# organisms in the colony.

#Import Portion

import random

# Initial Defining Portion

family1_1 = random.randint(4, 19)
family1_2 = random.randint(4, 19)
family1_3 = random.randint(4, 19)
family2_1 = random.randint(9, 20)
family2_2 = random.randint(9, 20)
family2_3 = random.randint(9, 20)

# Mathematics Portion

family1_addition = family1_1 + family1_2 + family1_3
family2_addition = family2_1 + family2_2 + family2_3

family1 = family1_addition / 3
family2 = family2_addition / 3

# Display Portion

print (family1, "Days, on average, until eggs hatch")
print (family2, "Number, on average, of instars of the pupa")
