# Filename: Arrays&Files.py
# Author: J. Hayes
# Date: Dec. 2, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on page 490-491. Demonstrates how elements of an
#           array can be written to a file and read back into an array.


SIZE = 5
numbers = [10, 20, 30, 40, 50]

# Writing the array to a file
index = 0 # The loop control variable
numberFile = open('values.txt', 'w')

# Writing the elements of the array to the file
for index in range(SIZE):
    numberFile.write(str(numbers[index]) + '\n')

numberFile.close()  # close the file
print('All the elements of the array have been written to the file.')



