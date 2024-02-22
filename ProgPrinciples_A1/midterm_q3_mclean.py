#read two integers as start and stop numbers
#print a table of squares for the range of numbers (inclusive)
#print average of the squares

start_numb = int(input('Start number: '))
stop_numb = int(input('Stop number: '))

total_numb = count = 0

print(f'Number\tSquared')

for i in range(start_numb, stop_numb + 1):
    print (f'{i}\t{i ** 2}')
    total_numb += i ** 2
    count += 1

print(f'Average of squares: {total_numb / count}')