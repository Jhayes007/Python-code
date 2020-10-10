# Filename: Program10-12.py
# Author: J. Hayes
# Date: Dec. 4, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on paged 504-505. Demonstrates how elements of an
#           array can be written to a file and read back into an array.

import os # For deleting and renaming files

# Create a file variable and set it to false
found = False
# Create a file variable and open the coffee.txt file
coffeeFile = open('coffee.txt', 'r')
# Open a temporary file
tempFile = open('temp.txt', 'w')
# Get the search value
searchValue = input('Enter the coffee you wish to update: ')
# Get the new quantity
newQty = float(input('Enter the new quantity: '))

# The priming read
line = coffeeFile.readline().rstrip()
# The loop
while (line != ''):
    description, quantity = line.split(',')
    # Write this record to the temporary file, or the new
    # record if the following condition is true
    if (description.find(searchValue) >= 0):
        tempFile.write(description + ',' + str(newQty) + '\n')
        found = True
    else:
        tempFile.write(description + ',' + str(quantity) + '\n')
    # Read the next record
    line = coffeeFile.readline().rstrip()
# Close the file
coffeeFile.close()
tempFile.close()

# Delete the original file
os.remove('coffee.txt')
# Rename the temporary file
os.rename('temp.txt', 'coffee.txt')

# Indicate if the operation was successful
if found:
    print('The record was updated.')
else:
    print(searchValue, ' was not found in the file.')
