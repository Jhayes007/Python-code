#   Filename: Program4-1.py
#   Author: J. Hayes
#   Date: October 2, 2019
#   Purpose: To demonstrate the use and functioning of
#           a single-alternative selection structure (if
#           statement).
#           This script is based on the algorithim in Fig. 4-7.

test1 = int(input('Enter the score for test1: '))
test2 = int(input('Enter the score for test2: '))
test3 = int(input('Enter the score for test3: '))
# Processing
average = (test1 + test2 + test3) /3
# Display the Output
print('The average score is ', average)
# Single-alternative if
if (average > 95):
    print('Congratulations! Great Average!')

