# FileName: Program 10-8.py
# Author: J. Hayes
# Date: Dec. 2, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on page 494-495. Demonstrates how elements of an
#           array can be written to a file and read back into an array.

# Create a file variable and open the file
employeeFile = open('employees.txt', 'r')

print('Here are the employee records: ')

# Priming read
line = employeeFile.readline().rstrip()
while (line != ''):
    name, idNumber, department = line.split(',')
    print('Name: ', name)
    print('ID Number: ', idNumber)
    print('Department: ', department)
    print()
    line = employeeFile.readline().rstrip() # Next line
# Close the file
employeeFile.close()
