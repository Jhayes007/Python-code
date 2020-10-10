# Filename: pe3-7.py
# Author: J. Hayes
# Date: Sep 30, 2019
# Purpose: To solve programming exercise 307. In this
#           exercise grams fat and grams carb are input,
#           the program converts them to calories
#           and displays the result.

#   The getFatGms() module
def getFatGms():
    global gramsFat
    gramsFat = float(input('Enter fat grams consumed: '))
    return

# The getCarbGms() module
def getCarbGms():
    global gramsCarb
    gramsCarb = float(input('Enter the carbohydrate grams consumed: '))
    return
# The setFatCals() module
def setFatCals(gramsFat):
    global calsFat
    calsFat = gramsFat * CALSFROMFAT
    return

# The setCarbCals() module
def setCarbCals(gramsCarb):
    global calsCarb
    calsCarb = gramsCarb * CALSFROMCARB
    return

# The showResults() module
def showResults(gramsFat, gramsCarb, calsFat, calsCarb):
    print('Grams of Fat: ', gramsFat)
    print('Result calories: ', calsFat)
    print('Grams of Carbohydrate: ', gramsCarb)
    print('Result calories: ', calsCarb)
    return


# The main() module
def main():
    # Get fat grams
    getFatGms()
    # Get carb grams
    getCarbGms()
    # Compute calories from fat
    setFatCals(gramsFat)
    # Calculate calories from carbs
    setCarbCals(gramsCarb)
    # Display the results
    showResults(gramsFat, gramsCarb, calsFat, calsCarb)
    return

# Global constants
CALSFROMFAT = 9
CALSFROMCARB = 4
# Global variables
gramsFat = 0.0
gramsCarb = 0.0
calsFat = 0.0
calsCarb = 0.0
# Call main() to run the program
main()
