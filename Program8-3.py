# Filename: Program8-3.py
# Author: J.Hayes
# Date: Nov. 6, 2019
# Purpose: To demonstrate the use of arrays. In python there
#           are no true arrays as in traditional languages.
#           We will use lists to simulate arrays.
#           This script is based on Program 8-3 on page 356.

# Constant for array size
SIZE = 3
# Declare the array
hours = [0] * SIZE

# Read values into the array
for index in range(SIZE):
    print('Enter the hours worked by ', end='')
    print('Employee number ', index+1, ': ', end='')
    hours[index] = int(input())

# Display the elements of the array
print('The hours you entered are: ')
for index in range(SIZE):
    print(hours[index], '  ', end='')
    
