# Filename: program6-8.py
# Author: J.Hayes
# Date: Oct. 21, 2019
# Purpose: To demonstrate the use of a 
#      user-defined function.
#      This script is based on program 6-11 thru 6-14.
#       Uses multiple user-defined functions.

# The getSales() function
def getSales():
    monthlySales = float(input("Enter the salesperson's " \
                               "monthly sales: "))
    return monthlySales

# The getAdvancedPay() function
def getAdvancedPay():
    print('Enter the amount of advanced pay, or 0 if ')
    print(' no advanced pay was given: ', end = '')
    advanced = float(input())
    return advanced

# Date: Oct. 23, 2019
# The determineComissionRate() function
def determineCommissionRate(sales):
    if (sales < 10000.00):
        rate = 0.10
    elif (sales < 15000.00):
        rate = 0.12
    elif (sales < 18000.00):
        rate = 0.14
    elif (sales < 22000.00):
        rate = 0.16
    else:
        rate = 0.18

    return rate

# The main() function
def main():
    # Get the sales amount
    sales = getSales()
    # Get the amount of advanced pay
    advancedPay = getAdvancedPay()
    # Determine the comission rate
    commissionRate = determineCommissionRate(sales)
    # Calculate the pay
    pay = sales * commissionRate - advancedPay
    # Display the amount of pay
    print('The pay is $', pay)
    # Determine whether the pay is negative
    if (pay < 0):
        print('The salesperson must reimburse the company.')
    return

main() 
