# Lists - 3/3

# Review: regular way vs. python - try to code in python style
# example: given a list of superheros 
#  [name1, strength1, fly1, name2, strength2, fly2...]
# - get 3 parallel lists from the list
# - get a list of names who can fly
def our_heros(heros):
    # 1. parallel list: names, strengths, flies
    # ver1: regular way
    names, strengths, flies = [], [], []
    for i in range(0, len(heros), 3): # i = 0, 3, 6, 9, 12, 15, 18, ...
        names.append(heros[i])
        strengths.append(heros[i + 1])
        flies.append(heros[i + 2])
    print(names, strengths, flies)    

    # ver2: python way 
    names, strengths, flies = heros[::3], heros[1::3], heros[2::3]
    print(names, strengths, flies)

    # 2. names who can fly 
    # ver1: regular way
    can_fly = []
    for i in range(0, len(heros), 3):
        if heros[i + 2]:
            can_fly.append(heros[i])
    print(can_fly)

    # ver2: python way 
    can_fly = [heros[i] for i in range(0, len(heros), 3) if heros[i + 2]]
    print(can_fly)

# ===================================================
    
# Topic 1 - Searching
# - provided: count(value), index(value), in/not in 
# - linear search: mostly the only choice 
# - binary search: used to sorted list 

def searching():
    num = [5, 3, 2, 2, 4, 2, 3, 4, 5, 1, 6]
    c = num.count(2) # 3 
    i = num.index(3) # 1
    b1 = 6 in num    # True
    b2 = 7 not in num # True 
    print(c, i, b1, b2) # 3 1 True True

def my_search(lst, key):
    # return a list containing the indices of key in the list
    
    # [1, 2, 2, 3, 2, 3], key=2 ---> [1, 2, 4]
    # result = []
    # for i in range(len(lst)):
    #     if lst[i] == key:
    #         result.append(i) 
    # return result 

    return [i for i in range(len(lst)) if lst[i] == key]

# ===================================================

# Topic 2 - Sorting
# - re-order elements in list in ascending or decending order 
#    [7, 2, 3, 5, 4, 6, 8, 1] --> [1, 2, 3, 4, 5, 6, 7, 8]
# - many algorithms: seletion, insertion, mergy, quick, heap, ...
# - bubble sort: smaller going to beginning, bigger goint to end
#   - each round moves one number to its position
#   - in a round, compare adjacent elements, swap if wrong order

#  5 2   5 > 2  swap 2 5
#  5 3 1 5 > 3  3 5 1
#        5 > 1  3 1 5
#        3 > 1  1 3 5
#  7 2 3 5 1
#  2 7 3 5 1
#  2 3 7 5 1
#  2 3 5 7 1
#  2 3 5 1 7 --> 1st round, 7 is ready
#  2 3 1 5 7 --> 2nd round, 5 is ready
#  2 1 3 5 7 --> 3rd round, 3 is ready
#  1 2 3 5 7 --> 4th round, 2 is ready

# optimization
# 1 - in round, no need to compare ready numbers
# 2 - for list of size n, need n - 1 rounds
# 3 - in a round if no swap, sorted, have an early stop

def bubble_sort(lst):
    # nested-for loop: outer --> round, inner-->compare & swap
    for i in range(len(lst) - 1):
        swapped = False # flag
        for j in range(len(lst) - 1 - i): 
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True 
        if not swapped: break # early stop

# Exercises on page 56

def main():
    import random
    rnd = [random.randint(10, 50) for _ in range(20)] # 20 random numbers
    print('Before sorting:', rnd)
    bubble_sort(rnd)
    print('After sorting:', rnd)

    # num = [1, 2, 5, 2, 2, 3, 2, 4, 6]
    # print(my_search(num, 2)) # [1, 3, 4, 6]

    # searching()
    # superheros = ['spiderman', 82.3, False,
    #               'superman', 93.2, True,
    #               'batman', 65.3, False,
    #               'hulk', 98.8, True]
    # our_heros(superheros)
main()

# Guest speaker (5:25 10min-20min) !!!!!

# >> Break

# Lab 3

