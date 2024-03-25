# Lists - 1/3

# Topic 1 - List basics 
# - what: a sequence of data 
#   - data in list is ordered 
#   - can contain duplicated data 
#   - can contain data of different types 
#   - is mutable
# - create a list: [,,,], [], list(range()), *, + 
# - basic operations: print(), len(), list[index], loop-through
# - 2D list: 2-dimensional list (lists in a list)
#   - loop-through: nested for-loop

def list_basics():
    # 1. create a list 
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    colors = ['red', 'blue', 'black', 'grey', 'green', 'yellow']
    lst = [] # empty 
    heros = ['spiderman', 17, 8.8, 
             'superman', 28, 8.9,
             'hulk', 23, 9.9] # data of different types
    # parallel lists
    names = ['spiderman', 'superman', 'hulk']
    ages = [17, 28, 23]
    power = [8.8, 8.9, 9.9]
    # using range()
    nums = list(range(2, 21, 2)) # [2, 4, 6, 8, ..., 20]
    # using *, + 
    lst1 = [1, 2, 3]
    lst2 = lst1 * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]
    counters = [0] * 100 
    lst3 = ['a', 'b', 'c']
    lst4 = lst1 + lst3 # [1, 2, 3, 'a', 'b', 'c]

    # 2. basic operations 

    # print
    nums = [11, 3, 9, 2, 8, 4, 5, 7]
    print(nums)

    # get the length(number of elements): len(list)
    length = len(nums)
    print('The size of the list is', length) # 8

    # access (get or update the value) elements in list 
    # - using index(position number)
    #   - indics: 0, 1, 2, ..., len(list) - 1 
    #   - negative:  -len(lst), ..., -3, -2 , -1
    nums[0] = 1 
    nums[7] = nums[7] + 1
    a = nums[3] # forth element: 2 

    # loop through
    # - for in, for in range()
    # - while 
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for day in days:
        print(day)
    for ind in range(len(days)): # ind = 0, 1, 2, ..., 6
        print(f'days[{ind}]={days[ind]}')
    students = ['jack', 21, 3.2,
                'anna', 17, 3.8,
                'alex', 23, 2.4] # names are at 0, 3, 6, 9, 12, ...
    for ind in range(0, len(students), 3): 
        print('Name at', ind, 'is', students[ind])

    ind = 0
    while ind < len(students):
        print(students[ind])
        ind += 1 

    # 3. 2D list
    table = [ [1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]] 
    # loop-through 2d list: nested for loop
    # element: table[row][col]: 0,0  0,1  0,2  1,0  1,1  1,2  2,0  2,1  2,2
    for row in table: # outer loop
        for col in row: # inner loop 
            print(col, end=' ')
        print()

    for row in range(len(table)):
        for col in range(len(table[row])):
            print(f'table[{row}][{col}]={table[row][col]}\t', end=' ')
        print()

# exercise on page 8
def exercise_p8():
    # Create the following list. Use print to print the content of each
    # list. Use for loop to iterate through each list
    # – A list containing names of your four favorite games
    games = ['Tetris', 'Red Alert', 'Minecraft', 'Clash of Clans']
    
    # – A list containing all your marks of 6 courses
    marks = [9.2, 8.3, 7.4, 6.5, 9.8, 6.4]    
    
    # – A list containing odd numbers from 1 to 9
    odds = list(range(1, 10, 2))

    # – A list containing your id, name, address, phone number
    my_info = [123423, 'ProfSun', '100 Main Str.', '+1-905-123-4567']

    # – A list containing a number of 100 zeros (Hint: use *)
    zeros = [0] * 100

    # – An empty list
    emt = [] 

# exercises on page 15 and 16
 
# Topic 2 - List more 
# - using in and not in to check the existance of an element 
# - slicing: list[start:stop:step]
# - methods: append(value), insert(index, value), 
#       remove(value), pop(index), clear()
#       index(value), reverse(), sort(), count(value)
# - built-in functions: del, min(), max(), sum() 
    
def list_more():
    # 1. search to check if a value is in or not in a list 
    # - using value in / not in list: True/False
    lst1 = list(range(10, 21)) # [10, 11, ..., 30]
    age = 6
    if age in lst1: print('list has this age')
    if age not in lst1: print('list has no this age')

    # 2. slicing: get a sublist from a list 
    #   - sublist = list[start:stop:step] 
    #   - by default: start=first, stop=last, step=1
    print(lst1) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    lst2 = lst1[:] # a copy 
    lst3 = lst1[::-1] # a reverse 
    evens = lst1[0::2] 
    odds = lst1[1::2]
    smalls = lst1[:len(lst1) // 2]
    bigs = lst1[len(lst1) // 2:]
    lst4 = lst1[3:5] 
    print(lst2, lst3, lst4)
    print(evens, odds)
    print(smalls, bigs)

    students = ['jack', 21, 3.2,
                'anna', 17, 3.8,
                'alex', 23, 2.4] 
    names = students[0::3]
    ages = students[1::3]
    marks = students[2::3]
    print(names, ages, marks)

    # 3. list methods
    # - methods: functions used to a specific value 
    # - add new: append(value), insert(index, value)
    # - delete: remove(value), pop(index), clear()
    # - others: index(value), count(value), reverse(), sort() 
    #   - sort(): all elements in list must be comparable 
    
    # append
    print(lst1) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    lst1.append(33)
    lst1.append(44)
    print(lst1)

    # insert
    lst1.insert(0, 999)
    lst1.insert(5, 777)
    print(lst1)
    lst1.insert(100, 333)
    print(lst1)

    # remove
    lst1.remove(333) # remove the first occurrance of the value
    if 555 in lst1: lst1.remove(555)

    # pop
    x = lst1.pop(0) # 999 is removed
    y = lst1.pop()  # last element removed 
    # lst1.pop(100) # IndexError
    print('Removed values:', x, y) # 999, 44

    # other methods: index, count, sort, reverse
    lst = [9, 8, 8, 4, 7, 7, 5, 1, 2, 2, 3]
    ind = lst.index(7) # 4
    count = lst.count(2) # 2
    print(ind, count)
    lst.sort() # ascending order 
    print(lst)
    lst.reverse()
    print(lst)
    names = ['jack', 'bob', 'alice', 'ethen', 'david']
    names.sort()
    print(names) # ['alice', 'bob', 'david', 'ethen', 'jack']

    # 4. built-in functions: del, min(), max(), sum()
    nums = list(range(11)) # [0, 1, 2, ..., 10]
    del nums[5]
    del nums[:3]
    mini = min(nums) # 3
    maxi = max(nums) # 10 
    total = sum(nums) # 
    print(mini, maxi, total, nums) # 3 10 47 [3, 4, 6, 7, 8, 9, 10]
    if len(nums) > 0: 
        average = sum(nums) / len(nums)
        print('average is', average)

    # example:
    employees = ['alex', 22, 234.23, 'balex', 34, 97.32, 'calex', 45, 888.22]
    # increment age by 1, salary by 10%
    for i in range(0, len(employees), 3):
        # i - name, i+1 - age, i+2 - salary
        employees[i + 1] += 1 
        employees[i + 2] *= 1.1
    print(employees) # ['alex', 23, 257.653, 'balex', 35, 107.052, 'calex', 46, 977.0420000000001] 

# exercises on page 25 and 26
    
def main():
    # list_basics()
    list_more()

main()

