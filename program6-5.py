# Filename: program6-5.py
# Author: J.Hayes
# Date: Oct. 21, 2019
# Purpose: To demonstrate the use and functioning
#       of random functions.
#       This script is based on figure 6-6. Coin Flipping simulation

import random

# Constant
NUMFLIPS = 10

for counter in range(NUMFLIPS):
    if (random.randint(0, 1) == 0):
        print('Heads')
    else:
        print('Tails')


