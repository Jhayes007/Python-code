# Filename: Program10-11.py
# Author: J. Hayes
# Date: Dec. 4, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on page 490-491. Demonstrates how elements of an
#           array can be written to a file and read back into an array.

# Create a file variable and open the file
coffeeFile = open('cofee.txt', 'r')
# Create a flag and set it to false
found = False

# Get the value to search for
searchValue = input('Enter a value to search for: ')
# Loop to search for the record
line = coffeeFile.readline().rstrip()   # The priming read
while (line != ''):
    description, quantity = line.split(',')
    if (description.find(searchValue) >= 0):
        print('Description: ', description, ' Quantity: ', \
              float(quantity), ' pounds.')
        found = True
    line = coffeeFile.readline().rstrip() # Read next record

# if the value isn't found, display a message
if (not(found)):
    print(searchValue, ' was not found.')

# Close the file
coffeeFile.close()

