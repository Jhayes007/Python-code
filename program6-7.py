# Filename: program6-7.py
# Author: J.Hayes
# Date: Oct. 21, 2019
# Purpose: To demonstrate the use of a 
#      user-defined function.
#      This script is based on program 6-7. discounted price

# Constant
DISCOUNTPERCENTAGE = 0.20

# The getRegularPrice() function to prompt the user
# to enter the regular price needed to read it.
def getRegularPrice():
    price = float(input("Enter the item's regular price: "))
    return price

# The discount() function accepts an item's regular price
# as an argument and returns the amount of the discount
# specified by the constant defined above.
def discount(price):
    return price * DISCOUNTPERCENTAGE

# The main() function
def main():
    # Get the item's regular price
    regularPrice = getRegularPrice()
    # Get the sale price
    salePrice = regularPrice - discount(regularPrice)
    # Display the sale price
    print('The sale price is $', salePrice)
    return

main()
