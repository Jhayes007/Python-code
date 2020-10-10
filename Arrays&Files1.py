# Filename: Arrays&Files1.py
# Author: J. Hayes
# Date: Dec. 2, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on page 490-491. Demonstrates how elements of an
#           array can be written to a file and read back into an array.

# Reading the array from the file
index = 0 # The loop control variable
numbers = []


# Open the file
numberFile = open('values.txt', 'r')
# Read from the file and put the records in the array
for line in numberFile:
    line = line.rstrip()
    numbers.append(line)
    
# close the file
numberFile.close()


# Display the array
for index in range(len(numbers)):
    print(numbers[index])


