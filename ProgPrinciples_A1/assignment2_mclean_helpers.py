# Name: Cameron McLean
# Class: PROG10004 20230905_00
# Assignment: Assignment #2
# Date: February 18, 2024
# Program: assignment2_mclean.py
# Description: A program that takes the number of times the user wishes to roll
# a dice, rolls said dice the provided amount of times, and prints out the
# count of each side rolled and a corresponding visual respresentation

import math
import random

# get_rolls function, which prompts the user to provide a valid input
# of amount of rolls user would like to be performed, returning an error
# message if inputted number does not fall between the upper and lower bound.
# returns rolling_times if valid input is entered, and prints 'Thank you'
# if user inputs 0.
def get_rolls(lower_bound, upper_bound, prompt_message, error_message):
    
    rolling_times = 0

    # while loop that will continue looping until a valid input is entered
    while rolling_times < lower_bound or rolling_times > upper_bound:
        
        # prompts user to input a number between provided bounds
        rolling_times = int(input(prompt_message))
        
        # prints 'Thank you' if user inputs 0
        if rolling_times == 0:
            print('Thank you')
            return None
        
        # prints an error message if user inputs invalid number
        elif rolling_times < lower_bound or rolling_times > upper_bound:
            print(error_message)
        
        # returns rolling_times if user input a valid number
        else: return rolling_times
                
def dice_rolling(rolling_times):
    
    dice_one = dice_two = dice_three = dice_four = dice_five = dice_six = 0

    # rolls a random number between 1 and 6, and depending on the number 
    # rolled, adds 1 to corresponding side of the dice variable
    for i in range(rolling_times):
        random_num = random.randint(1, 6)
        if random_num == 1: dice_one+= 1
        elif random_num == 2: dice_two += 1
        elif random_num == 3: dice_three += 1
        elif random_num == 4: dice_four += 1
        elif random_num == 5: dice_five += 1
        elif random_num == 6: dice_six += 1
        
    # returns each dice side variable 
    return dice_one, dice_two, dice_three, dice_four, dice_five, dice_six

def print_results(dice_title, line_length, print_character, roll_count):
   
    # prints visual representation of the number of times said dice was rolled
    # using the print_character and line_length as an indicator of the amount
    # rolled compared to the dice with the highest number of rolls
    print()
    print(f'{dice_title}:  ', end = '')
    if roll_count != 0:
        for i in range(line_length):
            print (print_character, end = '')
    print(f' {roll_count}', end = '')
    
    