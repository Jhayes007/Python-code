# Filename: program6-7.py
# Author: J.Hayes
# Date: Oct. 21, 2019
# Purpose: To demonstrate how to create and use a 
#      user-defined function.
#      This script is based on program 6-6.

# The main() function
def main():
    # Get the ages of the user and his/her best friend
    firstAge = int(input('Enter your age: ' ))
    secondAge = int(input("Enter best friend's age: "))
    # Calculate the sum of the two ages
    total = sum1(firstAge, secondAge)
    # Display the total
    print('Together they are ', total, ' years old.')
    return

# The function to add 2 variables
def sum1(num1, num2):
    result = num1 + num2
    return result

main()
