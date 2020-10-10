# Filename: Program10-2.py
# Author: J.Hayes
# Date: Nov. 25, 2019
# Purpose: To demonstrate how to create a file object, open a file
#           write to a file, and close the file.
#           This is based on Figure 10-4 on pg. 474.

# Create a file object and open a file named "philosophers.txt"
infile = open('philosophers.txt', 'r')

# Read the whole file
filecontents = infile.read()
# Display the contents of the whole file
print(filecontents)
# Close the file
infile.close()

print()
print('Now reading one line at a time as in the text: ')
# Reopen the file
infile = open('philosophers.txt', 'r')
# Read the names of three philosophers from the file and
# display them.
line1 = infile.readline()   # Read the line from the file
line1 = line1.rstrip()  # Removes the newline character from record
line2 = infile.readline().rstrip()
line3 = infile.readline().rstrip()
# Display the names
print(line1)
print(line2)
print(line3)

# Close the file
infile.close()
