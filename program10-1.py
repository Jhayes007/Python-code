# Filename: Program10-1.py
# Author: J.Hayes
# Date: Nov. 25, 2019
# Purpose: To demonstrate how to create a file object, open a file
#           write to a file, and close the file.
#           This is based on Figure 10-4 on pg. 474.

# Create a file object and open a file named "philosophers.txt"
outfile = open('philosophers.txt', 'a')

# Write the names of some philosophers to the file
outfile.write('James\n')
outfile.write('Einstein\n')
outfile.write('Descartes\n')
outfile.write('Bach\n')
outfile.write('Socrates\n')

# Close the file
outfile.close()

