# Comments: 
# - for people who read your code
# - Python interpreter will ignore them 

# Announments:
# - Finish intalling VS Code and Python, try it 
# - Complete Quiz 0, get 100% to move on
# - Assignment 1 posted, 5%, due in week 5
# - VS Code how-to:
#   - 1. create a folder for this course, e.g. "prog10004"
#   - 2. start VS Code, open the folder
#   - 3. create a new file, named it xxxx.py
#   - 4. run the file without debugging, check output window
# - How to learn:
#   - in class: listen, take notes, follow me to write demo code (optional)
#   - after class: review, read slides, notes, textbook, do exercises
#       - "Questions?" slide marks the break of classes 

# ====================================================

# Topic 1: How to write a program

# + Program Development
#   1. Design
#       - 1.1 Get requirements
#       - 1.2 Analyse requirements, get a solution (algorithm)
#           - algorithm: actions and order of the actions
#           - representation: pseudocode and flowchat
#               - Pseudocode: fake code, close to natural language
#               - Flowchat: boxes->actions, arrows->orders
#   2. Implementation
#       - write source code, save them into files named xxxx.py
#       - check code, fix errors (syntax errors, runtime errors)
#   3. Testing
#       - given inputs, check outputs against expected output
#       - check and fix logic errors 

# +. Errors
#   - Syntax errors: not following language rules 
#       - program doesn't run (doesn't compile)
#   - Runtime errors: runs but crash
#   - Logic errors: result is incorrect (bugs)

print('hello world')
# print('hello wolrd' # Syntax error
# print('hello world) # Syntax error
print('welcome to python')
# print(abc) # NameError - runtime error

# + IPO: general structure of an algorithm/solution
#   - Input: from user, network, files, input devices
#   - Processing: calculation, compress, search, sort, transform, ...
#   - Output: to console, save into a file, led, play sound

# Example: calculate and print the surface area and volume of a
#   cylinder, given the height and radius
# - Input: radius(r) and height(h)
# - Processing: 
#       area = 2 * pi * r * r + h * 2 * pi * r
#       vol = pi * r * r * h
# - Output: area and volume

# Do exercises on slide page 16-19
# - no need to write code, just identify IPO
# - after 2.1, come back to write code for the tasks 

# Exercise on page 16
# Define the inputs, processing, and outputs for a
# program that displays the future value of an
# investment for a principal P at a rate R compounded
# yearly for n years. The formula for compound
# interest is
# final amount = P(1+R/100)n
# - Input: principal(p), rate(r), years(n)
# - Processing: final amount = p x ( 1 + r / 100) ^ n 
# - Output: final amount

# ====================================================

# Topic 2: Program components 

# + Statements 
#   - a command, basic unit, an action to be carried out 
#   - block: a group of statements for a specific task
#   - function: prewritten/existing code, used directly (call a function)
#       - arguments: function may take/accept arguments

print('Today is a great day!') # a statement

# block: print the steps of putting an elephant into a fridge
print('1-open the fridge door')
print()
print('2-put the elephant in')
print()
print('3-close the fridge door')

print('Python is cool') # print is a function, message is the argument

# + Data types
#   - Strings(str): a sequence of characters in quotes ('...', "...", '''...''', """...""")
#       - 'Jack', '12345', "Sheridan College"
#       - '''Python is good''', """Today is a nice day."""
#       - Triple quotes are for multiline strings
#   - Integers(int): 1, 2, 3, -2, -33, -123, 0
#   - Float(float): 3.14, 1.0, 0.1, -3.45
#   - function type(value) to check the type of a value 

print('Jack Smith')
print("Alex Anna")
print('''Knowing is not enough, 
      You must apply''') # multiline string 
# I'm a 'good' professor 
print("I'm a 'good' professor") # single quotes in string, use ""
print('You are "great" students') # double quotes in string, use ''

print(123)
print(3.14)

# using print to print multiple values separated by comma 
# - Python will insert a space after each value 
# I am 25 years old.
print('I am', 25, 'years old.') # print 3 values 

# use type() to check type of value 
# <class 'str'> <class 'int'> <class 'float'>
print(type("abc"), type(123), type(-4.567))

# + Variables
#   - what: a reference to the value
#       - a named value, a container of a value
#   - how: 
#       - define and initialize:
#           variable_name = initial_value
#   - naming rules:
#       - can not use keywords to name variables (if, else, while, for)
#       - first character must be _ or letter(a-z, A-Z)
#       - other characters must be _ or letters or digits(0-9)
#       - no spaces or special symbols(!@@#$%^&*(),.)
#       - descriptive name
#       - follow a styles (CamelCase, lowerCamelCase, snake_case)
#           - Examples: StudentMark, studentMark, student_mark
#           - most popular: snake_case 
#   - Notes:
#       - value can be changed (re-assign a new value)
#           - old value -> garbage collection in Python
#       - value can be of different types 
#       - assign multiple values to multiple variables in one statement

name = 'Jack Anna' # define a varible named name, assign an initial value 'Jack Anna'
age = 18 # a variable named age, having init value 18
salary = 34567.89 # a variable named salary, assigned an init value 
print('My name is', name, 'and I am', age, 'years old')
print('I make', salary, 'amount of money per year.')

age = 17 # re-assign new value 
name = 'Jack Smith'
print(type(name), type(age), type(salary)) # str, int, float 

age = 'Twenty'
print(type(age)) # str

x, y, z = 12, 23, 34 # x = 12, y = 23, z = 34 

# Do exercises on page 35-37
