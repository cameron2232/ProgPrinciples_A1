import math
import random

def get_rolls(lower_bound, upper_bound, prompt_message, error_message):
    
    rolling_times = 0

    while rolling_times < lower_bound or rolling_times > upper_bound:
        rolling_times = int(input(prompt_message))
        if rolling_times == 0:
            print('Thank you')
            return rolling_times
        elif rolling_times < lower_bound or rolling_times > upper_bound:
            print(error_message)
        else: return rolling_times
                
def dice_rolling(rolling_times):
    
    dice_one = dice_two = dice_three = dice_four = dice_five = dice_six = 0

    for i in range(rolling_times):
        random_num = random.randint(1, 6)
        if random_num == 1: dice_one+= 1
        elif random_num == 2: dice_two += 1
        elif random_num == 3: dice_three += 1
        elif random_num == 4: dice_four += 1
        elif random_num == 5: dice_five += 1
        elif random_num == 6: dice_six += 1
    return dice_one, dice_two, dice_three, dice_four, dice_five, dice_six

def print_results(dice_one, dice_two, dice_three, dice_four, dice_five, dice_six):
    print(dice_one)
    print(dice_two)
    print(dice_three)
    print(dice_four)
    print(dice_five)
    print(dice_six)