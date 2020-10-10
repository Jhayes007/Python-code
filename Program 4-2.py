#   Filename: Program4-2.py
#   Author: J. Hayes
#   Date: October 2, 2019
#   Purpose: To demonstrate the use and functioning of
#           a dual-alternative selection structure (if
#           statement).
#           This script is based on the algorithim in Fig. 4-11.

# Module that calculates the regular pay
def calculateRegularPay(hours, rate):
    # Calculate the regular pay
    grossPay = hours * rate
    # Display the gross pay
    print('The gross pay is $%.2f' % grossPay)
    return

# Module to calculate gross with overtime pay
def calculatePayWithOT(hours, rate):
    # Calculate the number of overtime hours worked
    OTHours = hours - BASEHOURS
    # Calculate the amount of overtime pay
    OTPay = OTHours * rate * OTMULTIPLIER
    # Calculate the gross pay
    grossPay = BASEHOURS * rate + OTPay
    # Display the gross pay
    print('The gross pay is $%.2f' % grossPay)
    return

# The main() program
# Global constants
BASEHOURS = 40
OTMULTIPLIER = 1.5
# Read in the hours worked and pay rate
hoursWorked = float(input('Enter the number of ' \
                          'hours worked: '))
payRate  = float(input('Enter the hourly pay rate: '))
# Calculate and display the gross pay
if (hoursWorked > BASEHOURS):
    calculatePayWithOT(hoursWorked, payRate)
else:
        calculateRegularPay(hoursWorked, payRate)

# End of if


