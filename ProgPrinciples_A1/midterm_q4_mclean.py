#write function that gets valid integer in specified range
#functions takes lower bound and upper bound
#return number if given valid
#return none if lower bound is greater than upper bound
#default lower bound = 0 upper bound = 100

def read_valid_integer(lower_bound = 0, upper_bound = 100):
    if lower_bound > upper_bound:
        return None
    
    user_input = int(input(f'Enter an integer between {lower_bound} and {upper_bound} inclusive: '))
    
    while user_input < lower_bound or user_input > upper_bound:
        print('The number is out of the required range.')       
        user_input = int(input(f'Enter an integer between {lower_bound} and {upper_bound} inclusive: '))
        
    return user_input
        
read_valid_integer(100, 50)
read_valid_integer()
read_valid_integer(1, 20)
    
    
