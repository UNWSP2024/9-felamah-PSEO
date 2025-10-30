# Faith Lamah
# 10/30/2025
# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():

    numbers_file = open('numbers.txt', 'r')
    total = 0
    try:
        for number in numbers_file:
            total += int(number)
            print(number)
        print(f'The calculated total is {total}.')
    except ValueError:
        print('Item has not been converted to a number.')
    except IOError:
        print('File not found.')

    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()