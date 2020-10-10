# Filename: Program10-3.py
# Author: J.Hayes
# Date: Nov. 25, 2019
# Purpose: To demonstrate how to create a file object, open a file,
#           write to a file, and close a file.
#           This script is based on Figure 10-13 on pg. 483
#           This is an example of using a loop to process a file.

# Create a file object and open a file named "sales.txt"
outfile = open('sales.txt', 'w')

# Get the number of days of data
numDays = int(input('For how many days do you have sales? '))

# Get the amount of sales for each day and write it to the file
for counter in range(1, numDays+1):
    print('Enter the sales for day # ', counter, ': ', end='')
    sales = input() # Just to write to a file, not for calc
    # Write to the file
    outfile.write(sales + '\n')

# Close the file
outfile.close()
print('Data written to the file sales.txt')

