# Review
# Exercise: given a list, print unique elements
# - [5, 2, 3, 5, 2, 2, 4, 3, 1, 2] -->[5, 2, 3, 4, 1]
def print_uniques(lst):
    temp = []
    for ele in lst:
        if ele not in temp:
            temp.append(ele)
    print(temp)
    # homework: try to find a way without using temp list

# ================================================================
    
# Topic 1 - Tuples
# - a sequence of data that is immutable
# - create: (,,,)
# - can not do: add new, update, delete 
# - can do: get element, indexing, slicing, loop-through, search, count    

def about_tuples():
    seasons = ('spring', 'summer', 'autumn', 'winter')
    for i in range(len(seasons)):
        print(seasons[i])
    # seasons[2] = 'fall' # TypeError: 'tuple' object does not support item assignment

# ================================================================
        
# Topic 2 - List processings 
# - make a copy: .copy(), []+, [:], for-loop
# - delete an element: .remove(value), .pop(index)
# - get random: choice(), choices(), sample() 
#   - 3 functions can be used to strings        
# - read from file to list: readlines()

def list_processings():
    # make a copy 
    lst1 = [1, 2, 3, 4, 5]
    lst2 = lst1 # doesn't work 
    # for-loop 
    lst3 = []
    for n in lst1: lst3.append(n)
    # .copy()
    lst4 = lst1.copy()
    # [] + 
    lst5 = [] + lst1 
    # slicing
    lst6 = lst1[:]

    # delete an element 

    # Example: [5, 2, 4, 3, 2, 2, 1, 4, 4, 7, 6, 6]
    # - delete all even numbers 

    num = [5, 2, 4, 3, 2, 2, 1, 4, 4, 7, 6, 6]
    # ver1: remove() doesn't work
    for n in num:
        if n % 2 == 0:
            num.remove(n)
    print(num) # [5, 3, 2, 1, 4, 4, 7, 6]
    # homework: find a way using remove() to do it

    num = [5, 2, 4, 3, 2, 2, 1, 4, 4, 7, 6, 6]
    # ver2: pop(index)
    # for i in range(len(num)):
    #     if num[i] % 2 == 0:
    #         num.pop(i)
    # print(num) # IndexError: list index out of range

    # ver2': using pop() loop-through in reverse 
    for i in range(len(num) - 1, -1, -1): # i = 11, 10, 9, ..., 2, 1, 0
        if num[i] % 2 == 0:
            num.pop(i)
    print(num) # [5, 3, 1, 7]
    # homework: using while loop to do this
    
    # get random element(s) from a list 
    # - random.choice(lst): get a random element
    # - random.choices(lst, k=): get a random sublist, with replacement
    # - random.sample(lst, k=): get a random sublist, without replacement
    import random 
    num = list(range(10, 31)) # [10, 11, 12, ..., 30]
    r = random.choice(num)
    rl1 = random.choices(num, k=88)
    rl2 = random.sample(num, k=8)
    print(r, rl1, rl2)

    str1 = '1234567ytgfdcxkzjbsnmw23r4thgva,q]=e[rhgnds]'
    rand_chars = random.choices(str1, k=10)
    print(rand_chars) # ['a', '1', '4', 'r', 'h', ....]

    # readlines()
    # - create a file containing 10000 random -100 to 100 
    # - read from the file, print average 
    with open('numbers.txt', 'w') as f:
        for _ in range(10000):
            f.write(str(random.randint(-100, 100)) + '\n')
    with open('numbers.txt', 'r') as f:
        numbers = f.readlines() 
    print(numbers)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    print(sum(numbers) / len(numbers))

# >> Break 

# ================================================================
    
# Topic 3 - Functions with lists
# - function accepting lists as arguments
# - function returning lists as value 

# Example1: given a list of numbers, double all numbers in it 
# [1, 2, 3] --> [2, 4, 6]
def double_list(num):
    for i in range(len(num)):
        num[i] *= 2 

# Example2: given a list of numbers, return two lists 
# containing small and big numbers 
def split_list(lst):
    small, big = [], [] 
    avg = sum(lst) / len(lst) 
    for n in lst:
        if n < avg: 
            small.append(n)
        else:
            big.append(n)
    return small, big 

# ================================================================
        
# Topic 4 - List comprehensions
# - an easier way to get a new list from an existing list 
# - mapping
#   - regular way: []-->for-->append
#   - [expression for n in lst]
# - filtering
#   - regular way: []-->for-->if-->append 
#   - [expression for n in lst if condition]

def list_comprehensions():
    lst = [5, 2, 7, 4, 3, 6, 1]
    # create a new list with elements to be the square of lst
    # [25, 4, 49, 16, 9, 36, 1]
    # regular: []-->for-->append
    squares = []
    for n in lst:
        squares.append(n ** 2)
    print(squares) # [25, 4, 49, 16, 9, 36, 1]

    squares1 = [n ** 2 for n in lst] # list comprehansion to do the same
    print(squares1)

    lst = [5, 2, 3, 4, 7, 6, 8, 1, 11, 10]
    # create a new list from exising list containing only odd numbers
    # regular: []-->for-->if-->append
    odds = []
    for n in lst:
        if n % 2 != 0:
            odds.append(n)
    print(odds)

    odds1 = [n for n in lst if n % 2 != 0] # list comprehension to do same
    print(odds1)

# Exercises on page 34(processings) and 43(comprehension)
    
# >> Break 

# Game Time 

def main():
    list_comprehensions()
    # lst = [1, 2, 3]
    # double_list(lst)
    # print(lst) # [2, 4, 6]
    # lst = [23, 23, 11, 22, 66, 77, 21, 12, 7, 9, 15]
    # x, y = split_list(lst)
    # print(x, y) # [23, 23, 11, 22, 21, 12, 7, 9, 15] [66, 77]

    # list_processings()
    # about_tuples()
    # print_uniques([5, 2, 3, 5, 2, 2, 4, 3, 1, 2])

main()

