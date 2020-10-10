# FileName: Program 3-7.py
# Author: J.Hayes
# Date: Sep 18, 2019
# Purpose: To demonstrate the creation and use of a module
#       in python. This module accepts multiple arguments.

# The module that accepts multiple arguments
def showSum(num1, num2):
    # num1 and num2 are just placeholders; technically
    # they are called "formal arguments"
    result = num1 + num2
    print('The sum of the two numbers = ', result)
    return


def main():
    n1 = int(input('Enter the first number: '))
    n2 = int(input('Enter the second number: '))
    showSum(n1, n2)
    # In the module call, the placeholders are replaced
    # by literals or variables that have a value. Here
    # the arguments are referred to as "actual arguments."
    return


main()
