import assignment2_mclean_helpers

def main():
    
    dice_one, dice_two, dice_three, dice_four, dice_five,  dice_six = assignment2_mclean_helpers.dice_rolling(assignment2_mclean_helpers.get_rolls(1, 100000, 'Rolling Times(1, 10000, 0 to stop): ', 'Invalid number'))

    assignment2_mclean_helpers.print_results(dice_one, dice_two, dice_three, dice_four, dice_five, dice_six)
    pass

main()