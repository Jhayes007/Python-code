# Filename: Program8-16.py
# Author: J.Hayes
# Date: Nov. 18, 2019
# Purpose: To demonstrate the use of two-dimensional arrays.
#           On page 392, this is an example of referencing 2D arrays.

# Constants for rows and columns
ROWS = 3
COLS = 4
# Creating a 2D array with 3 rows and 4 columns in Python
Values = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 

# Read values into the array
for row in range(ROWS):
    for col in range(COLS):
        Values[row][col] = int(input('Enter an integer: '))
# End of the nested for loops

# Display the values in the array
print('Here are the values held in the array: ')
for row in range(ROWS):
    for col in range(COLS):
        print(Values[row][col])
# end of nested loops

