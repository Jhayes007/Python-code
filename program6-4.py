# Filename: program6-4.py
# Author: J.Hayes
# Date: Oct. 21, 2019
# Purpose: To demonstrate the use and functioning
#       of random functions.
#       This script is based on figure 6-5. Rolling dice

import random

# The loop control variable
again = 'y'
# Simulate the die roll
while (again == 'y' or again == 'y'):
    print('Rolling the dice...')
    print('Their values are: ')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    # Do another roll of dice?
    again = input('Roll them again? (y = yes): ')


