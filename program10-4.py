# Filename: Program10-4.py
# Author: J.Hayes
# Date: Nov. 25, 2019
# Purpose: To demonstrate how to create a file object, open a file,
#           read from a file, and close a file.
#           This script is based on Figure 10-14 on pg. 485
#           This is an example of using a loop to process a file.

# Create a file object and open a file named "sales.txt"
infile = open('sales.txt', 'r')

print('Here are the sales amounts from the file: ')
# Priming Read
line = infile.readline()
while (line != ''):
    print('${:,.2f}'.format(int(line)))
    line = infile.readline()

# Close the file
infile.close()
