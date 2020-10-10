coffeeFile = open('coffee.txt', 'w')

coffeeType = int(input('Enter the coffee type: '))
for counter in range(1, coffeeType+1):
    print('Enter the coffee quantity', counter, ':  ',end='')
    coffeeFile.write(coffeeQuan + '\n')

coffeeFile.close()
print('The coffee has been saved to coffee.txt.')
