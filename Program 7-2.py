# Filename: Program7-2.py
# Author: J.Hayes
# Date: Oct. 30, 2019
# Purpose: To demonstrate the use and functioning
#           of a validation loop.
#           This script is based on Fig. 7-2

# Definiton of showRetail() module
def showRetail():
    # Constant
    Markup = 2.5

    # Prompt for and read the wholesale cost / item
    # This is the priming read for the loop
    wholesale = float(input("Enter an item's wholesale cost: "))

    # Validation loop
    while (wholesale < 0):
        print('The cost cannot be negative. Please enter ')
        print('The correct Wholesale cost: ', end='')
        wholesale = float(input())

        # Calculate the retail price
        retail = wholesale * MARKUP
        # Display the retail price
        print('The retail price is $%.2f' % retail)
        return

# The main module
def main():
    doAnother = 'y'
    while (doAnother == 'y' or doAnother == 'y'):
        showRetail()
        doAnother = input("Do you have another item (Y/N): ")
    return

main()
