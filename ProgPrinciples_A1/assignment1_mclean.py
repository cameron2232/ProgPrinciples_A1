# Name: Cameron McLean
# Class: PROG10004 20230905_00
# Assignment: Assignment #1
# Date: January 10, 2024
# Program: assignment1_mclean.py
# Description: An application that reads two positive integers, prints whether
# integer_one is bigger or smaller, prints the common factors between both
# numbers, and then asks the user if they want to enter two new integers or
# terminate the program.

#while True looping the program until user chooses to exit
while True:
    integer_one = integer_two = 0
    
    #two while loops asking user to input an integer, and looping and asking 
    #user to reenter if the inputted integer is less than or equal to 0
    #first for integer_one
    while integer_one <= 0: 
        integer_one = int(input('= Enter the first positive integer: '))
        if integer_one <= 0: print('Error: number must be positive') 
        else: break
    #repeat some process above for integer_two    
    while integer_two <= 0: 
        integer_two = int(input('= Enter the second positive integer: '))
        if integer_two <= 0: print('Error: number must be positive') 
        else: break
    
    #print whether integer_one is greater, smaller, or equal to integer_two
    print(f'= {integer_one} is greater than {integer_two}' 
          if integer_one > integer_two 
          else f'= {integer_one} is less than {integer_two}' 
          if integer_one < integer_two 
          else '= The two numbers are equal')
    
    #set integer_factor to the smaller number for for loop range
    if integer_one >= integer_two: integer_factor = integer_two
    else: integer_factor = integer_one
    
    print(f'= Common factors of {integer_one} and {integer_two} are: ', end='')
    
    #for loop ranging from 1 to the smallest number, checking if
    #both integers divided by i are 0. If both are, print the number.
    for i in range (1, (integer_factor+1)): 
        if(integer_one % i) == 0 and (integer_two % i) == 0: 
            print(str(i), end=' ')
    
    print()
    
    #while True loop asking the user to input if they would like to repeat
    #the program. if Y/N or y/n is not provided as an input, loop and 
    #have the user input again. if Y/y is inputed, loop the entire program
    #if N/n is inputed, break out of the While True and end.
    while True:
        user_input = input('= Play again (Y/N or y/n): ')
        if (user_input == 'Y' or user_input == 'y' or user_input == 'N' or  
            user_input == 'n'): 
            break
        else: print('Error: choice must be Y/N or y/n')
        
    if user_input == 'N' or user_input == 'n': break
            
        