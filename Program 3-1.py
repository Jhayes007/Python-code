# FileName: Program 3-1.py
# Author: J.Hayes
# Date: Sep 11, 2019
# Purpose: To demonstrate the creation and use of a module
#       in python.

# The main() module
def main():
    print('I have a message for you. ')
    showMessage() # Call to the showMessage() module
    print("That's all folks.")
# End of main()

# The showMessage() module
def showMessage():
    print('Hello world!:')
# end of showMessage() module

main()  # Call the main() module to run the program.

