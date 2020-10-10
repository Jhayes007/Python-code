# FileName: Program 3-13.py
# Author: J.Hayes
# Date: Sep 18, 2019
# Purpose: To demonstrate the creation and use of a module
#   in python. This script illustrates the use of
#   multiple modules in a program. It is based on
#   the algorithim in Figure 3-21 in the text.
#   This also demonstrates a global constant.

# The getGrossPay() module
def getGrossPay():
    global grosspay
    grossPay = float(input('Enter the total gross pay: '))
    return

# The getBonuses() module
def getBonuses():
    global bonuses
    bonuses = float(input('Enter the amount of bonuses: '))
    return

# The showGrossPayContrib() module
def showGrossPayContrib(grossPay):
    contrib = grossPay * CONTRIBUTIONRATE
    print('The contribution for the gross pay ')
    print('is $', contrib)
    return


# The showBonusesContrib() module
def showBonusesContrib(bonuses):
    contrib = bonuses * CONTRIBUTIONRATE
    print('The contribution for the bonuses ')
    print('is $', contrib)
    return

def main():
    getGrossPay()
    getBonuses()
    showGrossPayContrib(grossPay)
    showBonusesContrib(bonuses)
    return

CONTRIBUTIONRATE = 0.05 # Global constant
# Global variables
grossPay = 0.0
bonuses = 0.0

main()
