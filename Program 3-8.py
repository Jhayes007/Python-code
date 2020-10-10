# FileName: Program 3-8.py
# Author: J.Hayes
# Date: Sep 18, 2019
# Purpose: To demonstrate the creation and use of a module
#   in python. This script illustrates the use of
#   multiple modules in a program. It is based on
#   the algorithim in Figure 3-17 in the text.

#   The showIntro() module
def showIntro():
    print('This program converts measurements in cups ')
    print('to fluid ounces. ')
    print ('For your reference the formula is: ')
    print('\t1 cup = 8 fluid ounces.\n')
    return

# The cupsToOunces() module
def cupsToOunces(cups):
    ounces = cups * 8
    print('That converts to ', ounces, ' ounces.')
    return

# The main() module
def main():
    showIntro()
    cups = float(input('Enter the number of cups: '))
    cupsToOunces(cups)
    return

#   Call to main() to run the script
main()

