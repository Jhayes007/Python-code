# Filename: Program10-13.py
# Author: J. Hayes
# Date: Dec. 4, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on page 508. Demonstrates how elements of an
#           array can be written to a file and read back into an array.

import os # For deleting and renaming files

# Create a file variable and set it to false
found = False
# Create a file variable and open the coffee.txt file
coffeeFile = open('coffee.txt', 'r')
# Open a temporary file
tempFile = open('temp.txt', 'w')
# Get the search value
searchValue = input('Enter the coffee you wish to delete: ')
# Priming read
line = coffeeFile.readline()
# The loop
while (line != ''):
    description, quantity = line.rstrip.split(',')
    # Write this record if it is not to be deleted
    if (description.lower().find(searchValue.lower()) < 0):
        tempFile.write(description + ',' + quantity + '\n')
    line = coffeeFile.readline() # Next record
# Close files
coffeeFile.close()
tempFile.close()

# Delete original file and rename temp file
os.remove('coffee.txt')
os.rename('temp.txt', 'coffee.txt')

# Indicate if the record was deleted
print('The record has been updated.')
