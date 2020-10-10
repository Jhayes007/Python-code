#   Filename: Program4-6.py
#   Author: J. Hayes
#   Date: October 7, 2019
#   Purpose: To demonstrate the use and functioning
#           of multiple nested decisions.
#           This script based on Fig. 4-17.

# Prompt the user for his/her test score
score = int(input('Enter your test score: '))

# Determine the grade
if (score < 60):
    print ('1-Your grade if F.')
else:
    if (score < 70):
        print('1-Your grade is D.')
    else:
        if (score < 80):
            print('1-Your grade is C.')
        else:
            if (score < 90):
                print('1-Your grade is B.')
            else:
                print('1-Your grade is A.')
                

# Converting the above structure to a simpler structure
# as in Program 4-7
if (score < 60):
    print ('2-Your grade if F.')
elif (score < 70):
    print('2-Your grade is D.')
elif (score < 80):
    print('2-Your grade is C.')
elif (score < 90):
    print('2-Your grade is B.')
else:
    print('2-Your grade is A.')
                
