# Faith Lamah
# 10/30/2025
# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random
def random_number_file():

    numberRandoms = int(input('Enter the number of random numbers the file will hold (Max of 1000):'))

    if numberRandoms > 1 and numberRandoms < 1000:
        number_file = open('random_numbers.txt', 'w')
        for i in range(1, numberRandoms + 1):
            random_number = random.randint(1, 500)
            number_file.write(str(random_number) + '\n')

        print('In the random_number_file.')
    else:
        print('Enter a number between 1 and 1000')


    number_file.close()

random_number_file()
