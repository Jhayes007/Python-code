# Filename: Program10-5.py
# Author: J. Hayes
# Date: Nov. 27, 2019
# Purpose: To demonstrate how to create, open, read, and close a file.
#           based on figure 10-15.

# create a file variable/file object and open a file
# named "videotimes.txt."

VideoFile = open('videotimes.txt', 'w')

# Get the number of videos
numVideos = int(input('Enter the number of videos in the project: '))
# Prompt for and read the running times for the videos
for counter in range(1, numVideos+1):
    # Get the times
    print('Enter the running time for video #', counter, ': ',end='')
    runningTime = input()
    # Write the time to the file
    VideoFile.write(runningTime + '\n')

# Close the file
VideoFile.close()
print('The times have been saved to videotimes.txt.')


