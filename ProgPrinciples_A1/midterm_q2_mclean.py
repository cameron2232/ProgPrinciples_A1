# read two integers check and print if even or odd
# 

numb_one = int(input('First integer: '))
numb_two = int(input('Second integer: '))

if numb_one % 2 == 0 and numb_two % 2 == 0:
    print('Both are even.')
elif numb_one % 2 == 1 and numb_two % 2 == 1:
    print('Both are odd.')
else: 
    print(numb_one, 'is', 
          'even, ' if numb_one % 2 == 0 else 
          'odd, ', numb_two, 'is ',
          'even.' if numb_two % 2 == 0 else
          'odd.') 
    