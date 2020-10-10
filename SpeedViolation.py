# Filename: SpeedingViolation.py
# Author: J.Hayes
# Date: November, 4 2019
# Purpose: To demonstrate the use and functioning
#           of a validation loop
#           This script is the solution to exercise 4 @ the end of chap 7.
#           In this exercise the user inputs the speed limit on a
#           a road and the driving speed of a driver and check if the
#           driving speed is greater than the limit. If so, display
#           how much over the limit the speed is.

# The getLimit() function
def getLimit(minSpeed, maxSpeed):
    # Enter the speed limit
    inputAmount = int(input("Enter the speed limit: "))
    # Validate the limit
    while (inputAmount < minSpeed or inputAmount > maxSpeed):
        print('Limit must be between ', minSpeed, ' and ', \
              maxSpeed)
        inputAmount = int(input('Enter a valid quanity: '))
    return inputAmount

# The getDrive() function
def getDrive(limitSpeed):
    # Enter the drive's speed
    inputAmount = int(input('Enter the speed of the driver: '))
    # Validation loop
    while (inputAmount <= limitSpeed):
           print('Speeding must be over ', limitSpeed, '!')
           inputAmount = int(input('Enter a valid quanity: '))
    return inputAmount

# The overSpeed() function
def overSpeed(limitSpeed, driveSpeed):
    overLimit = driveSpeed - limitSpeed
    print('The driver is going ',overLimit, 'MPH over the speed limit!')
    return

# The main() module
def main():
    # The range for the limit speeds
    minSpeed = 20
    maxSpeed = 70
    # Get the speed limit
    limitSpeed = getLimit(minSpeed, maxSpeed)
    # Get the driver's speed
    driveSpeed = getDrive(limitSpeed)
    # Show if speeding
    if (driveSpeed > limitSpeed):
        overSpeed(limitSpeed, driveSpeed)
    return

main()
