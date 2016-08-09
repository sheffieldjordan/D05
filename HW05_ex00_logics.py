#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    user_number = ''
    user_number = input('What is your number?')
    while True:
        try:
            while user_number != '':
                user_number = int(user_number)
                if user_number%2 == 0:
                    print("Your number is even")
                    return
                else: 
                    print("Your number is odd")
                    return  
            break
        except:
            print("Only use integers!")
            even_odd()
            return

def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
   
    line_start = int(1)
    line_stop = int(11)
    while line_stop <= 101:
        for numbers in range (line_start, line_stop):
            print ('{:3}'.format(numbers), end=' ') #found this {:3}.format on SO, and don't completely understand it. I assume it tells the number to print on the 3rd position on the line. 
        print("\n")
        line_start += 10
        line_stop += 10
    return

    # I just want to point out all the crazy stuff 
    # I tried before I figured this one out. At least
    #  I think I figured it out.

    # count = ''
    # number = 1 
    # while number <= 10:
    #    print(number, " ")
    #    number += 1
    # # for x in range (1, 101):
    # #     print (x+0, end=' ') 
    # # print()

    # for numbers in range (11, 21):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")
    # for numbers in range (21, 31):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")
    # for numbers in range (31, 41):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")
    # for numbers in range (41, 51):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")
    # for numbers in range (51, 61):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")    
    # for numbers in range (61, 71):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")
    # for numbers in range (71, 81):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")
    # for numbers in range (91, 101):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")
 
    # for i in     for numbers in range (1, 11):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")
    # for numbers in range (11, 21):
    #     print ('{:3}'.format(numbers), end=' ')
    # print("\n")range(11, 101):
    # #     print(i, end = ' ')
    #     # if i == len(range(1,11)):print('{:3}'.format(i), end=' ')
        
    #     if i == len(range(1,21)):print()
    #     if i == len(range(1,31)):print()
    #     if i == len(range(1,41)):print()
    #     if i == len(range(1,51)):print()
    #     if i == len(range(1,61)):print()
    #     if i == len(range(1,71)):print()
    #     if i == len(range(1,81)):print()
    #     if i == len(range(1,91)):print()

from statistics import mean

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    numeric_input = ''
    counter = 1
    found_average = ''
    input_sum = ''
    inputted_numbers = []


    while True:
        try:
            while numeric_input != 'done':
                numeric_input = input("What is your input?")
                inputted_numbers.append(int(numeric_input))
                if numeric_input == 'done':
                    print("You're done!")
        except:
             print('Only use numeric values!') 
        
        print("We found the average:", mean(inputted_numbers))
        break
    
    return
##############################################################################
def main():
    even_odd()
    ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
