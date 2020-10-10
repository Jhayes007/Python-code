# FileName: Program 3-11.py
# Author: J.Hayes
# Date: Sep 18, 2019
# Purpose: To demonstrate the creation and use of a module
#   in python. This script illustrates the use of
#   multiple modules in a program. It is based on
#   the algorithim in Figure 3-19 in the text.
#   This also demonstrates a global variable. 

#   The showIntro() module
def showIntro():
    print('This program converts measurements in cups ')
    print('to fluid ounces. ')
    print ('For your reference the formula is: ')
    print('\t1 cup = 8 fluid ounces.\n')
    return

# The cupsToOunces() module
def cupsToOunces(cup):  # 'cup' is a local variable
    ounces = cup * 8
    print('That converts to ', ounces, ' ounces.')
    return

# The getCups() module
def getCups():   # 'cup' is a local variable
    global cups # Necessary to access a global variable
                # inside a module
    cup = float(input('Enter the number of cups: '))
    cups = cup
    return

# The main() module
def main():
    showIntro()
    getCups()
    cupsToOunces(cups)
    return

#   Call to main() to run the script
cups = 0    # A global variable
main()

