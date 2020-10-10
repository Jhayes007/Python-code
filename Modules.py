# FileName: Program 3-5.py
# Author: J.Hayes
# Date: Sep 18, 2019
# Purpose: To demonstrate the creation and use of a module
#       in python. This module accepts one argument.

# The module that has one argument
def doubleNumber(value):
    result = value * 2
    print('The doubled number is ', result)

# The main()
def main():
    number = int(input('Enter an integer number: '))
    doubleNumber(number)

main()


