# Name: Cameron McLean
# Class: PROG10004 20230905_00
# Assignment: Assignment #2
# Date: February 18, 2024
# Program: assignment2_mclean.py
# Description: A program that takes the number of times the user wishes to roll
# a dice, rolls said dice the provided amount of times, and prints out the
# count of each side rolled and a corresponding visual respresentation

import assignment2_mclean_helpers
import math

def main():
    # while True loop, loops indefinitely until 0 is inputted
    while True:
        
        # Calls rolling time function, receving a valid input from the user
        # of how many times to roll the dice
        rolling_times = assignment2_mclean_helpers.get_rolls(1, 100000,
            'Rolling Times(1, 10000, 0 to stop): ', 'Invalid number')
    
        # Ends program if user inputs 0 in rolling_times function
        if rolling_times == 0:
            return None
          
        # Calls dice_rolling function, simulating dice rolls for count
        # specified by rolling_times, and assigning the amount of times each
        # face was rolled into each corresponding variable
        dice_one, dice_two, dice_three, dice_four, dice_five, dice_six \
          = assignment2_mclean_helpers.dice_rolling(rolling_times)
 
        # Goes through checking amount each side was rolled, and setting
        # largest_dice to the largest number
        largest_dice = dice_one
        if largest_dice < dice_two: largest_dice = dice_two
        if largest_dice < dice_three: largest_dice = dice_three
        if largest_dice < dice_four: largest_dice = dice_four
        if largest_dice < dice_five: largest_dice = dice_five
        if largest_dice < dice_six: largest_dice = dice_six
    
        char_count = 0

        # Goes through each dice, finds the percentage difference compared
        # to largest_dice, and rounds
        if dice_one != 0:
            dice_percentage = dice_one / largest_dice
            char_count = 70 * dice_percentage
            char_count = math.floor(char_count)
      
        # Calls print_results function, printing out a visual representation of
        # the amount of times a side was rolled compared to other sides
        # and repeat said process for each side of the dice           
        assignment2_mclean_helpers.print_results('One  ', char_count, '=',
            dice_one)
    
        if dice_two != 0:
            dice_percentage = dice_two / largest_dice
            char_count = 70 * dice_percentage
            char_count = math.floor(char_count)
       
        assignment2_mclean_helpers.print_results('Two  ', char_count, '=',
            dice_two)
    
        if dice_three != 0:
            dice_percentage = dice_three / largest_dice
            char_count = 70 * dice_percentage
            char_count = math.floor(char_count)
       
        assignment2_mclean_helpers.print_results('Three', char_count, '=',
            dice_three)
    
        if dice_four != 0:
            dice_percentage = dice_four / largest_dice
            char_count = 70 * dice_percentage
            char_count = math.floor(char_count)
        
        assignment2_mclean_helpers.print_results('Four ', char_count, '=',
            dice_four)
    
        if dice_five != 0:
            dice_percentage = dice_five / largest_dice
            char_count = 70 * dice_percentage
            char_count = math.floor(char_count)
        
        assignment2_mclean_helpers.print_results('Five ', char_count, '=',
            dice_five)
    
        if dice_six != 0:
            dice_percentage = dice_six / largest_dice
            char_count = 70 * dice_percentage
            char_count = math.floor(char_count)

        assignment2_mclean_helpers.print_results('Six  ', char_count, '=',
            dice_six)
        
        print(), print()
    
    


main()