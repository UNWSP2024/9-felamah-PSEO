# Faith Lamah
# 10/30/2025
# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():

    count = 0
    names_file = open('names.txt','r')
    for name in names_file:
        count += 1

    print(f'The number of names stored in the file is {count}.')

    names_file.close()


    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()