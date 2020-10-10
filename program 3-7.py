# FileName: Program 3-7.py
# Author: J.Hayes
# Date: Sep 18, 2019
# Purpose: To demonstrate the creation and use of a module
#       in python. This module accepts multiple arguments.

# The module that accepts multiple arguments
def showSum(num1, num2):
    result = num1 + num2
    print('The sum of the two numbers = ', result)
    return


def main():
    n1 = int(input('Enter the first number: '))
    n2 = int(input('Enter the second number: '))
    showSum(n1, n2)
    return


main()
