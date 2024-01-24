# Topic 1 - control structures
# - Sequence: write first, run first, run one next to the other
# - Decision (selection):
#   - Based on a condition, decide to do or not to do, or decide
#       to do this or do that
#   - Single Alternative (one-way selection)
#       - if it is raining, then ring your umbrella 
#   - Duel Alternative (two-way selection)
#       - if vit is raining, umbrella, otherwise, sunglasses
#   - Multiple Selection (match-case, out of scope)
# - Repition (Iteration, Loop): Ch4, 3 classes
#   - do something repeatedly

# Topic 2 - Condition
#   - Boolean expression: two possible values, True or False
#   - 6 relational operators: comparison
#       - > (greater than), >= (greater than or equal to)
#       - < (less than), <= (less than or equal to)
#       - == (equal to), != (not equal to)
#   - String comparison:
#       - Each character in a string has a number (ASCII)
#       - 'Welcome' vs 'welcoMe': find first different char,
#           - 'm' : 'M' - 109 : 077 ---> 'welcome' > 'welcoMe'

x, y = True, False;
print(x, y, type(x), type(y)); #True false <class 'bool'> <class 'bool'>
a1 = 12 > 23 #False
b1 = 34.45 >= 23.34 #True
print(a1, b1)
a2, b2 = 234 < 202, 2345 <= 2345
print(a2, b2) #False, True
a3, b3 = 123 == 234, 234 != 234
print(a3, b3) #False, False

s1, s2 = 'welcome', 'welcoMe'
print(s1 < s2) #Falsem 'm' > 'M'

# Topic 3 - Single Alternative (one-way selection): if statement
# - Syntax:
#   - if condition:
#       - statement 1
#       - statement 2
#       - ...
#   - Logic: when condition is true, run if block
#   - Note: If block needs to be indented once
#   - Note: when block has one statement, write it one line
#       - if condition: statement

weather = input('What is the weather like: ')

if weather == 'raining': print('Bring an umbrella')

print('Have a good day')

guest = input('What is your name: ')
age = int(input('How old are you: '))
print(f'hi {guest}, welcome, havea  drink')
if age < 19: print('Oh you are still young, get a water')

x, y = int(input('number 1: ')), int(input('number 2: '))
bigger = x
if x < y:
    bigger = y
print(f'The bigger one is {bigger}')

# Topic 4 - Duel Alternative (two-way selection): if/else statement

mark = int(input('Plese enter your mark: '))

if mark >= 50: print('Congrats! You passed')
elif mark <= 50: print('Uh oh. You failed')

num1 = int(input('First number: '))
num2 = int(input('Second number: '))
if num1 % num2 == 0: print(f'{num1} is a multiple of {num2}')
else: print(f'{num2} is not a factor of {num1}')

pay = 10000.00
score = int(input('Score: '))
if score > 90: pay *= 1.03
else: pay *= 1.01
print(pay)

#Write a program to calculate the total payments of movie
#tickets. One ticket is $7.50. If you buy 10 or more, you get
#a 2% discount. If you are a VIP, you get another 10%
#discount. If it is weekend, you get another 5% discount.

tickets = int(input('Enter number of tickets ($7.50 each, 10+ discount: 2%): '))
VIP = input("Are you a VIP (VIP discount: 10%) (Y/N): ")
weekend = input('Is today Saturday or Sunday (Weekend discount: 5%) (Y/N): ')

if tickets < 10: ticket_price = tickets * 7.50
else: ticket_price = tickets * (7.50 * 0.98)

if VIP == 'Y': ticket_price *= 0.90
if weekend == 'Y': ticket_price *= 0.95
print(f'Total Payment: ${ticket_price:.2f}')