# Functions - 1/3

# Topic 1 - Function what and why
#   - what: a group of statements for a specific task
#   - examples: print(), input(), int(), float(), round()
#   - why: reusability and modularity
#       - divide and conquer: task -> subtask
#       - easy to read 
#   - two types:
#       - 1. void function: just do something, no data carried back
#           - print()
#       - 2. value-returning function: return data back to caller
#           - input(), int()
#           - use return statement

# Topic 2 - Function how
#   - Defining function
#       def function_name(parameters):
#           statements
#   - Naming: same rules as naming a variable
#       - no keyword, first _ or letter, others _, letters, digit
#       - no space, no special symbols
#       - follow a style (snake_case), meaningful / descriptive name

# Example: a function printing message
def print_message():
    print('Hello')
    
# Example: a function reading int 19-59 until a valid one, print 'good'
def read_int():
    x = int(input('x = '))
    while x < 19 or x > 59:
        x = int(input('x = '))
    print('good')
    
# Example: a function reading two integerse, print multiples of 7 
def multiple_seven():
    x, y = int(input('Number 1: ')), int(input('Number 2: '))
    if x > y: x, y = y, x
    print('Multiple of 7: ', end='')
    for n in range(x, y+1):
        if n % 7 == 0: print(n, end = ' ')
        
#   - Calling function
#       - a function is executed only when being called
#       - how: function_name()
#       - a function can be called many times, from many places
#           - note: a recursive function calls itself
#       - entrance of program: main()
#           1. jump to the function being called
#           2. execute called function
#           3. jump back to the caller function
#       - pass statement: does nothing
#           - used in skeleton functions

def fun9():
    pass

def topic2_example():
    print_message()
    read_int()
    multiple_seven()
    

# Topic 3 - Passing data to function
#   - Example: print(value1, value2, value3, ...)
#       input(prompt_message)
#       int(string), round(value, number)
#   - def function_name(parameters):
#       - Multiple parameters: use comma
#   - Parameters: aka formal parameters
#       - in function definition
#   - Arguments: aka actual parameters
#       - values used in calling the function
#       - optional argument

# Example
def get_int(lower = 19, upper = 59):
    x = int(input(f'Enter an int between {lower} and {upper}: '))
    while x < lower or x > upper:
        x = int(input(f'Enter an int between {lower} and {upper}: '))
    print(f'Got a good number: {x}')
    
def func(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    
def topic3_tester():
    get_int(1, 20)
    get_int(50,80)
    get_int()
    
    func(12, 23, 24)
    
def sum_average(a, b):
    print(f'sum of {a} and {b} is: {a + b}')
    print(f'average of {a} and {b} is: {(a + b) / 2}')
    
def float_player(num):
    print(f'Square of {num}: {num ** 2}')
    print(f'Cube of {num}: {num ** 3}')
    print(f'Cube root of {num}: {num ** (1/3)}')
    print(f'Square root of {num}: {num ** (1/2)}')
    
def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0 and a + b > c \
        and a + c > b and b + c > a:
        print(f'{a}, {b}, and {c} can be the sides of a triangle')
    else:
        print(f'{a}, {b}, and {c} cannot be the sides of a triangle')

# Topic 4 - More about parameters
#   - Parameters are local variables
#       - local variables are defined in functions
#       - has a function scope(where can access it)
#       - multiple functions can have variables of the same name
#   - Positional parameters and Keyword parameters
#       - used when defining functions
#       - any parameteres before '/': require caller to pass by position
#       - any parameters after '*': require caller to pass by name

def foo(*, x, y):
    print(x, y)
    
def goo(a, b, /):
    print(a, b)
    
def topic4():
    foo (x = 123, y = 234)
    goo(23, 24)

def fun1(x, y):
    a = 123
    
def fun2():
    a = 234
    x, y = 1, 2
    fun1(x, y)

def main():
    topic2_example()
    topic3_tester()
    float_player(-1000)
    is_triangle(3, 4, 5)
    is_triangle(1, 2, 100)
    is_triangle(int(input('Please enter first number: ')), 
                int(input('Please enter second number: ')), 
                int(input('Please enter third number: ')))
    
main()