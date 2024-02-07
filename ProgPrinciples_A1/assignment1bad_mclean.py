# Name: Cameron McLean
# Class: PROG10004 20230905_00
# Assignment: Assignment #1
# Date: January 10, 2024
# Program: assignment1_mclean.py
# Description: An application that reads two positive integers, prints which
# integer is bigger, prints the common factors between both numbers,
# and then asks the user if they want to enter two new integers or terminate 
# the program.

#Initialize variables to be used in program
integer_1 = integer_2 = integer_factor = 0; 
user_input = '';

while(True):
    #Two while loops requesting for the first and second integer to be given,
    #providing an error message and relooping if provided with an invalid input
    while(integer_1 <= 0):
        integer_1 = int(input(f'= Enter the first positive integer: '));
        if(int(integer_1) <=0):
            print(f'Error: number must be positive.');
    
    while(integer_2 <= 0):
            integer_2 = int(input(f'= Enter the first positive integer: '));
            if(integer_2 <=0):
                print(f'Error: number must be positive.');   

    #Comparing each integer and returning whether integer_1 is larger, greater,
    #or equal to each other.
    if(integer_1 > integer_2):
        print(f'= ' + str(integer_1) + f' is greater than ' + str(integer_2));
        integer_factor = integer_2;
    elif(integer_1 < integer_2):
        print(f'= ' + str(integer_1) + f' is less than ' + str(integer_2)); 
        integer_factor = integer_1;
    else:
        print(f'= The two numbers are equal');
        integer_factor = integer_1;
  
    print(f'= Common factors of ', str(integer_1), ' and ', integer_2, ' are: ',
          end='');
    
    #Determining common factors between both numbers, remaining within
    #the range of the lowest number, no unecessary math being performed
    for i in range(integer_factor):
        if(i == 0): #Skips dividing by zero to avoid crashes
            continue
        if((integer_1 % i) == 0 and (integer_2 % i) == 0):
            print(str(i), end=' ');
    print('');
    integer_1 = integer_2 = 0;

    #Asking the user if they want to play again, providing an error message
    #and relooping if provided with an incorrect input
    while(True):
        user_input = input(f'= Play again (Y/N or y/n): ');
        if(user_input == 'Y' or user_input == 'y' or user_input == 'N' 
           or  user_input == 'n'):
            break;
        else:
            print(f'Error: choice must be Y/N or y/n.');
    
    if(user_input == 'N' or user_input == 'n'):
        break;
        
    
    
         