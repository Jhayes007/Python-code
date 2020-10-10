# Filename: stringMethods.py
# Author: J.Hayes
# Date: Oct. 23, 2019
# Purpose: To demonstrate various string methods
#       available in Python.

# A quote from an IBM President, Thomas Watson, in 1943
quote = 'i think there is a world market for maybe five computers.   '

# String methods
print('Original quote: ')
print(quote)
print('\nIn uppercase: ')
print(quote.upper())
print('\nIn lowercase: ')
print(quote.lower())
print('\nAs a title: ')
print(quote.title())
print('\nWith a minor replacement: ')
print(quote.replace('five', 'millions of'))
print('\nCapitalize: ')
print(quote.capitalize())
print('\nAfter swapping case: ')
print(quote.swapcase())
print('\nRemoving white spaces at the ends: ')
print(quote.strip())
print('\nOriginal quote is still: ')
print(quote)
