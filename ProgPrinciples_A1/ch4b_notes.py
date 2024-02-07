# Review on loop 1

# + while loop
#   - condition-controlled loop
#   - while condition:
#       statements
#   - used as count-controlled: 1) initialization; 2) comparison; 3) update 
#   - pretested loop, check condition before running loop or not, no infinite loop

# + for loop
#   - count controlled loop
#   - for variable in range (values):
#       statements
#   - values: list([,,]), string range
#   - range(start = 0, stop, step = 1), all integers, step can be negative
for i in range(100, 0, -1):
    print(i, end = ' ')
print()

# exercise on slide 15
# read a nonnegative integer, compute and print its
# factors, determine whether it is a prime number

num = prime = 0

while num <= 0:   
    num = int(input('Please enter a positive integer: '))
    if num <= 0: print ('Error: must enter a positive integer.')
    
print(f'Factors of {num}:', end = ' ')
for i in range(1, num+1):
    if num % i == 0: 
        print(i, end = ' ')
        prime += 1

print()

if prime == 2: print(f'{num} is a prime number')
else: print(f'{num} is not a prime number')

# Repition - 2/3

# Topic 1 - Augmented assignment
# - update variable by doing something to it
# - operators: +, -, *, /, %, **, //
# - augmented assignment: +=, -=, *=, /=, %=, **=, //=
a = 10
a = a + 1
a += 1 #the good way

b = 12
b = b - 2
b -= 2

c = 20
c = c * 3
c *= 3


# Topic 2 - Get running total
# - define an accumulator variable, initialized to 0

# what is the sum of 1, 2, ... 100
sum = 0
for x in range(1, 101):
    sum += x
print(f'Sum of 1 to 100 is {sum}')

#keep depositing until no more money, what is balance
balance = 0
more_money = input('More money (y-yes): ')

while more_money == 'y':
    amount = float(input('How much to deposit: '))
    balance += amount
    more_money = input('More money (y-yes): ')
print(f'Balance is {round(balance,2)}')

# Topic 3 - Sentinel 
# - a signal to mark the end of a sequence of data
# - a special value to tell the program there is no more data
#   Example: mark(-1), name($)

#Example, read radius, print area, until radius is -1 
radius = float(input('Enter radius (-1 to stop): '))
while radius != -1:
    print(f'Area is {3.14 * radius * radius}')
    radius = float(input('Enter radius (-1 to stop): '))

#Topic 4 - Input validation
# - garbage in, garbage out
# - use a while loop

# Example: read age(18, 60), if not valid, read again

age = int(input('Your age: '))
while age < 18 or age > 60:
    print('Age must be 18-60')
    age = int(input('Your age: '))
print(f'A valid age: {age}')

color = input('Traffic light color: ')
while color != 'red' and color != 'green' and color != 'yellow':
    print('Not a valid color')
    color = input('Traffic light color: ')
print('Stop' if color == 'red' else
      'Lets go' if color == 'green' else
      'Be careful')