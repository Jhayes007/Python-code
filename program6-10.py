# Filename: program6-10.py
# Author: J.Hayes
# Date: Oct. 23, 2019
# Purpose: To demonstrate the use of a 
#      user-defined function.
#      This script is based on program 6-10
#      This script uses pre-defined mathematical functions.

import math

# Get the first side of a right triangle
a = float(input('Enter the length of side A: '))
# Get the second side of the triangle
b = float(input('Enter the length of side B: '))
# Calculate the length of the hypotenuse
c = math.sqrt(a**2 + b**2)
# Display the result
print('The length of the hypotenuse is ', c)
