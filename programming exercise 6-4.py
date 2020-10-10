# Filename: programmingexercise6-4.py
# Author: J.Hayes
# Date: Oct. 23, 2019
# Purpose: This script find the bigger of two
#           integers and displays it.
#           This is the solution of programming
#           exercise 4 @ the end of chapter 6.

# The main() function
def main():
    num1 = getNum() # Get the first number
    num2 = getNum() # Get the second number
    # Find the maximum and display the result
    showMaximum(num1, num2)
    return

# The getNum() function
def getNum():
    inputAnswer = int(input('Enter an integer: '))
    return inputAnswer

# The showMaximum() function
def showMaximum(num1, num2):
    if (num1 == num2):
        result = 0
    elif (num1 > num2):
        result = num1
    else:
        result = num2
    # End of if 
    if (result != 0):
        print('The maximum is: ', result)
    else:
        print('The two numbers are equal.')

    return result

main()

