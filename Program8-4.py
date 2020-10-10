# Filename: Program8-4.py
# Author: J.Hayes
# Date: Nov. 6, 2019
# Purpose: To demonstrate the use of arrays. In python there
#           are no true arrays as in traditional languages.
#           We will use lists to simulate arrays.
#           This script is based on the algorithim Figure 8-4 on page 360.

# Constant for array size
SIZE = 6
# Declare the array
hours = [0] * SIZE

# Get the work hours for each employee
for index in range(SIZE):
    print('Enter the hours worked by ', end='')
    print('employee', index+1, ': ', end='')
    hours[index] = float(input())

# Get the hourly pay rate
payRate = float(input('Enter the hourly pay rate: '))

# Display the gross pay of each employee
print("Here is each employee's gross pay: ")
for index in range(SIZE):
    grossPay = hours[index] * payRate
    print('Employee ', index+1, '$%.2f' % grossPay)

