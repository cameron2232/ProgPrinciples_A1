# About assignment 1
# - read 2 positive integers, compare them, print common factors 
def assignment2():
    while True:
        x = int(input('Number 1: '))
        while x < 1: 
            print('Number must be positive')
            x = int(input('Number 1: '))

        y = int(input('Number 2: '))    
        while y < 1: 
            print('Number must be positive')
            y = int(input('Number 1: '))

        if x > y: print(f'{x} > {y}')
        elif x < y: print(f'{x} < {y}')
        else: print(f'{x} = {y}')

        print(f'Common factors of {x} and {y} are: ', end='')
        # x = 10, y = 100
        mini = x if x < y else y
        for n in range(1, mini + 1): # n = 1, 2, 3, ..., x/y
            if x % n == 0 and y % n == 0:
                print(n, end=' ')
        print()

        choice = input('Play again: ')
        while choice != 'Y' and choice != 'y' \
            and choice != 'N' and choice != 'n':
            print('Choice must be Y/y or N/n')
            choice = input('Play again: ')

        if choice == 'N' or choice == 'n':
            break 

# ===================================================================================
    
# Functions - 2/3 

# Topic 1 - Global variables 
# - defined outside any functions
# - has a global scope, starting from the place it is defined 
# - to modify global variable in a function, re-declare it 
# - Note: try not to use any global variable, unless they are contant        
#   - naming contants ALL_CAPS

MIN_AGE = 18 # global constant
MAX_AGE = 59                
age = 19 # global variable, bad practice

def print_age():
    global age # re-declare
    age = 33
    print(age)
    
# Topic 2 - Random numbers 
# - Standard Library: pre-existing functions
#   - built-in functions: direct use them 
#       - print(), input(), int(), float()
#   - others, first import, then use 
#       - random, math 
# - random package: used to generate random numbers 
#   - import random 
#   - use functions: random.function_name()
#   - random.randint(lower, upper): return a random int between lower and upper, both inclusive
#   - random.randrange(start, stop, step): return a random int, params same as range()
#   - random.random(): return a random float [0.0, 1.0)
#   - random.uniform(lower, upper): return a random float between lower and upper  
        
import random 

def random_tester():
    # randint()
    print('Random integers:', end=' ')
    for n in range(10): 
        x = random.randint(20, 50)
        print(x, end=' ')
    print() 

    # randrange()
    print('Random integers:', end=' ')
    for n in range(10): 
        x = random.randrange(10, 100, 5)
        print(x, end=' ')
    print() 

    # random()
    print('Random float [0, 1):', end=' ')
    for n in range(10): 
        x = random.random()
        print(x, end=' ')
    print() 

    # uniform()
    print('Random float:', end=' ')
    for n in range(10): 
        x = random.uniform(20.0, 50.0)
        print(x, end=' ')
    print() 

# Exercise: write a function that accepts a number, 
#   throw a coin for a number of times, count and print
#   heads and tails
def throw_coin(times):
    heads, tails = 0, 0 
    for _ in range(times):
        # get a random int, if 0 - head, 1 - tail 
        coin = random.randint(0, 1)
        if coin == 0: heads += 1 
        else: tails += 1 
    print(f'Heads: {heads}, Tails: {tails}')

# Topic 3 - Value-returning functions   
# - functions that carry data back to the caller
#   - input(), int(), float(), all functions in random
# - using return statement to return a value or multiple values
#   - function is terminated when return is executed
#   - use comma to seperate multiple values
#   - in calling function, assign to multiple variables
#   - return value can be of any type(string, int, float, boolean) 
#       - return None, caller check it using is None, is not None       
# - the returned value can be used in calling function at anywhere a value is needed

# Example: a function reads and returns the firstname and lastname 
def get_names():
    firstname = input('Enter firstname: ')
    lastname = input('Enter lastname: ')
    return firstname, lastname                

# Example: a function that takes lower and upper of valid mark,
#   read a valid mark and return it 
def get_mark(lower, upper, prompt='Test'):
    if lower > upper: return None
    mark = float(input(f'Enter mark ({lower} - {upper}) for {prompt}: '))
    while mark < lower or mark > upper:
        mark = float(input(f'Enter mark ({lower} - {upper}) for {prompt}: '))
    return mark        

# Example: a function that takes number of tests, 
#   for each test, read the mark. Finally return the average 
def get_average(num):
    if num < 1: return None 
    total = 0.0
    for n in range(1, num + 1):
        mark = get_mark(0, 100, 'Test#' + str(n))
        total += mark 
    return total / num

# Example: a function that accepts an average, returns the letter grade
def get_grade(average):
    if average > 100 or average < 0:
        return None
    return 'A+' if average >= 90 else \
           'A' if average >= 80 else \
           'B' if average >= 70 else \
           'C' if average >= 60 else \
           'D' if average >= 50 else \
           'F' 

def student_app():
    first, last = get_names()
    print(f'Hello {first} {last}')

    average = get_average(5)
    print(f'Average is: {average}')

    grade = get_grade(average)
    if grade is None: 
        print('Invalid average')
    else:
        print(f'Grade is: {grade}')

def main():
    student_app()

    # throw_coin(3)
    # throw_coin(33)
    # throw_coin(333)
    # throw_coin(3333)

    # random_tester()
    # print_age()
main()

