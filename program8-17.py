# Filename: Program8-17.py
# Author: J.Hayes
# Date: Nov. 18, 2019
# Purpose: To demonstrate the use of two-dimensional arrays.
#           On pages 396-397, this is an example of referencing 2D arrays.
#           we will read sales data for three divisions and 4 quarters
#           for a company. As in the text we will find the overall total
#           for the sales of the company. In addition, we will find the
#           overall sales for each division (totaling rows)
#           and also for each quarter (totaling columns). We will use
#           rows for divisions and columns for quarters.

DIVS = 3
QTRS = 4
# A 2D array with all elements intialized to zero.
sales = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# Accumulator for overall total
total = 0

# Display instructions
print("This program calculates the company's total sales.")
print('Enter the quarterly sales amounts for each division')
print('when prompted.')
# Nested loops to fill the array with quarterly sales amount
# for each division.
for row in range(DIVS):
    for col in range(QTRS):
        print('Division ', row+1, ' quarter ', col+1, ': ', end='')
        sales[row][col] = float(input())
    print() # A blank line

# The loop to compute the totals for each division
# This will be done by calculating row totals
rtotals = [0] * DIVS # 1D array to hold row totals
for row in range(DIVS):
    for col in range(QTRS):
        rtotals[row] += sales[row][col]
print('Totals for the Divisions: ', rtotals)

# The loop to compute totals for each quarter
# This will be done by calculating column totals
ctotals = [0] * QTRS # 1D array to hold column totals
for row in range(DIVS):
    for col in range(QTRS):
        ctotals[col] += sales[row][col]
print('Totals for the quarters: ', ctotals)

# Nested loops to add all the elements of the 2D array.
for row in range (DIVS):
    for col in range(QTRS):
        total += sales[row][col]

# Display the total sales for the organization
print('The total company sales are: ${:,.2f}'.format(total))




