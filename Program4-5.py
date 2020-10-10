#   Filename: Program4-5.py
#   Author: J. Hayes
#   Date: October 7, 2019
#   Purpose: To demonstrate the use and functioning
#           of nested decisions.
#           This script based on Fig. 4-15.

# Get the input and do numeric conversions
salary = float(input('Enter the annual salary: '))
yearsOnJob = int(input('Enter # of years on current job: '))

# Determine whether the user qualifies for a loan
if (salary >= 30000):
    if (yearsOnJob >= 2):
        print ('You qualify for the loan.')
    else:
        print('You must have been on your current job for')
        print('At least two years to qualify.')
    # End of inner if
else:
    print('You must earn at least $30,000 per year')
    print('To qualify.')
# End of the outer if

# Coding the above structure as an And
if (salary >= 30000) and (yearsOnJob >= 2):
    print('AND-You qualify for the loan.')
else:
    print('AND-You do not qualify for the loan.')
