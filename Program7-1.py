# Filename: Program7-1.py
# Author: J.Hayes
# Date: Oct. 30, 2019
# Purpose: This script is based on the pseudocode in
#       Program 7-1 on page 333 in the text.
#       To demonstrate how invalid data can be easily
#       entered.

# Get the number of hours worked
hours = float(input('Enter the number of hours worked: '))
# Get the hourly pay rate
payRate = float(input('Enter the hourly pay rate: '))
# Calculate the gross pay
grossPay = hours * payRate
# Display the gross pay
print('The gross pay is $%.2f' % grossPay)


