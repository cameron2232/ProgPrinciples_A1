# Annoucement:
# - room changed, Mon: B301, Wed: E205

# Topic 1 - Nested loop
#   - while/for loop in another while/for loop 

# Example: while in while 
# - keep on reading product name until 'done'
#   for each product, read the amount of sales
#   print the product that has the top sales
#   Make sure the amount is not negative

top_product, top_amount = '', 0.0
product = input('Product name: ')
while product != 'done':  # outer loop
    amount = float(input('Sale amount: '))
    while amount < 0:     # inner loop
        amount = float(input('Sale amount: '))
    if amount > top_amount:
        top_amount = amount 
        top_product = product
    product = input('Product name: ')
print(f'Top product: {top_product}, Top amount: {top_amount}')

# Example: for in for 
# - print time from 0:0:0, 0:0:1, 0:0:2, ... to 23:59:59
for hour in range(24):
    for min in range(60):
        for sec in range(60):
            print(f'{hour}:{min}:{sec}', end='\r') 

# Exercises on slide page 48
            
# • Read width and height from the user, print the triangle
# and rectangle using “$”.
# width = 4, height = 5
# $
# $$
# $$$
# $$$$                                    

# $$$$
# $$$$
# $$$$
# $$$$
# $$$$

width, height = int(input('Width: ')), int(input('Height: '))
for x in range(1, width + 1):   # rows 
    for y in range(x):          # columns
        print('$', end='')
    print() 
print()

for h in range(height):     # rows 
    for w in range(width):  # columns
        print('$', end='')
    print()

# • Use nested for loops to print a multiplication table.            
#   1x1=1   1x2=2   ...         1x9=9
#   2x1=2   2x2=4   ...         2x9=18
#   ...
#   9x1=9   9x2=18  ...         9x9=81
    
# - outer loop: rows, innerloop: columns
for a in range(1, 10):  # a = 1, 2, ..., 9
    for b in range(1, 10):  # b = 1, 2, ..., 9 
        print(f'{a}x{b}={a * b}\t', end='')
    print() # print a new line after each row 

# Topic 2 - break, continue, else 
# - break: used in a loop, immediately terminate the loop
# - continue: used in a loop, immediately start the next iteration
# - else: used in a loop, executed only when loop is stopped not using break 
        
# Example: repeatly read marks from student, until a perfect 

# ver1
mark = int(input('Mark: '))
while mark != 100:
    mark = int(input('Mark: '))
print('A perfect mark')            

# ver2
perfect = False  # Flag
while not perfect:
    mark = int(input('Mark: '))
    if mark == 100: 
        perfect = True 
print('A perfect mark')

# ver3: break 
while True:
    mark = int(input('Mark: '))
    if mark == 100:
        break # terminate the loop 
print('A perfect mark')

#ver4: continue 
repeat = True 
while repeat:
    mark = int(input('Mark: '))
    if mark != 100: 
        continue  # start next iteration in the loop immediately
    repeat = False 
print('A perfect mark')    

# Example: using else with loop 
# - read two integers, lower, upper, check if any number in between
#   is a multiple of 11
# - e.g. 12 25 - 22
# - e.g. 14 19 - No good number 
lower, upper = int(input('Lower: ')), int(input('Upper: '))
for num in range(lower, upper + 1):
    if num % 11 == 0: 
        print(num)
        break 
else: # will be executed when the for loop is stopped normally 
    print('No good number')    

# Exercise on slide page 59
    