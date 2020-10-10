# Filename: GuessingGame.py
# Author: J.Hayes
# Date: Oct. 21, 2019
# Purpose: To demonstrate the use of selection and
#       repetition structures together.

# The following library is needed to create
# random numbers
import random
# The following statement creates a random integer
# between 0 and 100 and stores it in rNum
rNum = random.randint(0, 100)

print('HI-LO NUMBER GUESSING GAME')
print()     # Blank Line
# Get the user input
guess = int(input('Enter your guess as an integer: '))
# The loop
while (0 <= guess and guess <= 100):
    if (guess > rNum):
        print('Guessed too high')
    elif (guess < rNum):
        print('Guessed too low')
    else:
        print('You guessed it. The number was: ', rNum)
        break
    # Request the next guess
    guess = int(input('Enter your guess again: '))




