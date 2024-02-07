# Repitition - 1/3
# - iteration or loop
# - two types:
#   1. condition-controller loop (while statement)
#       - before the loop, no idea how many times to run
#   2. count-controlled loop (for statement, while statement)
#       - before the loop, already know the times to run
# 

# repeatedly asking for sales and commission rate, print the commission, until the user says no more sales
'''
choice = 'y'
while choice == 'y':
    sale = float(input('Sale amount: '))
    rate = float(input('Commission rate: '))
    print(f'Commission is {sale * rate / 100:.2f}')
    choice = input('More sale (y-Yes, other-no): ')

more_room = True
while more_room:
    width, height = int(input('Width: ')), int (input('Height: '))
    print(f'The area is {width * height}')
    answer = input('Do you have more room (y-yes, other-No)')
    if answer != 'y': more_room = False
    
    
radius = 0
while radius != -1:
    radius = int(input('Please enter the radius: '))
    print (f'The area of the circle is {radius * radius * 3.14}')
    
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

mark = float(input('Your mark: '))

while(mark >= 0):
    print('A+' if mark >= 90 else
          'A' if mark >= 80 else
          'B' if mark >= 70 else
          'C' if mark >= 60 else
          'D' if mark >= 50 else
          'F')   
    mark = float(input('Your mark: '))
    '''
#for loops

for colour in ['red', 'yellow', 'blue', 'green', 'black']:
    print(f'Current colour is: {colour}') 
    
for num in [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]:
    print(f'Current number is: {num}')    
    
for ch in 'Hello world':
    print(f'Current Character is: {ch}')    



#function range(): generate a sequence of values automatically
# - range(start, stop, step)
#   - 1 argument: stop, by default start = 0, step = 1


