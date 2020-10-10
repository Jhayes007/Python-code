# Filename: Program10-6.py
# Author: J. Hayes
# Date: Nov. 27, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on figure 10-16 from page 489.

# Create a file variable/file object and open a file
# named "videotimes.txt."

VideoFile = open('videotimes.txt', 'r')
# Set the accumulator to zero
total = 0

print('Here are the running times, in seconds of each video ' \
      'in the project.')

# Read all the running times in the file; display them and add
# them to the accumulator.
for line in VideoFile:
    line = float(line)
    print(line)
    # Add to the total
    total += line


# Close the file
VideoFile.close()

# Display the total running time
print('The total running time of the videos is ', total, 'seconds.')





