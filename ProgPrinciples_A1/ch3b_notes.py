from logging import basicConfig


mark = float(input('Enter your mark: '))
print('Pass' if mark >= 50 else 'Fail')

x, y = 12, 23
maxi = 0
if x > y: maxi = x
else: maxi = y
#equivalent
maxi = x if x > y else y

n = int(input('Your favourite: (1-Spring,; 2-Summer; 3-Autumn; 4-Winter): '))
print('Your favourite season is:', 
    'Spring' if n == 1 else
    'Summer' if n == 2 else
    'Autumn' if n == 3 else
    'Winter' if n == 4 else
    'Not a valid number')

# Assignment expression
#   - walrus operator         variable := value
#   - it is an expression, not a statement
#   - 1) define variable, initialiaze it;
#   - 2) return the value
#   - Note: has lowest priority, mostly used in (...)

a, b = 1234, 345233
numSum = a + b
if numSum % 7 == 0:
    print('The sum is a multiple of 7')
    
if (total := a + b) % 7 == 0:
    print('The sum is a multiple of 7')
    
# Nested decision
#   -if/else in if/else
# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz