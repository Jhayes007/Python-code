# Filename: Program8-15.py
# Author: J.Hayes
# Date: Nov. 18, 2019
# Purpose: To demonstrate the use of parallel arrays. On pages 388-389

# Array size (number of employees)
SIZE = 6
# Array to hold employee names
names = [''] * SIZE
# Array to hold employee's hours worked
hours = [0] * SIZE
# Names and hours are parallel arrays

# Get each employee's data
for index in range(SIZE):
    # Get the employee's name
    print('Enter the name of employee ', index+1, ': ', end='')
    names[index] = input()
    # Get the hours worked of this employee
    print('Enter the hours worked by that employee: ', end='')
    hours[index] = float(input())

# Get the hourly pay rate
payRate = float(input('Enter the hourly pay rate: '))
# Display the gross pay for each employee
print("Here is each employees's gross pay: ")
for index in range(SIZE):
    grossPay = hours[index] * payRate
    # print(names[index], ': %.2f' % grossPay)
    print('{:15s}: ${:,.2f}'.format(names[index], grossPay))

