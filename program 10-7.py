# FileName: Program 10-7.py
# Author: J. Hayes
# Date: Dec. 2, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on page 490-491. Demonstrates how elements of an
#           array can be written to a file and read back into an array.

# Create a file variable and open the file
employeeFile = open('employees.txt', 'w')
# Get the number of employees
numEmployees = int(input('How many employee records do you ' \
                         'want to create?: '))
# Get the employee's data and write it to the file
for counter in range(numEmployees):
    # Get the employee's name
    print('Enter the name of the employee #', (counter+1), ': ', end='')
    name = input()
    # Get the employee's id
    idNumber = int(input("Enter the employee's ID number: "))
    # Get the employee's department
    department = input("Enter the employee's department: ")
    # Write the record to the file
    employeeFile.write(name + ' , ' + str(idNumber) + ' , ' + \
                       department + '\n')
# Close the file
employeeFile.close()
print('Employee records written to the file employees.txt.')
