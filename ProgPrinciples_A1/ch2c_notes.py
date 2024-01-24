# Example heading comment:
# Name: ch2c_notes.py
# Author: Prof. Sun
# Date: Jan 17, 2024
# Version: 1.0
# Description: the last class about Chapter 2 - Fundimentals
#   Some review and small topics.

# Announcement:
# - Quiz 1 next week on Mon, check announcement for details

# Review on previous class

# + Input
#   - function input(prompt), return a string
#   - use function int(...) or float(...) to convert to number
#   - function chaining: num = int(input('give me a number: '))
#   - function round(value, number), number by default 0
#       - number is number of digits after decimal point

a = int(56.78) # a is 56, no rounding
print(a)
a = round(56.78) # 57
print(a)
print(round(13.579, 1), round(2523.3232, 3)) # 13.6 2523.323

# + Arithmetic
#   - operators: +, -, *, /, %, **, //
#   - operands: positive and negative, int and float
#   - /(division): result is a float, divisor cannot be zero
#   - %(remainder): divisor cannot be zero, when divisor is negative
#   - **(exponent): x ** y ** z = x ** (y ** z), right to left
#   - //(integer division): divisor cannot be zero

# Exercise on slide page 55
# Write a Python program that asks the user to enter
# –the initial velocity and acceleration of an object, and
# the time that has elapsed,
# –places them in the variables u, a, and t, and
# –prints the final velocity, v, and distance traversed, s,
# using the following equations.
# Get inputs from the user
u = float(input('Initial velocity(m/s): '))
a = float(input('Acceleration(m/s^2): '))
t = float(input('Time(in second): '))

# Using provided equations to calculate the final speed and distance
v = u + a * t
s = u * t + 0.5 * a * t ** 2

# Print the result
print('Final velocity:', v)
print('Distance:', s)

# Exercise on slide page 61
# (Separating Digits in an Integer) Write a program
# that
# • inputs one five-digit number,
# • separates the number into its individual digits
# • prints the digits separated from one another by three
# spaces each.
# • For example, if the user types in 42139, the program
# should print: 4 2 1 3 9

num = int(input('Please give me a 5-digit integer: '))
# num = 42139 
# d5,d4,d3,d2,d1
# 42139 % 10 -> 9
d1 = num % 10
# 42139 // 10 -> 4213 % 10 -> 3
d2 = num // 10 % 10 
# 42139 // 100 -> 421 % 10 -> 1
d3 = num // 100 % 10
d4 = num // 1000 % 10
d5 = num // 10000 # no need % 10
print(d5, '  ', d4, '  ', d3, '  ', d2, '  ', d1)

# Homework: try to do it in another way to get d5 first, then d4, d3, d2, d1

# ===============================================================
# Topic 1: programming styles
#   - read submission standard
#   - Commenting (Documentation): help reader understand the code
#       - Heading comments (name, author, version, date, description)
#       - Internal comments (on top of code segment/block, somewhere logic complicated)
#           - One-line comment, in-line comment
#   - Naming: meaning name(self-documentation), follow style(snake_case)
#   - Spacing: 
#       - one space before and after an operator
#       - one space after a comma
#       - no space in function name and ()
#       - inside (), no space before/after the first/last item
#       - indentation: a must, 4 spaces for one level 
#   - Line length
#       - keep all lines in 80 characters (column width)
#       - to separate a long line into multiline: add \ 
#       - anything inside (), no \ is needed

a = 321 + 213 - 345 * 897 / 123.5
print(321, 'hello', 123.45, type(a))
x = input('x = ')

regular_hourly_payment, regular_hours = 17, 20
extra_hourly_payment, extra_hours = 35, 7
total_payment = regular_hourly_payment * regular_hours \
                + extra_hourly_payment * extra_hours
print(123, 'hello world',
      234, 'welcome python', 
      345, 'good day guys') # separate to 3 lines, no need of \

# ===============================================================
# Topic 2: string concatnation
#   - use + to connect two strings
#   - implicit concatnation: 'string1' 'string2'
#   - for numbers, convert first using str(...)
name = 'Jack'
# Hello Jack, how are you
print('Hello', name, ', how are you') # Hello Jack , how are you
print('Hello ' + name + ', how are you') # Hello Jack, how are you
name = 'Jack' 'Anna' # JackAnna, implicit concatnation
print(name)
print('My age is ' + str(23))

# ===============================================================
# Topic 3: print()
#   - ending: by default is a new line, change using end='...'
#   - separator: by default is a space, change using sep='...'
#   - escape(\?): new line (\n), tab(\t), '(\'), "(\"), \(\\)

print('Hello everyone', end=' ') # change ending from new line to a space
print('How is going today')

print(123, 234, 345) # 123 234 345
country = 1
city = 905
number = 5232
print(country, city, number, sep='-') # 1-905-5232, new separator is -
year, month, date = 2004, 8, 12
print(year, month, date, sep='/') # 2004/8/12, new separator is /

print('Hello everyone,\nToday is a good day') # \n means new line
print('No.\tName\tAge\tMark\tNote') # table header with tabs
# I'm in "Love" with 'Python'
print('I\'m in \"Love\" with \'Python\'')
# In Python \n is a new line
print('In Python \\n is a new line')

# ===============================================================
# Topic 4: f-string (formating string)
#   - a string prefixed with a f
#   - can have placeholders {....}, can be a value, an expression, a variable
#   - string: alignment (< ^ >) and width
#   - integers: alignment and width, comma-separated 3-digit, percentage(%)
#       - d - integer type
#   - float: alignment and width, comma-separated, percentage, precision
#       - f - float, e - scientific notation (1.234e+3 = 1.234 x 10^3)

message = f'hello world'
name = 'Jack Alex'
age = 19
score = 8.2352345
print(name, age, score)
print(name + str(age) + str(score))
print(f'My name is {name}, I am {age}, the score is {score}')

address = input(f'Hello {name}, where are you living: ')

print(f'My name is {name:<30}') # < is align to left, 30 is width
print(f'My name is {name:^30}')
print(f'My name is {name:>30}')

# 6,543,213,456
print(f'The number is {6543213456:,d}') # , 3-digit separated, d - integer
print(f'The number is {6543213456:^25,}') 
print(f'The percent is {23:%}') # 2300.000000%

salary = 35532.345345
# 35532.35
print(f'My salary is {salary:.2f}') # .2 means keep two digits, f means float type

# Exercise on slide page 19
# You entered your five grades as: 
# 85.6 78.9 75.5 90.0 86.5 
# Your average grade: 83.3
mark1 = float(input('Python: '))
mark2 = float(input('Networks: '))
mark3 = float(input('Math: '))
mark4 = float(input('English: '))
mark5 = float(input('Database: '))
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
print(f'You entered marks like this: {mark1}, {mark2}, ' +
      f'{mark3}, {mark4}, {mark5}. The average is ' +
      f'{average:.2f}.')

# Do others on page 16-19 at home
# Do theory exercise in folder Ch02 or from Quizzes
